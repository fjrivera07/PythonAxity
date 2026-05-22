from laboratorio_concurrencia.cpu_bound import run_cpu


def test_run_cpu():
    result = run_cpu()

    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)
