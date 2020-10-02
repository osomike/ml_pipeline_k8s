import pandas as pd
import numpy as np
from load_data_lib import load_json_file

if __name__ == "__main__":

    data = load_json_file(json_path='./data.json')

    print(data)

    return data