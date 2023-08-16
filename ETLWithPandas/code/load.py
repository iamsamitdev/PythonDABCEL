from pandas import DataFrame
import sys

# If you are not able to import constant py file use below code
sys.path.insert(1, 'ETLWithPandas\metadata')

from constant import connection

# Load the data based on type
def load(type: str, df: DataFrame, target: str):
    try:
        if type == 'db':
            df.to_sql(target, con=connection(),
                      if_exists='replace', index=False)
            print(f"Data succesfully loaded to MySQL Database !!")

        if type == 'csv':
            df.to_csv(target, index=False)
            print('Data succesfully loaded to csv')
    except FileExistsError as e:
        print(e)