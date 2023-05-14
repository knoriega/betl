from pathlib import Path
from typing import Iterable, Callable, TypedDict, Protocol

import pandas as pd

DataStep = Path | Iterable[Path] | pd.DataFrame | Iterable[pd.DataFrame]

Transformer = Callable[..., dict[str, DataStep]]

class JobConfig(TypedDict):
    extract: dict
    load: dict

class JobPackage(Protocol):
    config: JobConfig
    transformer: Transformer
