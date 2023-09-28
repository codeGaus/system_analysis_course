import pandas as pd


def main(*args, **kwargs):
    path = kwargs.get('file_path')
    row = kwargs.get('row')
    col = kwargs.get('col')

    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f'Ошибка при открытии файла: {str(e)}')
        return

    try:
        print(df.iloc[col, row])
    except Exception as e:
        print(f'Ошибка индексирования: {str(e)}')


if __name__ == '__main__':
    main(file_path='example.csv', row=2, col=2)
