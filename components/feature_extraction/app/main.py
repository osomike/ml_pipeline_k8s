import sys
import json
import pandas as pd
import numpy as np
from feature_engineering_lib import rename_fields

if __name__ == '__main__':

    script_args = sys.argv[1:]

    input_d = json.loads(script_args[0].replace('\'', '"'))

    data = rename_fields(input_dict=input_d)

    print(data)
