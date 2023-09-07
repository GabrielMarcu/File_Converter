"""Module used for reading and writing files"""
import csv
import os


def read_csv(path: str) -> list[str]:
    """
    Reads a csv file and returns a list of strings, each string is a row in the file
    """
    with open(path, 'r') as fr:
        reader = csv.reader(fr)
        rows = [','.join(row) for row in reader]
    return rows


def read_txt(path: str) -> list[list]:
    """Reads text files and returns a list with elements of type list, each element is a row in the file"""
    with open(path, 'r') as fr:
        stripped = [line.strip() for line in fr]
        lines = [line.split() for line in stripped if line]

    return lines


def write_csv(path: str, file_text: list[list]) -> None:
    """Writes a new csv file or overwrites an existing one """
    with open(f"{os.path.splitext(path)[0]}.csv", 'w', newline='') as fw:
        writer = csv.writer(fw)
        for row in file_text:
            writer.writerow(row)


def write_txt(path: str, file_text: str) -> None:
    """Writes a new text file or overwrites and existing one"""
    with open(f'{os.path.splitext(path)[0]}.txt', 'w', newline='\n') as fw:
        for row in file_text:
            fw.write(row)


if __name__ == '__main__':
    pass

    print(read_txt(r"D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\text.txt"))
    print(read_csv(r"D:\Gabriel\Curs_Python\Password Manager\userdata.csv"))
    # write_csv(r'D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\text.txt')
    # write_txt(r"D:\Gabriel\Curs_Python\Password Manager\userdata.csv")
    # write_csv(r"D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\libs\text.txt")


