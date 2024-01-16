import json
import numpy as np


def read_json_file(file):
    with open(file, "r") as f:
        j = json.load(f)
    return j


def create_list(exp_list):
    exp_indexes, exp_flatten = [], []
    pos = 0
    for k in exp_list:
        if isinstance(k, int):
            k = [k]
        for value in k:
            exp_indexes.append(pos)
            exp_flatten.append(value)
        pos += 1

    return exp_flatten, exp_indexes


def matrix_calculate(exp_list):
    exp_flatten, exp_indexes = create_list(exp_list)

    matrix = [
        [0 for _ in range(len(exp_flatten))]
        for _ in range(len(exp_flatten))
    ]

    for i in range(len(exp_indexes)):
        for j in range(len(exp_indexes)):
            if (
                exp_indexes[exp_flatten.index(i + 1)]
                <= exp_indexes[exp_flatten.index(j + 1)]
            ):
                matrix[i][j] = 1

    return matrix


def get_result(expert_1, expert_2, kernel):
    result = []
    for i in range(len(expert_1)):
        if isinstance(expert_1[i], int):
            expert_1[i] = [expert_1[i]]
        for j in range(len(expert_2)):
            if isinstance(expert_2[j], int):
                expert_2[j] = [expert_2[j]]
            expert_1_set = set(expert_1[i])
            expert_2_set = set(expert_2[j])
            for value in expert_1[i]:
                for k in kernel:
                    if value in k:
                        flag, k = (True, k)
                    else:
                        flag, k = (False, [])
                if flag:
                    if k not in result:
                        result.append(k)
                        break
            inter = expert_1_set.intersection(expert_2_set)
            if inter and not flag:
                if len(inter) > 1:
                    result.append(list(inter))
                else:
                    result.append(inter.pop())

    print(result)


def kernel_calculate(matrix_1, matrix_2):
    matrix_1 = np.array(matrix_1)
    matrix_2 = np.array(matrix_2)

    kernel = np.multiply(matrix_1, matrix_2)
    kernel_T = np.multiply(matrix_1.T, matrix_2.T)

    kernel_res = np.logical_or(kernel, kernel_T).astype(np.int32)
    result = []

    for i in range(len(kernel_res)):
        for j in range(len(kernel_res[i])):
            if kernel_res[i][j] == 0:
                pair = sorted([i + 1, j + 1])
                if pair not in result:
                    result.append(pair)
    conc_result = []
    checked = [0 for _ in range(len(result))]
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            set_1 = set(result[i])
            set_2 = set(result[j])

            if set_1.intersection(set_2):
                checked[i] = 1
                checked[j] = 1
                conc_result.append(list(set_1.union(set_2)))

        if result[i] not in conc_result and checked[i] == 0:
            conc_result.append(result[i])

    return conc_result


def main():
    exp_A = [
        [1],
        [2, 3, 4],
        [5, 6, 7],
        8,
        9,
        10,
    ] 
    exp_B = [
        [1, 2, 3],
        [4, 5],
        6,
        7,
        9,
        [8, 10],
    ]
    exp_C = [
        1,
        4,
        3,
        2,
        6,
        [5, 7, 8],
        [9, 10],
    ]
    
    matrix_A = matrix_calculate(exp_A)
    matrix_B = matrix_calculate(exp_B)
    matrix_C = matrix_calculate(exp_C)
    kernel_AB = kernel_calculate(matrix_A, matrix_B)
    kernel_BC = kernel_calculate(matrix_B, matrix_C)

    get_result(exp_A, exp_B, kernel_AB)


if __name__ == "__main__":
    main()
