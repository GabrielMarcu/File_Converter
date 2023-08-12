"""Module used for reading and writing files"""
import csv


def read_csv(path: str) -> list[list]:
    with open(path, 'r') as fr:
        reader = csv.reader(fr)
        rows = [row for row in reader]
    return rows


def read_txt(path: str) -> list[list]:
    with open(path, 'r') as fr:
        stripped = (line.strip() for line in fr)
        lines = [line.split(",") for line in stripped if line]
    return lines


def write_csv(path: str) -> None:
    pass


def write_txt(path: str) -> None:
    pass


if __name__ == '__main__':
    print(read_txt(r"D:\Gabriel\Curs_Python\Team_Project\Read_File\test.txt"))
    print(read_csv(r"D:\Gabriel\Curs_Python\Password Manager\userdata.csv"))