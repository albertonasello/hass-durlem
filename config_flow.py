from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries

DOMAIN = "durlem" 

class DurlemConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Durlem", data=user_input)

        schema = vol.Schema({
            vol.Required("email"): str,
            vol.Required("password"): str,
        })
        return self.async_show_form(step_id="user", data_schema=schema)
