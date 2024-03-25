import pandas as pd


class FileManager:
    def __init__(self, *filenames):
        self.filenames = filenames

    def open_file(self):
        res = []
        for file in self.filenames:
            res.append(pd.read_csv(file, sep=","))
        return res