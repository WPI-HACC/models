# Models

Code, experiments and design of models for HACC.

After pulling in the repo, download a zip of the data and
decompress it into the data folder.


## Testing

From `./models/` run:

```{bash}
python -m unittest discover -s "test" -p "*_test.py"
```

## Folder Structure

### /data

Contains all the data used by the models.

### /data/dictionaries

Dictionaries used for CNTK CTF data file formats. Each source should generally have the following format:

```{bash}
/data/[source]/raw/...
/data/[source]/aggregated/...
/data/[source]/ctf/...
```

The `raw` folder contains the dataset in its original format. The `aggregated` dataset contains the parsed and coalsed data set, still in a raw form for future processing. The `ctf` format will have the dataset files in .ctf format.

### /utils

Has utility functions used for parsing different data formats and folders.

### /tests

Yup!

### /notebooks

Dump of the original notebooks, being cleaned up.
