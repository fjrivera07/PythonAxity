import random
import time


def retry(retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ultimo_error = None

            for intento in range(1, retries + 1):
                try:
                    print(f"Intento {intento}")
                    return func(*args, **kwargs)

                except Exception as error:
                    ultimo_error = error

                    print(f"Error: {error}")

                    if intento < retries:
                        espera = delay * intento

                        print(f"Esperando {espera} segundos")

                        time.sleep(espera)

            raise ultimo_error

        return wrapper

    return decorator


@retry(retries=3, delay=2)
def consumir_api():
    if random.random() < 0.7:
        raise ConnectionError("API no disponible")

    return "OK"


print(consumir_api())
