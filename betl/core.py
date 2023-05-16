from pathlib import Path
from typing import Generic, Iterable, Callable, TypeVar, TypedDict, Protocol
from attrs import define, Factory

import pandas as pd

DataStep = Path | Iterable[Path] | pd.DataFrame | Iterable[pd.DataFrame]

Transformer = Callable[..., dict[str, DataStep]]

class JobConfig(TypedDict):
    extract: dict
    load: dict

class JobPackage(Protocol):
    config: JobConfig
    transformer: Transformer

T = TypeVar("T")

@define
class ObjectFactory(Generic[T]):
    _builders: dict = Factory(dict)

    def register_builder(self, key: str, builder: Callable[..., T]) -> None:
        self._builders[key] = builder

    def build(self, key: str, **kwargs) -> T:
        builder = self._builders.get(key)
        if builder is None:
            raise ValueError(f"{key} not supported")
        return builder(**kwargs)
    
