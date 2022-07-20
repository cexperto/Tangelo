from requests.exceptions import HTTPError
from time import time
import requests
import pandas as pd
import requests
import base64
import hashlib

class ManageDataToDF:
    def __init__(self, url):
        self.url =url

    def get_data_from_url(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'error http: {http_err}')
        except Exception as ex:
            print(f'error: {ex}')
        else:
            return response.json()

    def data_to_df(self, data):        
        init = time()        
        df = pd.DataFrame(data)
        df['d_init'] = init
        name = df['name'].apply(lambda x: x.get('official'))
        region = df['region']
        languages = df['languages'].astype(str).str.encode('UTF-8').apply(lambda x: base64.b64encode(hashlib.sha1(x).digest()))
        df['time']= time()-init        
        new_df = pd.concat([name, region, languages, df['time']], axis=1)
        return new_df
    

class Application:
    
    def extract_data(self, url):
        manage_data = ManageDataToDF(url)
        data_url = manage_data.get_data_from_url()
        df = manage_data.data_to_df(data_url)        
        return df

    def operations(self, col):
        total = col.sum()
        mean =  col.mean()
        max = col.max()
        min = col.min()
        return {
            'total':total,
            'mean': mean,
            'max': max,
            'min': min
        }
    
    def download_df_to_json(self, df, path):
        if isinstance(df, pd.DataFrame):
            return df.to_json(path)
        return False