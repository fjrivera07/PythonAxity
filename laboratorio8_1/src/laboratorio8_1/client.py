import httpx


class HttpClient:

    def __init__(self):
        self.client = httpx.Client(timeout=5.0, http2=True)

    def get(self, url: str):
        response = self.client.get(url)
        response.raise_for_status()
        return response
