# TODO решите задачу
import json
def task(data) -> float:
    total_value = 0
    for elem in data:
        total_value += elem["score"] * elem["weight"]
    return round(total_value, 3)


file_name = "input.json"
with open(file_name, "r") as file:
    data = json.load(file)


print(task(data))
