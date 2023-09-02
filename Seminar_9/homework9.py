from cmath import sqrt
from functools import wraps
import json
import csv
from random import randint
from typing import Callable

MIN_NUM = 1
MAX_NUM = 9
LINE_COUNT = 100

def find_root_in_cvs(func: callable):
    write_csv(f'{func.__name__}.cvs')
    @wraps(func)
    def wrapper(*args):
        with open(f'{func.__name__}.cvs', 'r') as f:
            reader = csv.reader(f, dialect='excel')
            count = 0
            for row in reader:
                if count > 0:
                    result = func(int(row[0]), int(row[1]), int(row[2]))
                count += 1
        return result
    return wrapper


def our_cash(func: callable):
    try:
        with open(f'{func.__name__}.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    @wraps(func)
    def wrapper(*args):
        arg = str(args)
        data_res = data.get(arg)
        if data_res:
            return data_res
        result = func(*args)
        data.update({arg: result})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(data, f, indent=4)
        return result

    return wrapper



def write_csv(file_name: str) -> None:
    list_csv = []
    for _ in range(LINE_COUNT):
        num_1, num_2, num_3 = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)
        list_csv.append([num_1, num_2, num_3])
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'c'])
        writer.writerows(list_csv)


@find_root_in_cvs
@our_cash
def find_root(a: int = 1, b: int = 1, c: int = 1) -> tuple[str, str] | str:
    discriminant = (pow(b, 2)) - (4 * a * c)
    if discriminant < 0:
        return f'no roots'
    if discriminant == 0:
        return str(-b / (2 * a))
    else:
        if a != 0:
            return str((-b + sqrt(discriminant)) / (2 * a)), str((-b - sqrt(discriminant)) / (2 * a))



if __name__ == '__main__':
    find_root()