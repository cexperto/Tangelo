class InsertData:
    """
    Class for insert data
    receive as params:
    df: data frame
    table: name's table
    engine: engine of conection from sqlite3
    """
    def __init__(self, df, table, engine):
        self.df = df
        self.table = table
        self.engine = engine
    
    def insert_data(self):
        self.df.to_sql(self.table, con=self.engine, if_exists="append")
