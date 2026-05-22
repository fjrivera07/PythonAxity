import pytest

from laboratorio_concurrencia.async_fetcher import run_async


@pytest.mark.asyncio
async def test_run_async():
    result = await run_async()

    assert isinstance(result, list)
    assert all(code == 200 for code in result)
