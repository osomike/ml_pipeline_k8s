import pandas as np
import numpy as np

def rename_fields(input_dict):
    new_dict = {}
    for k, v in input_dict.items():
        new_dict.update({k.replace('raw_', '') : v})

    return new_dict
