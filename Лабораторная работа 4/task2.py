# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(file_name) -> None:
    with open(file_name, "r") as file_reading:
        data_raw = csv.DictReader(file_reading)  # TODO считать содержимое csv файла
        data_final = []
        for column in data_raw:
            data_final.append(column)
    ensure = False
    indent = 4
    data_for_writing = json.dumps(data_final, ensure_ascii=ensure, indent=indent)
    with open(OUTPUT_FILENAME, "w") as file_writing:
        file_writing.write(data_for_writing)# TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
