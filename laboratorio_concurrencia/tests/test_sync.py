from laboratorio_concurrencia.sync_fetcher import run_sync


def test_run_sync():
    result = run_sync()

    assert isinstance(result, list)
    assert all(code == 200 for code in result)
