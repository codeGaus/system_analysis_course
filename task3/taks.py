import pandas as pd
from math import log


def r1(df: pd.DataFrame, elem: int):
    """Я начальник"""
    count = 0
    row = df.loc[elem]
    for i in range(1, len(row) + 1):
        # print(j)
        i = str(i)
        # print(row[j])
        if row[i] != 0:
            count += 1
    return count


def r2(df: pd.DataFrame, elem: int, get_bosses=False):
    """Я подчиненный"""
    count = 0
    bosses = []
    for i, row in df.iterrows():
        for j in range(1, len(row) + 1):
            # print(j)
            j = str(j)
            # print(row[j])
            if row[j] != 0 and i != elem and int(j) == elem:
                bosses.append(i)
                count += 1
    if get_bosses:
        return count, bosses
    else:
        return count


def r3(df: pd.DataFrame, elem: int):
    """У моего подчиненного есть подчиненный"""
    count = 0
    row = df.loc[elem]
    # print(row)
    for i in range(1, len(row) + 1):
        i = str(i)
        if row[i] != 0:
            # print(i)
            count += r1(df, int(i))
    return count


def r4(df: pd.DataFrame, elem: int):
    """У моего начальника есть начальник"""
    count = 0
    _, bosses = r2(df, elem, get_bosses=True)
    for boss in bosses:
        count += r2(df, boss)
    return count


def r5(df: pd.DataFrame, elem: int):
    """Cоподчинение"""
    count = 0
    _, bosses = r2(df, elem, get_bosses=True)
    for boss in bosses:
        count += r1(df, boss) - 1
    return count


def read_file(graph: str):
    """Чтение графа из файла"""
    try:
        df = pd.read_csv(graph)
        df.index = range(1,len(df)+1)
    except Exception as e:
        print(f'Ошибка при открытии файла: {str(e)}')
        return None
    return df


def get_statistic(df: pd.DataFrame):
    stat = []
    for i in range(1, len(df) + 1):
        stat.append([r1(df, i), r2(df, i), r3(df, i), r4(df, i), r5(df, i)])
        # print(f'{r1(df, i)} {r2(df, i)} {r3(df, i)} {r4(df, i)} {r5(df, i)}')
    return stat


def entropy(row: list) -> float:
    """Энтропия для i-ой строки"""
    sum = 0
    for el in row:
        if el != 0:
            sum += el * log(el, 2)
    return -sum


def system_entropy(lst: list):
    """Энтропия системы"""
    probs = []
    for i in range(len(lst)):
        tmp = []
        for j in range(len(lst[0])):
            tmp.append(lst[i][j] / (len(lst) - 1))
        probs.append(tmp)

    entropy_values = []
    for row in probs:
        entropy_values.append(entropy(row))
    # print(entropy_values)

    return round(sum(entropy_values), 2)


def main():
    df = read_file('example.csv')
    print('Исходный граф системы:')
    print(df)
    print()

    stat = get_statistic(df)
    print('Значения отношений:')
    print('   r1 r2 r3 r4 r5')
    for i, s in enumerate(stat):
        print(f'{i + 1}: {s}')
    print()

    print('Энтропия системы: ', end='')
    print(system_entropy(stat))


if __name__ == '__main__':
    main()
