import time


def retry_request(
    func,
    retries=3,
):

    for intento in range(1, retries + 1):
        try:
            return func()
        except Exception as error:
            if intento == retries:
                raise error
            time.sleep(intento)
