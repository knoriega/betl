from betl.core import Transformer
from betl.extractor import Extractor
from betl.loaders import Loader


def main(
     extractors: list[Extractor],
     transformer: Transformer,
     loaders: list[Loader]
 ) -> None:
     datasets = {
         extractor.dataset_name: extractor.extract()
         for extractor in extractors
     }
     processed_data = transformer(**datasets)
     for loader in loaders:
         loader.load(processed_data)

