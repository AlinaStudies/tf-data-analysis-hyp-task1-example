import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 721973830

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.1
    p1 = x_success / x_cnt  
    p2 = y_success / y_cnt
    successes = [x_success, y_success]
    cnts = [x_cnt, y_cnt]
    _, pval = proportions_ztest(count=successes, nobs=cnts, value=p2-p1, alternative='smaller')
    return pval < alpha
