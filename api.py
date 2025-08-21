# custom_components/durlem/api.py
from __future__ import annotations

import time
import requests
from requests import HTTPError

from .const import API_BASE


class DurlemClient:
    def __init__(self, email: str, password: str, locale: str = "en") -> None:
        self.email = email
        self.password = password
        self.locale = locale

        self._token: str | None = None
        self._token_exp: float = 0.0 
        self._timeout = 15  

        self._session = requests.Session()
        self._session.headers.update({"X-LOCALE": self.locale})

    def _login(self) -> str:
        """Authenticate and cache token."""
        r = self._session.post(
            f"{API_BASE}/sessions",
            data={"email": self.email, "password": self.password},
            timeout=self._timeout,
        )
        try:
            r.raise_for_status()
        except HTTPError as e:
            raise RuntimeError(f"Login HTTP {r.status_code}: {r.text[:200]}") from e

        j = r.json()
        token = j.get("token")
        if not token:
            raise RuntimeError(f"Login OK mais pas de 'token' dans la réponse: {j}")

        self._token = token
        self._token_exp = time.time() + 20 * 60
        return token

    def _get_token(self) -> str:
        """Return a valid token, logging in again if needed."""
        if self._token and time.time() < self._token_exp:
            return self._token
        return self._login()

    def fetch_user_show(self) -> dict:
        """GET /users/show with valid token (retry once on 401)."""
        token = self._get_token()
        r = self._session.get(
            f"{API_BASE}/users/show",
            headers={"X-TOKEN": token},
            timeout=self._timeout,
        )
        if r.status_code == 401:
            token = self._login()
            r = self._session.get(
                f"{API_BASE}/users/show",
                headers={"X-TOKEN": token},
                timeout=self._timeout,
            )
        r.raise_for_status()
        return r.json()
