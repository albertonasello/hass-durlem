from __future__ import annotations
import time
import requests
from .const import API_BASE

class DurlemClient:
    def __init__(self, email: str, password: str, locale: str = "en"):
        self.email = email
        self.password = password
        self.locale = locale
        self._token: str | None = None
        self._token_exp: float = 0 
        self._session = requests.Session()
        self._session.headers.update({"X-LOCALE": self.locale})

    def _login(self) -> str:
        r = self._session.post(
            f"{API_BASE}/sessions",
            data={"email": self.email, "password": self.password},
            timeout=15,
        )
        r.raise_for_status()
        token = r.json().get("token")
        if not token:
            raise RuntimeError("Durlem login: no token returned")
        self._token = token
        self._token_exp = time.time() + 20 * 60
        return token

    def _get_token(self) -> str:
        if self._token and time.time() < self._token_exp:
            return self._token
        return self._login()

    def fetch_user_show(self) -> dict:
        token = self._get_token()
        r = self._session.get(
            f"{API_BASE}/users/show",
            headers={"X-TOKEN": token},
            timeout=15,
        )
        if r.status_code == 401:
            token = self._login()
            r = self._session.get(
                f"{API_BASE}/users/show",
                headers={"X-TOKEN": token},
                timeout=15,
            )
        r.raise_for_status()
        return r.json()
