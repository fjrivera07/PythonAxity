import asyncio
import time

from laboratorio_concurrencia.async_fetcher import run_async
from laboratorio_concurrencia.cpu_bound import run_cpu
from laboratorio_concurrencia.sync_fetcher import run_sync


def benchmark_sync():
    start = time.perf_counter()
    run_sync()
    end = time.perf_counter()

    print(f"Sync fetch: {end-start:.2f}s")


def benchmark_async():
    start = time.perf_counter()
    asyncio.run(run_async())
    end = time.perf_counter()

    print(f"Async fetch: {end-start:.2f}s")


def benchmark_cpu():
    start = time.perf_counter()
    run_cpu()
    end = time.perf_counter()

    print(f"CPU process pool: {end - start:.2f}s")


if __name__ == "__main__":
    benchmark_sync()
    benchmark_async()
    benchmark_cpu()
