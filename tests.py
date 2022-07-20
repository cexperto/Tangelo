from unittest import TestCase
from ManadeData import Application
from InsertData import InsertData
from models import do_conection
from models import RestCountries
from sqlalchemy.sql import select
import pandas as pd

class TestManageData(TestCase):

    app = Application()    
    url = 'https://restcountries.com/v3.1/all'

    def test_extract_data(self):
        df = self.app.extract_data(self.url)
        self.assertIsInstance(df, pd.DataFrame)

    def test_insert_data(self):
        df = self.app.extract_data(self.url)
        db = 'restcountries'
        engine = do_conection()
        InsertData(df, db, engine).insert_data()
        query = select(RestCountries.name)
        result = do_conection().execute(query)        
        self.assertTrue(result)
        



