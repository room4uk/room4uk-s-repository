numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers1 = numbers[:4]
numbers2 = numbers[5:]
s = sum(numbers1) + sum(numbers2)
l = len(numbers)
sr = s/l
numbers[4] = sr
print("Измененный список:", numbers)
