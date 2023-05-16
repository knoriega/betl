from typing import Protocol

from betl.core import DataStep, ObjectFactory

import pandas as pd
from attrs import define


class Extractor(Protocol):
    dataset_name: str

    def extract(self) -> DataStep:
        ...

@define
class CsvExtractor:
    dataset_name: str
    location: str

    def extract(self) -> pd.DataFrame:
        return pd.read_csv(self.location)

factory: ObjectFactory[Extractor] = ObjectFactory()
factory.register_builder(CsvExtractor.__name__, CsvExtractor)

def build(dataset_name: str, config: dict) -> Extractor:
    """Convenient way to build extractor from config"""
    _config = config.copy()
    _type = _config.pop("type")
    return factory.build(_type, dataset_name=dataset_name, **_config)

