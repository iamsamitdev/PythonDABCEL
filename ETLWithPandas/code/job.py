import pandas as pd
import sys

# If you are not able to import constant py file use below code
sys.path.insert(1, 'ETLWithPandas\metadata')

from constant import connection,JOIN_ON_COLUMNS,JOIN_TYPE,SPEC_COLS,CITY_COL_DICT,COUNTRY_COL_DICT,COUNTRY_LANGUAGE_COL_DICT

from extract import extract
from transform import rename_cols,specific_cols,join_df
from load import load

#################### Extract ####################
# Extract data from database
city_df = extract('db', 'city')
country_df = extract('db', 'country')

# Extract data from csv
country_language_df = extract('csv', 'ETLWithPandas\data\countrylanguage.csv')

# print("city_df",city_df.head())
# print("country_df",country_df.head())
# print("country_language_df",country_language_df.head())

#################### Transform ####################

# 1. Rename Columns
city_df = rename_cols(city_df, CITY_COL_DICT)
country_df = rename_cols(country_df, COUNTRY_COL_DICT)
country_language_df = rename_cols(country_language_df, COUNTRY_LANGUAGE_COL_DICT)

# 2. Join DF with common column "country_code"
country_city_df=join_df(country_df, city_df, JOIN_ON_COLUMNS, JOIN_TYPE)
country_city_language_df= join_df(country_city_df, country_language_df, JOIN_ON_COLUMNS, JOIN_TYPE)

# 3. Get specific cols
country_city_language_df = specific_cols(country_city_language_df, SPEC_COLS)

#################### Load Data ####################
# Load data to database
load('db', country_city_language_df,'countrycitylanguage')

# Load data to csv
load('csv', country_city_language_df,'ETLWithPandas/output/countrycitylanguage.csv')

