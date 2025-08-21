from __future__ import annotations
from datetime import timedelta
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .api import DurlemClient
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL

class DurlemCoordinator(DataUpdateCoordinator[dict]):
    def __init__(self, hass: HomeAssistant, client: DurlemClient):
        super().__init__(
            hass,
            logger=hass.helpers.logger.logging.getLogger(DOMAIN),
            name="Durlem Coordinator",
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.client = client

    async def _async_update_data(self) -> dict:
        return await self.hass.async_add_executor_job(self._fetch)

    def _fetch(self) -> dict:
        try:
            data = self.client.fetch_user_show()
            return data
        except Exception as e:
            raise UpdateFailed(str(e)) from e
