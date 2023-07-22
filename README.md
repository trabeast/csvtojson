# csvtojson

Convert csv data to JSON formatted data and save it on JSON file.

## Installation

Install `conda`. See https://conda.io/projects/conda/en/latest/user-guide/install/index.html for more detail

## Usage

- `file` a `string` to the absolute path of the csv file.
- `main_key` a `string` of the column name in csv file that will be the key of the object.
- `exclude` a `string` or `list` of column names that will be excluded from the object properties.
- `dest` a `string` to the absolute path where the JSON file will be saved.