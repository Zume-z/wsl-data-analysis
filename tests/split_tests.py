import pandas as pd
import numpy as np

def import_data(file_path):
    df = pd.read_csv(file_path)
    return df

# assert that columns are aligned
def aligned_columns(X_train, X_test):
    assert set(X_train.columns) == set(X_test.columns), "Columns in X_train and X_test are not aligned."

# assert that there are no null
def null_vals(df):
    for col in df.columns:
        assert df[col].isnull().sum() == 0, f"Column {col} has {df[col].isnull().sum()} null values"
        

def test_data(X_train_path, X_test_path, y_train_path, y_test_path):
  X_train = import_data(X_train_path)
  X_test = import_data(X_test_path)
  y_train = import_data(y_train_path)
  y_test = import_data(y_test_path)

  aligned_columns(X_train, X_test)
  null_vals(X_train)
  

if __name__ == "__main__":
    X_train_path = "../data/splits/X_train.csv"
    X_test_path = "../data/splits/X_test.csv"
    y_train_path = "../data/splits/y_train.csv"
    y_test_path = "../data/splits/y_test.csv"

    test_data(X_train_path, X_test_path, y_train_path, y_test_path)