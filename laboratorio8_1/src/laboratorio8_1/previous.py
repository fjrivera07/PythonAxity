import time

import httpx


def get_with_retry(
    url: str,
    retries: int = 3,
):
    for intento in range(1, retries + 1):
        try:
            response = httpx.get(
                url,
                timeout=5.0,
            )
            response.raise_for_status()
            return response
        except Exception as error:
            print(f"Intento {intento} falló")
            if intento == retries:
                raise error
            time.sleep(intento)


response = get_with_retry("https://api.github.com", 3)
print(response.status_code)
print(response.json)

# import httpx

# try:
#     timeout = httpx.Timeout(connect=2.0, read=5.0, write=5.0, pool=5.0)
#     response = httpx.get("https://api.github.com", timeout=timeout)
#     print(response.status_code)
#     print(response.json)
# except httpx.TimeoutException:
#     print("Timeout")
# except httpx.HTTPStatusError as error:
#     print(f"Http error: {error}")
# except httpx.RequestError as error:
#     print(f"Request error: {error}")

# import requests
# response = requests.get("https://api.github.com")
# print(response)
