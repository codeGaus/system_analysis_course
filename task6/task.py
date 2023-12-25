import numpy as np


def calculate_kendell(exp):
    '''Calculate Kendell'''
    matr = [[0 for i in range(len(exp))] for _ in range(len(exp[0]))]
    matr_eta = [[len(exp[0]) - j for _ in range(len(exp))] for j in range(len(exp[0]))]
    all_elements = sorted(exp[0])
    for i in range(len(exp)):
        for j in range(len(exp[i])):
            matr[j][i] = len(exp[i]) - exp[i].index(all_elements[j])
    matr = np.array(matr)
    matr_eta = np.array(matr_eta)

    disp_m = ((matr_eta.sum(axis=-1) - matr_eta.sum(axis=-1).mean())**2).sum() \
        / (len(exp[0]) - 1)
    disp_matr = ((matr.sum(axis=-1) - matr.sum(axis=-1).mean())**2).sum() \
        / (len(exp[0]) - 1)

    print(disp_matr)
    print(disp_m)

    return disp_matr / disp_m


def run():
    exp_A = ["O1", "O2", "O3"]
    exp_B = ["O1", "O3", "O2"]
    exp_C = ["O1", "O3", "O2"] 
    exp = [exp_A, exp_B, exp_C]
    res = round(calculate_kendell(exp), 2)
    print(res)


if __name__ == "__main__":
    run()
