from __future__ import annotations
from datetime import datetime
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import PERCENTAGE
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN
from .coordinator import DurlemCoordinator

SENSORS = [
    ("remaining_capacity", "Durlem Remaining Capacity", PERCENTAGE),
    ("low_salt", "Durlem Low Salt", None),
    ("working", "Durlem Working", None),
    ("last_regeneration_at", "Durlem Last Regeneration", None),
    ("next_regeneration_at", "Durlem Next Regeneration", None),
]

async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities):
    store = hass.data[DOMAIN][entry.entry_id]
    coord: DurlemCoordinator = store["coordinator"]
    entities = [DurlemSensor(coord, key, name, unit) for key, name, unit in SENSORS]
    async_add_entities(entities, True)

class DurlemSensor(CoordinatorEntity[DurlemCoordinator], SensorEntity):
    def __init__(self, coordinator: DurlemCoordinator, key: str, name: str, unit):
        super().__init__(coordinator)
        self._key = key
        self._attr_name = name
        self._attr_native_unit_of_measurement = unit
        self._attr_unique_id = f"durlem_{key}"

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
    def extra_state_attributes(self):
        soft = (self.coordinator.data or {}).get("softener", {})
        return {
            "hardness": soft.get("hardness"),
            "hardness_units": soft.get("hardness_units"),
            "leaking": soft.get("leaking"),
            "service": soft.get("service"),
            "low_battery": soft.get("low_battery"),
            "city": soft.get("city"),
            "zipcode": soft.get("zipcode"),
        }

    @property
    def native_value(self):
        data = (self.coordinator.data or {}).get("softener", {})
        val = data.get(self._key)
        if isinstance(val, str) and ("T" in val or "-" in val):
            try:
                return val
            except Exception:
                return val
        return val
