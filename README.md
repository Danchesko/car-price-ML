# Car Price Prediction

Project for predicting car prices via machine learning algorithms.

### Prerequisites

To be able to work with server or api. Install requirements from root directory as follows:
```
pip install -r requirements/api_requirements.txt
```

To be able to update parameters of model and update data:
```
pip install -r requirements/param_update_requirements.txt
```

If you want to scrape new data or add new data:
```
pip install -r requirements/scrape_new_data_requirements.txt
```

If you want to see the process of analyzing data in jupyter notebooks:
```
pip install -r requirements/notebook_requirements.txt
```

If you want to use everything, or don't want to care about installing requirements for different parts of the project, use command as follows:
```
pip install -r all_requirements.txt
```

Also, if you'd like to use conda environments, you can create conda environment with environment.yml as follows:
```
conda env create -f environment.yml
```

Since there is no one strict entry point, and you can use different parts, for different purposes, set PYTHONPATH to the project root, so import system can use absolute paths to import the project packages.

Linux/MacOS:
```
export PYTHONPATH $PROJ_ROOT
```

Windows:
```
set PYTHONPATH %PROJ_ROOT%
```

## Authors

### Daniiar Berdikulov

## Acknowledgments

* [Esen Dzhailobaev](https://github.com/s7b5en) - thanks for front-end advices
* [Andrei Khegai](https://github.com/akhegai) - thanks for helping me with docker
