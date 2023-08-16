from pandas import DataFrame

# Rename all the columns in the dataframe
def rename_cols(df: DataFrame, mapping_dict: dict) -> DataFrame:
    df.rename(columns=mapping_dict, inplace=True)
    print(df.dtypes)
    print("--------------")
    return df

# get specific columns from the dataframe
def specific_cols(df: DataFrame, specific_cols: list):
    return df[specific_cols]

# Join two dataframes
def join_df(left_df: DataFrame, right_df: DataFrame, ON_COLUMNS: list, JOIN_TYPE: str) -> DataFrame:

    output_df = left_df.merge(right_df, on=ON_COLUMNS, how=JOIN_TYPE)

    return output_df