from functools import lru_cache
import requests
import logging


class TokenClient:
    def __init__(self, username, password, apikey):
        self.token_endpoint = "https://api.platts.com/auth/api"
        self.endpoint = "https://api.platts.com"
        self.un = username
        self.pw = password
        self.apikey = apikey
        return

    def get(self, path, params):
        headers = {
            "appkey": self.apikey,
            "Authorization": f"Bearer {self.token}",
            "User-Agent": "platts-py-sdk",
        }

        r = requests.get(f"{self.endpoint}{path}", headers=headers, params=params)
        try:
            r.raise_for_status()
            return r.json()
        except Exception as err:
            if r.status_code >= 500:
                logging.error(err)
            else:
                logging.error(r.status_code, r.json())
            raise

    @property
    @lru_cache()
    def token(self):
        body = {"username": self.un, "password": self.pw}
        headers = {"appkey": self.apikey}

        try:
            r = requests.post(self.token_endpoint, data=body, headers=headers)
            r.raise_for_status()
            return r.json()["access_token"]
        except Exception as err:
            if r.status_code >= 500:
                logging.error(f"[{r.status_code}] - {err}")
            else:
                logging.error(f"[{r.status_code}] -  {r.json()}")
            raise
