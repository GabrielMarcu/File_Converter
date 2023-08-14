"""Module used for reading and writing files"""
import csv


def read_csv(path: str) ->list[list]:
    pass


def read_txt(path: str) -> list:
    pass


def write_csv(path: str) -> None:
    text = read_txt(path)
    with open(path, 'w') as fw:
        writer = csv.writer(fw)
        return writer.writerow(text)

def write_txt(path: str) -> None:
    text = read_csv(path)
    with open(path, 'w') as fw:
        return fw.writelines(text)


