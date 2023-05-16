from pathlib import Path
from typing import Protocol

from attrs import define
from loguru import logger

import pandas as pd

from betl.core import ObjectFactory


class Loader(Protocol):
    dataset_name: str
    def load(self, *args, **kwargs) -> None:
        ...

@define
class CsvLoader:
    dataset_name: str
    location: str
    
    def load(self, data: pd.DataFrame, *args_ignored, **kwargs_ignored) -> None:
        _location = Path(self.location)
        _location.parent.mkdir(parents=True, exist_ok=True)
        data.to_csv(self.location)        
        logger.info(f"Wrote data to {_location}")

factory: ObjectFactory[Loader] = ObjectFactory()
factory.register_builder(CsvLoader.__name__, CsvLoader)

def build(dataset_name: str, config: dict) -> Loader:
    """Convenient way to build loader from config"""
    _config = config.copy()
    _type = _config.pop("type")
    return factory.build(_type, dataset_name=dataset_name, **_config)

