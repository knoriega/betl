from importlib import import_module

import click

import betl.extractor
import betl.loaders
from betl import main
from betl.core import JobPackage
from betl.jobs import AVAILABLE_JOBS

@click.command()
@click.option(
    "-j", 
    "--job", 
    help="Name of job", 
    type=click.Choice(AVAILABLE_JOBS)
)
def cli(job: str) -> None:
    job_package: JobPackage = import_module(f"betl.jobs.{job}") # type: ignore
    job_config = job_package.config
    
    extractors = []
    for dataset_name, extractor_config in job_config["extract"].items():
        _extractor_config = extractor_config.copy()
        _type = _extractor_config.pop("type")  
        extractor = getattr(betl.extractor, _type)(dataset_name=dataset_name, **_extractor_config)
        extractors.append(extractor)
        
    loaders = []
    for _, loader_config in job_config["load"].items():
        _loader_config = loader_config.copy()
        _type = _loader_config.pop("type")
        loader = getattr(betl.loaders, _type)(**_loader_config)
        loaders.append(loader)

    main(
        extractors,
        job_package.transformer,
        loaders
    )

if __name__ == "__main__":
    cli()
