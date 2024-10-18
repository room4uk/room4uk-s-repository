# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 * 1024 * 1024
papers = 100
strings = 50
symbols = 25
symbol_size = 4

one_book = strings * symbols * symbol_size * papers

print("Количество книг, помещающихся на дискету:", int(disk_size//one_book))