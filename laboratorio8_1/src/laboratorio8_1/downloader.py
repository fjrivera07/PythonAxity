from pathlib import Path

import httpx


def download_file(url: str, output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    with httpx.stream("GET", url, timeout=10.0) as response:
        response.raise_for_status()
        with output.open("wb") as file:
            for chunk in response.iter_bytes():
                file.write(chunk)
