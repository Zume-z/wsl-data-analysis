import pandas as pd
import numpy as np
from data_clean import drop_values, custom_sort_key, save_to_csv
from utils.col_data import categorical_cols, ath_comp_cols, related_numeric_cols
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler

# Function to import data
def import_data(file_path):
    df = pd.read_csv(file_path)
    return df

def data_split(df):
    X = df.drop('surfer_won', axis=1)
    y = df['surfer_won']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test

def impute_age(X_train, X_test, age_cols):
    X_train_male = X_train[X_train['tour_gender'] == 'MALE']
    X_train_female = X_train[X_train['tour_gender'] == 'FEMALE']

    median_age_male = pd.concat([
    X_train_male['surfer_age'].dropna(), 
    X_train_male['op1_age'].dropna(), 
    X_train_male['op2_age'].dropna()
    ]).median()

    median_age_female = pd.concat([
    X_train_female['surfer_age'].dropna(), 
    X_train_female['op1_age'].dropna(), 
    X_train_female['op2_age'].dropna()
    ]).median()

    for col in age_cols:
        X_train.loc[X_train['tour_gender'] == 'MALE', col] = X_train.loc[X_train['tour_gender'] == 'MALE', col].fillna(median_age_male)
        X_test.loc[X_test['tour_gender'] == 'MALE', col] = X_test.loc[X_test['tour_gender'] == 'MALE', col].fillna(median_age_male)
        X_train.loc[X_train['tour_gender'] == 'FEMALE', col] = X_train.loc[X_train['tour_gender'] == 'FEMALE', col].fillna(median_age_female)
        X_test.loc[X_test['tour_gender'] == 'FEMALE', col] = X_test.loc[X_test['tour_gender'] == 'FEMALE', col].fillna(median_age_female)

    return X_train, X_test

