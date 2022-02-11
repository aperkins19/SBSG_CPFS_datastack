import requests
from .config import *
import pandas as pd


def get_all_amplicons(BASE_URL=BASE):
    BASE_URL = BASE_URL + "/amplicons/"
    print('get all')
    response = requests.get(BASE_URL)

    df = pd.json_normalize(response.json())
    return df




def enter_new_amplicon(args, BASE_URL=BASE):
    BASE_URL = BASE_URL + "/amplicons/"

    print('enter new:')
    #print(args)

    response = requests.post(BASE_URL, args)
    print(response.json())
    return response.json()
