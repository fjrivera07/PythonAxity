import httpx

from laboratorio_concurrencia.urls import URLS


def fetch_url(url: str) -> int:
    response = httpx.get(url)
    return response.status_code


def run_sync() -> list[int]:
    return [fetch_url(url) for url in URLS]
