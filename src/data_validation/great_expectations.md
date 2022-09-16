# Great Expectations 

[Great expectations](https://greatexpectations.io/) is a tool for data validations.

## Installation

Great expectations requires python3.

To install, use the following command:

```
pip install great_expectations
```

, and then validate whether it is installed by:

```
great_expectations --version
```

## Great Expectations folder structure

Great expectations requires a project configuration to store the results.

If you run it locally, you can set it up interactively using:

```
great_expectations init
```

In [data_sanity_check](./data_sanity_check/), the project configuration is set
up using python scripts, however, we still need the folders to be created 
beforehand.

The folders may look like this:

```
great_expectations
    |-- great_expectations.yml
    |-- expectations
    |-- checkpoints
    |-- plugins
    |-- .gitignore
    |-- uncommitted
        |-- config_variables.yml
        |-- data_docs
        |-- validations
```