from importlib import import_module

import click

from betl import main
from betl.core import JobPackage
from betl.jobs import AVAILABLE_JOBS
import betl.extractors
import betl.loaders

@click.command()
@click.option(
    "-j", 
    "--job_name", 
    help="Name of job", 
    type=click.Choice(AVAILABLE_JOBS)
)
def cli(job_name: str) -> None:
    job: JobPackage = import_module(f"betl.jobs.{job_name}") # type: ignore
    extractors = [
        betl.extractors.build(name, config) 
        for name, config in job.config["extract"].items()
    ]
    loaders = [
        betl.loaders.build(name, config) 
        for name, config in job.config["load"].items()
    ]        

    main(extractors, job.transformer, loaders)

if __name__ == "__main__":
    cli()

