import pandas as pd
import numpy as np
from src.data_preprocess import data_split, impute_age, null_val_indicator, set_null_neg, set_null_zero
from sklearn.model_selection import train_test_split


def create_test_df():
    
    return pd.DataFrame({
        'col1': [1, np.nan, 3],
        'col2': [4, 5, np.nan]
    })

def test_data_split():
    df = pd.DataFrame({
        'feature1': range(10),
        'feature2': range(10, 20),
        'surfer_won': [1, 0] * 5
    })
    X_train, X_test, y_train, y_test = data_split(df)
    
    assert len(X_train) == 7
    assert len(X_test) == 3
    assert len(y_train) == 7
    assert len(y_test) == 3
    
    assert 'surfer_won' not in X_train.columns
    assert 'surfer_won' not in X_test.columns

def test_impute_age():
    df = pd.DataFrame({
        'tour_gender': ['MALE', 'FEMALE', 'MALE', 'FEMALE'],
        'surfer_age': [25, np.nan, 27, np.nan],
        'op1_age': [np.nan, 24, np.nan, 22],
        'op2_age': [28, np.nan, 26, np.nan],
        'surfer_won': [1, 0, 1, 0],
    })
    age_cols = ['surfer_age', 'op1_age', 'op2_age']
    
    X_train, X_test, y_train, y_test = train_test_split(df.drop('surfer_won', axis=1), df['surfer_won'], test_size=0.25, random_state=42)
    
    X_train_imputed, X_test_imputed = impute_age(X_train, X_test, age_cols)

    for col in age_cols:
        assert X_train_imputed[col].isna().sum() == 0
        assert X_test_imputed[col].isna().sum() == 0



def test_null_val_indicator():
    df = create_test_df()
    df_test = null_val_indicator(df, ['col1', 'col2'])
    assert (df_test['col1_nan'] == [0, 1, 0]).all()
    assert (df_test['col2_nan'] == [0, 0, 1]).all()

def test_set_null_neg():
    df = create_test_df()
    df_test = set_null_neg(df, ['col1', 'col2'])
    assert (df_test['col1'] == [1, -1, 3]).all()
    assert (df_test['col2'] == [4, 5, -1]).all()


def test_set_null_zero():
    df = create_test_df()
    df_test = set_null_zero(df, ['col1', 'col2'])
    assert (df_test['col1'] == [1, 0, 3]).all()
    assert (df_test['col2'] == [4, 5, 0]).all()
