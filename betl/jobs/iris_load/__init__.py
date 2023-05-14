from pathlib import Path
from yaml import safe_load

from betl.core import JobConfig
from .transfomer import iris_melter as transformer

config: JobConfig = safe_load((Path(__file__).parent / "config.yml").read_text())
