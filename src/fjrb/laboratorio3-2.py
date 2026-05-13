import time


class Timer:
    def __enter__(self):
        self.inicio = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        fin = time.time()
        print(f"Tiempo transcurrido: {fin - self.inicio:.2f} segundos")


with Timer():
    time.sleep(2)
