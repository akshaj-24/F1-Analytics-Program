Fast F1 library needs to be installed before running the program. 
Guide to install FastF1: Python 3.8 or higher

1. pip install fastf1
2. conda install -c conda-forge fastf1


Official documentation: https://docs.fastf1.dev/


After installation, to run please set the cache folder by running the command:

fastf1.Cache.enable_cache(CACHE_DIRECTORY_PATH)


All the data installed will be stored in the cache folder for faster accessibility.
To clear the cache folder run for storage purposes:

fastf1.Cache.clear_cache(CACHE_DIRECTORY_PATH)