import pandas as pd

# Function to import data
def import_data(file_path):
    df = pd.read_csv(file_path, dtype={5: str, 7: str, 9: str})
    return df

# Function to drop certain columns
def drop_values(df, columns_to_drop):
    df = df.drop(columns=columns_to_drop, axis=1)
    return df

def drop_by_string(df, column_name, string):
    mask = df[column_name].str.contains(string)
    df = df[~mask]
    return df

# Drop Surfer Values
def drop_surfer_values(df, drop_surfer, comp_prefix):
  for prefix in comp_prefix:
      for col in drop_surfer:
          df = df.drop(prefix + col, axis=1)
  return df

# Split surfer count into two cols
def split_surfer_count(df):
    df['surfer_count'] = df['surfer_count'].astype(str)
    dummies = pd.get_dummies(df['surfer_count'], prefix='surfer_count')    
    df = df.join(dummies)
    df = df.drop('surfer_count', axis=1)
    return df

# Convert surfer won from boolean to int
def convert_boolean_int(df, column_name):
    df[column_name] = df[column_name].astype(int)
    return df

def convert_date(df):    
    df['event_s_date'] = pd.to_datetime(df['event_s_date'])
    df['month'] = df['event_s_date'].apply(lambda date: date.month)
    return df


# Add Surfer_comp_hc: Surfer is competing in home country
def add_comp_hc(df):
    df['surfer_comp_hc'] = (df['surfer_country'] == df['event_country']).astype(int)
    df['op1_comp_hc'] = (df['op1_country'] == df['event_country']).astype(int)
    df['op2_comp_hc'] = (df['op2_country'] == df['event_country']).astype(int)
    return df


def add_frontside(df):
    df['surfer_frontside'] = (((df['surfer_stance'] == 'REGULAR') & (df['wave_dir'] == 'RIGHT')) | \
                            ((df['surfer_stance'] == 'GOOFY') & (df['wave_dir'] == 'LEFT'))).astype(int)
    df['op1_frontside'] = (((df['op1_stance'] == 'REGULAR') & (df['wave_dir'] == 'RIGHT')) | \
                            ((df['op1_stance'] == 'GOOFY') & (df['wave_dir'] == 'LEFT'))).astype(int)

    df['op2_frontside'] = (((df['op2_stance'] == 'REGULAR') & (df['wave_dir'] == 'RIGHT')) | \
                            ((df['op2_stance'] == 'GOOFY') & (df['wave_dir'] == 'LEFT'))).astype(int)
    return df

def custom_sort_key(col):
    if col.startswith('surfer_'):
        return (1, col)
    elif col.startswith('op1_'):
        return (2, col)
    elif col.startswith('op2_'):
        return (3, col)
    else:
        return (0, col)

def save_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

def clean_data(file_path, output_file_path):
    df = import_data(file_path)
    comp_prefix = ['surfer_', 'op1_', 'op2_']
    print(df.info())

    df = drop_by_string(df, 'event_slug', 'surf-ranch')
    df = drop_values(df, ['heat_round', 'heat_slug', 'event_slug', 'surfer_heat_place'])
    df = drop_surfer_values(df, ['dob', 'heat_total', 'slug'], comp_prefix)
    df = split_surfer_count(df)
    df = convert_boolean_int(df, 'surfer_won')
    df = convert_date(df)
    df = add_comp_hc(df)
    df = add_frontside(df)

    # Temp drop
    df = drop_values(df, ['heat_duration', 'wave_range', 'heat_date', 'wind_conditions', 'avg_wave_height', 'event_s_date'])

    # Sort the columns
    df = df[sorted(df.columns, key=custom_sort_key)]
    print(df.info(verbose=True))

    # Save the cleaned data
    # save_to_csv(df, output_file_path)

if __name__ == "__main__":
    input_file_path = '../data/raw/raw_2012_2024.csv'
    output_file_path = '../data/cleaned/clean_2012_2024.csv'
    
    clean_data(input_file_path, output_file_path)