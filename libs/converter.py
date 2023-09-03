"""Docstring"""
import os.path




def text_to_csv(input_path, output_path) -> None:
    """
    This function converts the text file into a csv file
    """
    if os.path.splitext(input_path)[1] != '.txt':
        raise ValueError('Wrong input file. It must be a text file!')
    if os.path.splitext(output_path)[1] != '.csv':
        raise ValueError('Wrong output file. It must be a csv file!')

    with open(input_path, 'r') as text_file:
        lines = text_file.readlines()

    with open(output_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in lines:
            csv_writer.writerow([line.strip()])


def csv_to_text(input_path, output_path) -> None:
    """
    This function converts a csv file into a text file
    """
    if os.path.splitext(input_path)[1] != '.csv':
        raise ValueError('Wrong input file. It must be a csv file!')
    if os.path.splitext(output_path)[1] != '.txt':
        raise ValueError('Wrong output file. It must be a txt file!')

    with open(input_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = [",".join(row) for row in csv_reader]

    with open(output_path, 'w') as text_file:
        text_file.write("\n".join(lines))


def convert_to_csv(path: str):
    file_list = rw.read_txt(path)
    output_path = os.path.splitext(path)[0]
    rw.write_csv(f"{output_path}.csv", file_list)
    print(f'File {output_path} converted to csv')

if __name__ == '__main__':

    try:
        input_file = input('input file: ')
        output_file = input('output file: ')
        text_to_csv(input_file, output_file)
    except ValueError as e:
        print(f'Error -> {e}')

    try:
        input_csv_file = input('csv file: ')
        output_csv_file = input('text file: ')
        csv_to_text(input_csv_file, output_csv_file)
    except ValueError as e:
        print(f'Error -> {e}')


