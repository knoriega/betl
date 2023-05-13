# betl

**B**etter **ETL**

An intial take on writing the skeleton of a small "Extract-Transform-Load" (ETL) application that is able to:

* Retrieve data from various locations using standard custom workflows
* Perform some amount of processing on that data
* Load the processed data to various locations using standard custom workflows

Our custom interfaces for defining the workflows of extraction, transforming, and loading data are:
* `Extractor`
* `Transformer`
* `Loader`

## Usage
Writing a new ETL job will require the following:

* A config file specifying what kind of extraction and loaded processes will be used
* A callabe function that will accept all the extracted datasources and return one or more datasets

We'll interact with our tooling using a simple command line interface (CLI)
```
betl -j <name-of-job>
```

### Configuration File:
The configuration file will define the kind of extraction process used and the names of the datasets at each step in the process


```yaml
extract:
    iris:
        type: CsvExtractor
        location: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

load:
    procssed_data:
        type: CsvLoader
        location: output/iris_melt.csv

```

The dataset names (e.g. "iris" and "processed_data" below) will be the argument names passed to the next step of an ETL job. 
So the related `Transformer` of this ETL job should be ready to accept `iris` as an argument. Similarily, the standard `CsvLoader` will be
ready to accept the `processed_data` argument.

## Data Intefaces
Data being passed between steps should one of the following:

* `Path`
* `Iterable[Path]`
* `pandas.DataFrame`
* `Iterable[pandas.DataFrame]`

This supports common ways of processing data either from files or loading data into memory immediately using `pandas`.
Using `Iterables` supports processing data in a pipeline where all extracted data does not need to be loaded into memory at once.
