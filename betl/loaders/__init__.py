from pathlib import Path
from typing import Protocol

from attrs import define
from loguru import logger

import pandas as pd


class Loader(Protocol):
    def load(self, *args, **kwargs) -> None:
        ...

@define
class CsvLoader:
    location: str
    
    def load(self, processed_data: pd.DataFrame):
        _location = Path(self.location)
        _location.parent.mkdir(parents=True, exist_ok=True)
        processed_data.to_csv(self.location)        
        logger.info(f"Wrote data to {_location}")
