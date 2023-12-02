import random
import time

import numpy as np
import concurrent.futures
from math import sqrt



def init_numbers():
    return [random.randint(1, 100) for _ in range(100)], [random.randint(1, 100) for _ in range(100)]
p, q = init_numbers()

def calculate_field(i, j, p=p, q=q):
    return sqrt(abs(q[j] - p[i]))


def build_matrix_consistently(p=p, q=q):
    matrix = np.zeros((len(q), len(p)))
    for i in range(len(p)):
        for j in range(len(q)):
            matrix[i][j] = sqrt(abs(q[j] - p[i]))
    return matrix

def build_matrix_concurrently(p=p, q=q):
    matrix = np.zeros((len(q), len(p)))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        fields = {}
        for i in range(len(p)):
            for j in range(len(q)):
                fields[(i, j)] = executor.submit(calculate_field,i,j)

        for i in range(len(p)):
            for j in range(len(q)):
                matrix[i][j] = fields[(i, j)].result()

    return matrix


if __name__ == '__main__':
    start1 = time.time()
    build_matrix_concurrently()
    end1 = time.time()
    start2 = time.time()
    build_matrix_consistently()
    end2 = time.time()
    print(f"Consistently: {end1 - start1}")
    print(f"Concurrently: {end2 - start2}")