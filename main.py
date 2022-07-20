from operator import imod
from ManadeData import Application
from InsertData import InsertData
from models import do_conection

app = Application()
def execute_df(url):
    """
    Generate dataframe
    """
    df = app.extract_data(url)
    return df

def execute_insert_data(df):
    """
    insert data
    """
    db = 'restcountries'
    engine = do_conection()
    InsertData(df, db, engine).insert_data()    

def execute_json(df):
    file_name = 'data.json'
    app.download_df_to_json(df, file_name)

def execute_operations(df):
    """"
    generate operations
    """
    operations = Application().operations(df['time'])    
    return operations

if __name__=='__main__':
    url = 'https://restcountries.com/v3.1/all'
    df = execute_df(url)
    execute_insert_data(df)
    execute_json(df)    
    print(execute_operations(df))
