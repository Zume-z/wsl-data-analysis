
import pandas as pd
from src.data_clean import drop_values, drop_by_string, drop_surfer_values, split_surfer_count, convert_boolean_int, convert_date, add_comp_hc, add_frontside

def test_drop_values():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
    columns_to_drop = ['A', 'B']
    result_df = drop_values(df, columns_to_drop)
    assert 'A' not in result_df.columns and 'B' not in result_df.columns
    assert 'C' in result_df.columns

def test_drop_by_string():
    df = pd.DataFrame({'Col': ['keep', 'drop_this', 'keep_this', 'drop']})
    string_to_drop = 'drop'
    result_df = drop_by_string(df, 'Col', string_to_drop)
    assert len(result_df) == 2
    assert 'drop_this' not in result_df['Col'].values
    assert 'drop' not in result_df['Col'].values

def test_drop_surfer_values():
    df = pd.DataFrame({
        'comp1_surf': [1, 2],
        'comp1_not_surf': [3, 4],
        'comp2_surf': [5, 6],
        'comp2_not_surf': [7, 8]
    })
    comp_prefix = ['comp1_', 'comp2_']
    drop_surfer = ['surf']
    result_df = drop_surfer_values(df, drop_surfer, comp_prefix)
    assert 'comp1_surf' not in result_df.columns and 'comp2_surf' not in result_df.columns
    assert 'comp1_not_surf' in result_df.columns and 'comp2_not_surf' in result_df.columns

def test_split_surfer_count():
    df = pd.DataFrame({'surfer_count': ['1', '2', '1']})
    result_df = split_surfer_count(df)
    assert 'surfer_count' not in result_df.columns
    assert 'surfer_count_1' in result_df.columns and 'surfer_count_2' in result_df.columns
    assert (result_df['surfer_count_1'] == [1, 0, 1]).all()


def test_convert_boolean_int():
    df = pd.DataFrame({
        'win': [True, False, True]
    })

    df_transformed = convert_boolean_int(df, 'win')
    expected_df = pd.DataFrame({
        'win': [1, 0, 1]
    })
    
    pd.testing.assert_frame_equal(df_transformed, expected_df)

def test_convert_date():
    df = pd.DataFrame({
        'event_s_date': ['2022-01-15', '2022-02-20']
    })
    
    df_transformed = convert_date(df)
    expected_df = pd.DataFrame({
        'event_s_date': pd.to_datetime(['2022-01-15', '2022-02-20']),
        'month': [1, 2]
    })
    
    pd.testing.assert_frame_equal(df_transformed, expected_df)

def test_add_comp_hc():
    df = pd.DataFrame({
        'event_country': ['USA', 'BRA'],
        'surfer_country': ['USA', 'AUS'],
        'op1_country': ['USA', 'BRA'],
        'op2_country': ['BRA', 'AUS']
    })
    
    df_transformed = add_comp_hc(df)
    expected_df = pd.DataFrame({
        'event_country': ['USA', 'BRA'],
        'surfer_country': ['USA', 'AUS'],
        'op1_country': ['USA', 'BRA'],
        'op2_country': ['BRA', 'AUS'],
        'surfer_comp_hc': [1, 0],
        'op1_comp_hc': [1, 1],
        'op2_comp_hc': [0, 0]
    })
    
    pd.testing.assert_frame_equal(df_transformed, expected_df)


def test_add_frontside():
    df = pd.DataFrame({
        'wave_dir': ['RIGHT', 'LEFT'],
        'surfer_stance': ['REGULAR', 'GOOFY'],
        'op1_stance': ['GOOFY', 'REGULAR'],
        'op2_stance': ['REGULAR', 'GOOFY']
    })
    
    df_transformed = add_frontside(df)
    expected_df = pd.DataFrame({
        'wave_dir': ['RIGHT', 'LEFT'],
        'surfer_stance': ['REGULAR', 'GOOFY'],
        'op1_stance': ['GOOFY', 'REGULAR'],
        'op2_stance': ['REGULAR', 'GOOFY'],
        'surfer_frontside': [1, 1],
        'op1_frontside': [0, 0],
        'op2_frontside': [1, 1]
    })
    
    pd.testing.assert_frame_equal(df_transformed, expected_df)



