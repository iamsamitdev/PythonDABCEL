import pandas as pd
import sys

# If you are not able to import constant py file use below code
sys.path.insert(1, 'ETLWithPandas\metadata')

from constant import connection

def extract(type, source):

    # Read data from mariadb
    if type == 'db':
        output_df = pd.read_sql(f'SELECT * FROM {source}', con=connection())

    # Read data from csv
    if type == 'csv':
        output_df = pd.read_csv(source)

    return output_df

# print(extract('db', 'country'))
# print(extract('csv', 'ETLWithPandas\data\countrylanguage.csv'))