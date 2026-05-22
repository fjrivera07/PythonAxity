import asyncio

import httpx

from laboratorio_concurrencia.urls import URLS


async def fetch_url(client: httpx.AsyncClient, url: str, semaphore: asyncio.Semaphore):
    async with semaphore:
        response = await client.get(url)
        return response.status_code


async def run_async() -> list[int]:
    semaphore = asyncio.Semaphore(3)
    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(client, url, semaphore) for url in URLS]
        return await asyncio.gather(*tasks)
