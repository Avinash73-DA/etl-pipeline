from collections import Counter

def make_column_names_unique(columns):
    counter = Counter()
    new_columns = []
    for col in columns:
        clean_col = col.lower().replace('.', '').replace(' ', '')
        counter[clean_col] += 1
        if counter[clean_col] > 1:
            clean_col = f"{clean_col}_{counter[clean_col] - 1}"
        new_columns.append(clean_col)
    return new_columns

def transform_custify_data(df):
    df.columns = make_column_names_unique(df.columns)
    df = df.astype(str)
    return df