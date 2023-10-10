import pandas as pd


class DataSet:

    def __init__(self, file_name: str, sep="\t") -> None:
        try:
            self.file = pd.read_csv(file_name, sep=sep, header=None, engine="python")
        except FileNotFoundError:
            print("Plik nie został znaleziony.")
        except pd.errors.EmptyDataError:
            print("Plik jest pusty lub nie zawiera danych.")

    def get_value(self, col: int, row: int) -> int | float:
        return self.file[col][row]

    def get_value_and_type(self, col: int, row: int) -> tuple:
        return self.file[col][row], type(self.file[col][row])


if __name__ == "__main__":
    ds_wartosci = DataSet("iris.txt")
    ds_atr = DataSet("iris-type.txt")

    print(ds_wartosci.get_value(4, 2))
    print(ds_wartosci.get_value_and_type(2, 2))
