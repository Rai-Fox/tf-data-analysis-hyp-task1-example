import pandas as pd
import numpy as np

from scipy.stats import binom

chat_id = 222287279 # Ваш chat ID, не меняйте название переменной

def solution(
        x_success: int, 
        x_cnt: int, 
        y_success: int, 
        y_cnt: int,
) -> bool:
    alpha = 0.03
    p_value = binom(n=y_cnt, p=x_success/x_cnt).cdf(y_success)
    return p_value > 1 - alpha
