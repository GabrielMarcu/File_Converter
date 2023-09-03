"""Docstring"""
import os.path

import read_write as rw


def convert_to_txt(path: str):
    file_list = rw.read_csv(path)
    output_path = os.path.splitext(path)[0]
    rw.write_txt(f'{output_path}.txt', file_list)
    print(f'File {output_path} converted to txt')


def convert_to_csv(path: str):
    file_list = rw.read_txt(path)
    output_path = os.path.splitext(path)[0]
    rw.write_csv(f"{output_path}.csv", file_list)
    print(f'File {output_path} converted to csv')

if __name__ == '__main__':
    # convert_to_csv('test_w_text.txt')
    convert_to_txt('test_w_csv.csv')
