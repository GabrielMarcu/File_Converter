"""Module used for reading and writing files"""
import csv


def read_csv(path: str) -> list:
    with open(path, 'r') as fr:
        reader = csv.reader(fr)
        rows = ['\n'.join(row) for row in reader]
    return rows


def read_txt(path: str) -> list:
    with open(path, 'r') as fr:
        stripped = [line.strip() for line in fr]
        # lines = [line.split() for line in stripped if line]

    return stripped


def write_csv(output_path: str, lista: list) -> None:
    """Creates a new csv file"""
    with open(output_path, 'w', newline='') as fw:
        writer = csv.writer(fw)
        writer.writerows(lista)


def write_txt(output_path: str, lista) -> None:
    """Creates a new text file"""

    with open(output_path, 'w') as fr:
        for row in lista:
            fr.writelines(row)



if __name__ == '__main__':
    pass
    print(read_txt(r"D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\text.txt"))
    # print(read_csv(r"D:\Gabriel\Curs_Python\Password Manager\userdata.csv"))
    # write_csv(r'D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\text.txt', 'test_w_csv.csv')
    # write_txt('test_w_text.txt')