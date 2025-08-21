from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
)
from homeassistant.const import PERCENTAGE
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import DurlemCoordinator


SENSORS: list[tuple[str, str, str | None, SensorDeviceClass | None, str]] = [
    ("remaining_capacity", "Durlem Remaining Capacity", PERCENTAGE, None, "mdi:water-percent"),
    ("low_salt", "Durlem Low Salt", None, None, "mdi:alert-circle-outline"),
    ("working", "Durlem Working", None, None, "mdi:cog-sync"),

    ("last_regeneration_at", "Durlem Last Regeneration", None, SensorDeviceClass.TIMESTAMP, "mdi:history"),
    ("next_regeneration_at", "Durlem Next Regeneration", None, SensorDeviceClass.TIMESTAMP, "mdi:calendar-clock"),

    ("regeneration_count_since_reset", "Durlem Regeneration Count", None, None, "mdi:counter"),
    ("hardness", "Durlem Hardness", "°f", None, "mdi:water-opacity"),
    ("installation_date", "Durlem Installation Date", None, SensorDeviceClass.TIMESTAMP, "mdi:calendar-start"),
]


async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities):
    store = hass.data[DOMAIN][entry.entry_id]
    coord: DurlemCoordinator = store["coordinator"]
    entities = [
        DurlemSensor(coord, key, name, unit, device_class, icon)
        for key, name, unit, device_class, icon in SENSORS
    ]
    async_add_entities(entities, True)


class DurlemSensor(CoordinatorEntity[DurlemCoordinator], SensorEntity):
    def __init__(
        self,
        coordinator: DurlemCoordinator,
        key: str,
        name: str,
        unit: str | None,
        device_class: SensorDeviceClass | None,
        icon: str,
    ):
        super().__init__(coordinator)
        self._key = key
        self._attr_name = name
        self._attr_unique_id = f"durlem_{key}"
        self._attr_native_unit_of_measurement = unit
        self._attr_device_class = device_class
        self._icon = icon

    @property
    def icon(self) -> str | None:
        return self._icon

    @property
    def available(self) -> bool:
        return self.coordinator.data is not None

    @property
    def device_info(self) -> DeviceInfo:
        soft = (self.coordinator.data or {}).get("softener", {})
        serial = soft.get("serial_number") or "unknown"
        model = soft.get("model") or "Durlem"
        return DeviceInfo(
            identifiers={(DOMAIN, f"softener_{serial}")},
            name=f"Durlem {serial}",
            manufacturer="Durlem",
            model=model,
        )

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        soft = (self.coordinator.data or {}).get("softener", {})
        return {
            "hardness_units": soft.get("hardness_units"),
            "zipcode": soft.get("zipcode"),
            "city": soft.get("city"),
            "low_battery": soft.get("low_battery"),
            "leaking": soft.get("leaking"),
            "service": soft.get("service"),
            "model": soft.get("model"),
            "serial_number": soft.get("serial_number"),
        }

    @property
    def native_value(self):
        soft = (self.coordinator.data or {}).get("softener", {})
        val = soft.get(self._key)

        if self._attr_device_class == SensorDeviceClass.TIMESTAMP:
            if isinstance(val, str):
                try:
                    dt = datetime.fromisoformat(val)
                    if dt.tzinfo is None:
                        dt = dt.replace(tzinfo=timezone.utc)
                    return dt.astimezone(timezone.utc)
                except Exception:
                    return val
            return val

        return val
