"""Module used for reading and writing files"""
import csv
import os


def read_csv(path: str) -> list:
    with open(path, 'r') as fr:
        reader = csv.reader(fr)
        rows = [row for row in reader]
    return rows


def read_txt(path: str) -> list:
    with open(path, 'r') as fr:
        stripped = [line.strip() for line in fr]
        # lines = [line.split() for line in stripped if line]

    return stripped


def write_csv(path: str) -> None:
    text =read_txt(path)
    with open(f"{os.path.splitext(path)[0]}.csv", 'w') as fw:
        writer = csv.writer(fw)
        for row in text:
            writer.writerow(row)


def write_txt(path: str) -> None:
    text =read_csv(path)
    with open(f'{os.path.splitext(path)[0]}.txt', 'w') as fw:
        return fw.writelines(text)

if __name__ == '__main__':
    pass

    print(read_txt(r"D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\text.txt"))
    print(read_csv(r"D:\Gabriel\Curs_Python\Password Manager\userdata.csv"))
    write_csv(r'D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\text.txt')
    # write_txt(r"D:\Gabriel\Curs_Python\Password Manager\userdata.csv")
    # write_csv(r"D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\libs\test_w_text.txt")