def scale_numeric(X_train, X_test, numeric_cols):
    scaler = StandardScaler()
    X_train_scaled = X_train.copy()
    X_test_scaled = X_test.copy()
    X_train_scaled[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
    X_test_scaled[numeric_cols] = scaler.transform(X_test[numeric_cols])
    return X_train_scaled, X_test_scaled

def scale_related_numeric(X_train, X_test, related_cols):
    for columns in related_cols:
        scaler = MinMaxScaler(feature_range=(0, 1))
        X_train_stacked = X_train[columns].apply(pd.to_numeric, errors='coerce').values
        X_train_valid_mask = ~np.isnan(X_train_stacked).any(axis=1)
        X_train_stacked_non_nan = X_train_stacked[X_train_valid_mask]
        scaler.fit(X_train_stacked_non_nan)
        
        X_train_scaled = scaler.transform(X_train[columns].apply(pd.to_numeric, errors='coerce').values)
        X_train[columns] = X_train_scaled
        
        X_test_stacked = X_test[columns].apply(pd.to_numeric, errors='coerce').values
        X_test_scaled = scaler.transform(X_test_stacked)
        X_test[columns] = X_test_scaled
    
    return X_train, X_test

def one_hot_encode(X_train, X_test, columns):
    encoder = OneHotEncoder(handle_unknown='ignore')
   
    X_train_temp = X_train.drop(categorical_cols, axis=1)
    X_test_temp =  X_test.drop(categorical_cols, axis=1)

    # Fit the encoder on the training data
    encoder.fit(X_train[categorical_cols])

    # Transform both training and test sets
    X_train_encoded = encoder.transform(X_train[categorical_cols])
    X_test_encoded = encoder.transform(X_test[categorical_cols])

    # Convert the output to a DataFrame, with column names
    columns = encoder.get_feature_names_out(categorical_cols)
    X_train_encoded = pd.DataFrame(X_train_encoded.toarray(), columns=columns)
    X_test_encoded = pd.DataFrame(X_test_encoded.toarray(), columns=columns)

    # Reindex the test DataFrame to ensure it has the same columns as the training DataFrame
    X_test_encoded = X_test_encoded.reindex(columns=X_train_encoded.columns, fill_value=0)
    X_train_temp.reset_index(drop=True, inplace=True)
    X_train_encoded.reset_index(drop=True, inplace=True)
    X_train_combined = pd.concat([X_train_temp, X_train_encoded], axis=1)
    X_test_temp.reset_index(drop=True, inplace=True)
    X_test_encoded.reset_index(drop=True, inplace=True)
    X_test_combined = pd.concat([X_test_temp, X_test_encoded], axis=1)
    return X_train_combined, X_test_combined

def null_val_indicator(df, columns):
    for col in columns:
        df[col+'_nan'] = df[col].isnull().astype(int)
    return df

def set_null_neg(df, columns):
    for col in columns:
        df.loc[df[col].isnull(), col] = -1
    return df

def set_null_zero(df, columns):
    for col in columns:
        df.loc[df[col].isnull(), col] = 0
    return df

def surfer_null_val_indicator(df, columns):
    for col in columns:
        df['surfer_'+col+'_nan'] = df['surfer_'+col].isnull().astype(int)
        df['op1_'+col+'_nan'] = df['op1_'+col].isnull().astype(int)
        df['op2_'+col+'_nan'] = df['op2_'+col].isnull().astype(int)
    return df

def surfer_set_null_neg(df, columns):
    for col in columns:
        df.loc[df['surfer_'+col].isnull(), 'surfer_'+col] = -1
        df.loc[df['op1_'+col].isnull(), 'op1_'+col] = -1
        df.loc[df['op2_'+col].isnull(), 'op2_'+col] = -1
    return df

def surfer_set_null_zero(df, columns):
    for col in columns:
        df.loc[df['surfer_'+col].isnull(), 'surfer_'+col] = 0
        df.loc[df['op1_'+col].isnull(), 'op1_'+col] = 0
        df.loc[df['op2_'+col].isnull(), 'op2_'+col] = 0
    return df

def null_third_surfer(df):
    op2_cols = [col for col in df.columns if col.startswith('op2')]
    df.loc[df['surfer_count_2'] == 1, op2_cols] = -1
    return df
    
def type_conversion(df):
    df.loc[df['op2_replace'] == -1, ['op2_replace']] = False
    df['op2_replace'] = df['op2_replace'].astype(int)
    return df
    

def process_data(file_path):
    df = import_data(file_path)
    
    X_train, X_test, y_train, y_test = data_split(df)
    X_train, X_test = impute_age(X_train, X_test, ['surfer_age', 'op1_age', 'op2_age'])
    X_train, X_test = scale_numeric(X_train, X_test, ['heat_round_number', 'heat_number', 'event_year', 'event_round', 'tour_year', 'surfer_matchup_count'])
    X_train, X_test = scale_related_numeric(X_train.copy(), X_test.copy(), related_numeric_cols)
    X_train, X_test = one_hot_encode(X_train, X_test, categorical_cols)
    X_train = drop_values(X_train, ['op2_stance_nan', 'op2_gender_nan', 'op2_country_nan'])
    X_test = drop_values(X_test, ['op2_stance_nan', 'op2_gender_nan', 'op2_country_nan'])
    X_train = null_val_indicator(X_train, ['surfer_win_rate', 'op1_win_rate', 'op2_win_rate', 'surfer_avg_ht', 'op1_avg_ht', 'op2_avg_ht'])
    X_test = null_val_indicator(X_test, ['surfer_win_rate', 'op1_win_rate', 'op2_win_rate', 'surfer_avg_ht', 'op1_avg_ht', 'op2_avg_ht'])
    X_train = set_null_neg(X_train, ['surfer_win_rate', 'op1_win_rate', 'op2_win_rate', 'surfer_avg_ht', 'op1_avg_ht', 'op2_avg_ht'])
    X_test = set_null_neg(X_test, ['surfer_win_rate', 'op1_win_rate', 'op2_win_rate', 'surfer_avg_ht', 'op1_avg_ht', 'op2_avg_ht'])
    X_train = set_null_zero(X_train, ['surfer_matchup_count', 'surfer_matchup_wins'])
    X_test = set_null_zero(X_test, ['surfer_matchup_count', 'surfer_matchup_wins'])
    X_train = surfer_null_val_indicator(X_train, ath_comp_cols)
    X_test = surfer_null_val_indicator(X_test, ath_comp_cols)
    X_train = surfer_set_null_neg(X_train, ath_comp_cols)
    X_test = surfer_set_null_neg(X_test, ath_comp_cols)
    X_train = surfer_set_null_zero(X_train, ['points', 'event_count', 'heat_count', 'heat_wins', 'heat_losses'])
    X_test = surfer_set_null_zero(X_test, ['points', 'event_count', 'heat_count', 'heat_wins', 'heat_losses'])
    X_train = null_third_surfer(X_train)
    X_test = null_third_surfer(X_test)
    X_train = type_conversion(X_train)
    X_test = type_conversion(X_test)

    X_train = X_train[sorted(X_train.columns, key=custom_sort_key)]
    X_test = X_test[sorted(X_test.columns, key=custom_sort_key)]

    save_to_csv(X_train, '../data/splits/X_train.csv')
    save_to_csv(X_test, '../data/splits/X_test.csv')
    save_to_csv(y_train, '../data/splits/y_train.csv')
    save_to_csv(y_test, '../data/splits/y_test.csv')

if __name__ == "__main__":
    input_file_path = '../data/cleaned/clean_2012_2024.csv'
    process_data(input_file_path)






