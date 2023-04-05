import pandas as pd
import numpy as np

from scipy.stats import norm

#task 2
chat_id = 434559054 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    a = 1/24 * (x**2).sum() /  (norm.ppf(1 - alpha/2) * np.sqrt(len(x)) + len(x))
    b = 1/24 * (x**2).sum() /  (norm.ppf(alpha/2) * np.sqrt(len(x)) + len(x))
    return np.sqrt(a), \
           np.sqrt(b)
