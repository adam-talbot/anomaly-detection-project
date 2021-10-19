####### PREPARE FUNCTIONS FOR CURRICULUM LOG DATA ######

import pandas as pd
import numpy as np

def prep_log(df):
    '''
    Taken in newly acquired df and does all preparation (see code for detailed cleaning steps)
    '''
    df['date'] = df.date + ' ' + df.time
    date_cols = [
        'date',
        'start_date',
        'end_date',
        'created_at',
        'updated_at'
    ]
    df[date_cols] = df[date_cols].apply(pd.to_datetime)
    df = df.set_index(df.date)
    program_dict = {
    1 : 'Web Dev - PHP',
    2 : 'Web Dev - Java',
    3 : 'Data Science',
    4 : 'Web Dev - Front End'
    }
    df['program'] = df.program_id.map(program_dict)
    cols_to_drop = [
        'date',
        'time',
        'id',
        'cohort_id',
        'slack',
        'deleted_at',
        'program_id'   
    ]
    df = df.drop(columns=cols_to_drop)
    df['module/lesson'] = df.path.str.split('/').str[0] + '/' + df.path.str.split('/').str[1]
    return df