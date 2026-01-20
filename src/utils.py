# src/utils.py
import numpy as np
import pandas as pd
from pathlib import Path

# rutas
DIR_DATA = Path("data")
DIR_OUT = Path("outputs")
DIR_MOD = Path("models")
DIR_RAW = Path(DIR_DATA / "raw")
DIR_PARQ = Path(DIR_OUT / "parquets")
DIR_LOG = Path(DIR_OUT / "logs")
DIR_IMG = Path(DIR_OUT / "images")

SEED = 42
MODO_TEST = False
LIMITE_TEST = 999

DIR_ARRAY = {
    "data": DIR_DATA,
    "outputs": DIR_OUT,
    "raw": DIR_RAW,
    "parquets": DIR_PARQ,
    "models": DIR_MOD,
    "logs": DIR_LOG,
    "images": DIR_IMG,
}

def obtener_modo_test() -> bool:
    """Devuelve el modo de prueba (True/False)."""
    return MODO_TEST

def obtener_limite_test() -> int:
    """Devuelve el límite de filas para el modo de prueba."""
    return LIMITE_TEST 

def obtener_seed() -> int:
    """Devuelve la semilla fija para experimentos reproducibles."""
    return SEED

def obtener_path(name: str) -> Path:
    """Devuelve la ruta asociada al nombre solicitado."""
    try:
        return DIR_ARRAY[name]
    except KeyError:
        raise ValueError(f"Ruta desconocida: {name!r}. Opciones válidas: {sorted(DIR_ARRAY)}") from None

def crear_carpetas():
    DIR_DATA.mkdir(parents=True, exist_ok=True)
    DIR_OUT.mkdir(parents=True, exist_ok=True)
    DIR_RAW.mkdir(parents=True, exist_ok=True)
    DIR_MOD.mkdir(parents=True, exist_ok=True)
    DIR_PARQ.mkdir(parents=True, exist_ok=True)
    DIR_LOG.mkdir(parents=True, exist_ok=True)
    DIR_MOD.mkdir(parents=True, exist_ok=True)
    DIR_IMG.mkdir(parents=True, exist_ok=True)
    print("[INFO] Creación de directorios OK")
