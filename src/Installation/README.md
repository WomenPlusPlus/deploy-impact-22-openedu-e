# Installation Instructions


This repo uses Python 3.8 and various NLP-related libraries that can be installed:

1. Using [mamba](https://github.com/mamba-org/mamba) in [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) based on the provided `unifire.yml` environment files,
   - If you run into issues with the OS-specific files, please use the agnostic `installation/unifire-base.yml` file instead.
   - Run:
   - ```bash
     conda create -n unifire python=3.8
     mamba env update -n unifire -f unifire-base.yml
     conda activate unifire
     ```
2. For macOS and Linux only: via [pip](https://pip.pypa.io/en/stable/) in a Python virtual environment created with, e.g., [pyenv](https://github.com/pyenv/pyenv) or [venv](https://docs.python.org/3/tutorial/venv.html) using the provided `unifire.txt` requirement files.
3. Deprecated: using [Docker](https://www.docker.com/) Desktop to pull an image from [Docker Hub](https://www.docker.com/products/docker-hub) and create a local container with the requisite software to run the notebooks. 


* You could also just install the packages required for the notebooks you are interested in.


### Create a conda environment from an environment file


```bash
conda env create -f installation/unifire-base.yml
```


## Installing the libraries using pip

Some of the libraries require previous installation of OS-specific software, which may depend on the state of your machine.

[Pycaret](https://pypi.org/project/pycaret/)

```bash
pip install pycaret
pip install pycaret[full]
```
[Shapash](https://pypi.org/project/shapash/)

```bash
pip install shapash
```

