
categorical_cols = ['wave_dir', 'break_slug', 'break_type', 'event_country', 'tour_gender', 
    'surfer_gender', 'surfer_country', 'surfer_stance',                 
    'op1_gender', 'op1_country', 'op1_stance',
    'op2_gender', 'op2_country', 'op2_stance'
]

related_numeric_cols = [
    ['surfer_age',  'op1_age', 'op2_age'], 
    ['surfer_points', 'op1_points', 'op2_points'],
    ['surfer_event_count', 'op1_event_count', 'op2_event_count'],
    ['surfer_heat_count', 'op1_heat_count', 'op2_heat_count'], 
    ['surfer_heat_wins', 'op1_heat_wins', 'op2_heat_wins'], 
    ['surfer_heat_losses', 'op1_heat_losses', 'op2_heat_losses'], 
    ['surfer_win_rate', 'op1_win_rate', 'op2_win_rate'], 
    ['surfer_avg_ht', 'op1_avg_ht', 'op2_avg_ht'], 
    ['surfer_heat_count_break',  'op1_heat_count_break', 'op2_heat_count_break'],
    ['surfer_heat_win_break',  'op1_heat_win_break', 'op2_heat_win_break'],
    ['surfer_avg_heat_total_break',  'op1_avg_heat_total_break', 'op2_avg_heat_total_break'],
    ['surfer_heat_count_event',  'op1_heat_count_event', 'op2_heat_count_event'],
    ['surfer_heat_win_event',  'op1_heat_win_event', 'op2_heat_win_event'],
    ['surfer_avg_heat_total_event',  'op1_avg_heat_total_event', 'op2_avg_heat_total_event'],
    ['surfer_heat_count_ws',  'op1_heat_count_ws', 'op2_heat_count_ws'],
    ['surfer_heat_win_ws',  'op1_heat_win_ws', 'op2_heat_win_ws'],
    ['surfer_avg_heat_total_ws',  'op1_avg_heat_total_ws', 'op2_avg_heat_total_ws'],
    ['surfer_heat_count_wd',  'op1_heat_count_wd', 'op2_heat_count_wd'],
    ['surfer_heat_win_wd',  'op1_heat_win_wd', 'op2_heat_win_wd'],
    ['surfer_avg_heat_total_wd',  'op1_avg_heat_total_wd', 'op2_avg_heat_total_wd'],
    ['surfer_heat_count_bt',  'op1_heat_count_bt', 'op2_heat_count_bt'],
    ['surfer_heat_win_bt',  'op1_heat_win_bt', 'op2_heat_win_bt'],
    ['surfer_avg_heat_total_bt',  'op1_avg_heat_total_bt', 'op2_avg_heat_total_bt'],
    ['surfer_prev_event_place',  'op1_prev_event_place', 'op2_prev_event_place'],
    ['surfer_prev_event_points',  'op1_prev_event_points', 'op2_prev_event_points'],
    ['surfer_prev_3_event_points',  'op1_prev_3_event_points', 'op2_prev_3_event_points'],
    ['surfer_prev_5_event_points',  'op1_prev_5_event_points', 'op2_prev_5_event_points'],
    ['surfer_prev_year_place',  'op1_prev_year_place', 'op2_prev_year_place'],
    ['surfer_prev_10_heat_place',  'op1_prev_10_heat_place', 'op2_prev_10_heat_place'],
    ['surfer_matchup_wins'],
]   

ath_comp_cols = [
    'heat_count_break', 'heat_win_break', 'avg_heat_total_break', 
    'heat_count_event', 'heat_win_event', 'avg_heat_total_event', 
    'heat_count_ws', 'heat_win_ws', 'avg_heat_total_ws', 'heat_count_wd', 
    'heat_win_wd', 'avg_heat_total_wd', 'heat_count_bt', 'heat_win_bt', 
    'avg_heat_total_bt', 'prev_event_place', 'prev_event_points', 'prev_3_event_points', 
    'prev_5_event_points', 'prev_year_place','prev_10_heat_place']