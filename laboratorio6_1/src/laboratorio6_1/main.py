from typing import Literal, Protocol, TypedDict


def int_or_float(valor: int | float) -> None:
    print(valor)


def estado(valor: Literal["activo", "inactivo"]) -> None:
    print(valor)


class UserDictionary(TypedDict):
    nombre: str
    edad: int


class Logger(Protocol):
    def log(self, message: str) -> None: ...


class ConsoleLogger:
    def log(self, message: str):
        print(message)


def procesar(logger: Logger) -> None:
    logger.log("Procesando...")


int_or_float(1)
int_or_float(135.5)
estado("activo")

usuarios: list[UserDictionary] = [
    {"nombre": "Francisco", "edad": 56},
    {"nombre": "Frida", "edad": 32},
]
print(usuarios)

logger = ConsoleLogger()

procesar(logger)
