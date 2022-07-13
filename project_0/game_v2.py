"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

from ast import While
from statistics import median
import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    max_number, min_number = 100, 1  # max, min значения диапазона чисел 
     
    while True:   # сравнение предполагаемого числа с серединой диапазона
        count += 1
        if predict_number > number:
           max_number = predict_number - 1
           predict_number = (max_number + min_number) // 2 
        elif predict_number < number:
           min_number = predict_number + 1
           predict_number = (max_number + min_number) // 2 
        else:
            break
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
        
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
