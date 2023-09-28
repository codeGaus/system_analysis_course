import pandas as pd


# я начальник
def r1(df: pd.DataFrame, elem: int):
    count = 0
    row = df.loc[elem]
    for i in range(1, len(row) + 1):
        # print(j)
        i = str(i)
        # print(row[j])
        if row[i] != 0:
            count += 1
    return count


# я подчиненный
def r2(df: pd.DataFrame, elem: int, get_bosses=False):
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


# у моего подчиненного есть подчиненный
def r3(df: pd.DataFrame, elem: int):
    count = 0
    row = df.loc[elem]
    # print(row)
    for i in range(1, len(row) + 1):
        i = str(i)
        if row[i] != 0:
            # print(i)
            count += r1(df, int(i))
    return count


# у моего начальника есть начальник
def r4(df: pd.DataFrame, elem: int):
    count = 0
    _, bosses = r2(df, elem, get_bosses=True)
    for boss in bosses:
        count += r2(df, boss)
    return count


# соподчинение
def r5(df: pd.DataFrame, elem: int):
    count = 0
    _, bosses = r2(df, elem, get_bosses=True)
    for boss in bosses:
        count += r1(df, boss) - 1
    return count


def read_file(graph: str):
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


def main():
    df = read_file('example.csv')
    stat = get_statistic(df)
    print('   r1 r2 r3 r4 r5')
    for i, s in enumerate(stat):
        print(f'{i + 1}: {s}')


if __name__ == '__main__':
    main()
