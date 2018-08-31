import numpy as np
import os
from datetime import datetime, date

datetime_epoch = np.datetime64('1970-01-01T00:00:00Z')
datetime_second = np.timedelta64(1, 's')


# Create a folder at the given path, if overwrite, delete existing folder and create a new empty one
def create_folder(path, overwrite=False):
    if(os.path.isdir(path)):
        if(overwrite):
            shutil.rmtree(path)
        else:
            return
    os.mkdir(path)

def timestamp():
    return datetime_to_epoch(datetime.now())

def datetime64_to_epoch(dt64):
    return (dt64 - datetime_epoch) / datetime_second

def datetime_to_epoch(dt):
    return datetime64_to_epoch(np.datetime64(dt))