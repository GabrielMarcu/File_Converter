"""Docstring"""
import os.path
import read_write as rw
import csv


def text_to_csv(input_path) -> None:
    """
    This function converts the text file into a csv file
    """
    if os.path.splitext(input_path)[1] != '.txt':
        raise ValueError('Wrong input file. It must be a text file!')

    file_text = rw.read_txt(input_path)
    rw.write_csv(input_path, file_text)


def csv_to_text(input_path) -> None:
    """
    This function converts a csv file into a text file
    """
    if os.path.splitext(input_path)[1] != '.csv':
        raise ValueError('Wrong input file. It must be a csv file!')

    file_text = '\n'.join(rw.read_csv(input_path))
    rw.write_txt(input_path, file_text)


if __name__ == '__main__':

    # try:
    #     input_file = input('input file: ')
    #     output_file = input('output file: ')
    #     text_to_csv(input_file, output_file)
    # except ValueError as e:
    #     print(f'Error -> {e}')
    #
    # try:
    #     input_csv_file = input('csv file: ')
    #     output_csv_file = input('text file: ')
    #     csv_to_text(input_csv_file, output_csv_file)
    # except ValueError as e:
    #     print(f'Error -> {e}')

    # text_to_csv(r"D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\text.txt")
    # csv_to_text(r"D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\libs\csv.csv")
    text_to_csv(r"D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\libs\text.txt")
    # file_text = (rw.read_txt(r"D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\libs\text.txt"))
    # print(file_text)
    # file_text = list(rw.read_csv(r"D:\Gabriel\Curs_Python\Team_Project\CSV_to_TXT_to_CSV\libs\csv.csv"))
    # print(file_text)