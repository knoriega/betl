from importlib import import_module

import click

import betl.loaders
from betl import main
from betl.core import JobPackage
from betl.jobs import AVAILABLE_JOBS
from betl.extractors import factory as extractor_factory
from betl.loaders import factory as loader_factory

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
    for name, extractor_config in job_config["extract"].items():
        _extractor_config = extractor_config.copy()
        _type = _extractor_config.pop("type")  
        extractor = extractor_factory.build(_type, dataset_name=name, **_extractor_config)
        extractors.append(extractor)
        
    loaders = []
    for name, loader_config in job_config["load"].items():
        _loader_config = loader_config.copy()
        _type = _loader_config.pop("type")
        loader = loader_factory.build(_type, dataset_name=name, **_loader_config)
        loaders.append(loader)

    main(
        extractors,
        job_package.transformer,
        loaders
    )

if __name__ == "__main__":
    cli()
