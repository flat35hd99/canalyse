import pandas as pd


class ConductivityParser:
    def __init__(self, header=["source", "target", "conductivity"]):
        self.header = header

    def run(self, filename):
        df = pd.read_table(
            filename,
            delim_whitespace=True,
            header=None,
            names=self.header,
        )
        return df


def conductivity_parser():
    return ConductivityParser


def get_number(col):
    return col.split()[0]


def get_residue(col):
    return col.split()[1]


class ConductivityFormatter:
    def __init__(self):
        pass

    def run(self, df):
        df = df.copy()
        for header in ["source", "target"]:
            df[f"{header}_numbeer"] = df[header].map(get_number)
            df[f"{header}_residue"] = df[header].map(get_residue)
        return df
