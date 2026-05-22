from concurrent.futures import ProcessPoolExecutor


def calculate(n: int) -> int:

    total = 0

    for i in range(n):
        total += i * i

    return total


def run_cpu() -> list[int]:

    values = [10_000_000] * 4

    with ProcessPoolExecutor() as executor:
        return list(executor.map(calculate, values))
