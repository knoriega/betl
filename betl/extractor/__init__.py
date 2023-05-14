from typing import Protocol

from betl.core import DataStep

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
