import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Table:
    def __init__(self, material: str, width: (int, float), length: (int, float)):
        """
                Создание и подготовка к работе объекта "Стол"

                :param material: материал стола
                :param width: ширина стола
                :param length: длина стола
                :raise TypeError: если типы данных неправильные, то ошибка
                :raise ValueError: параметры стола должны быть положительными, иначе - ошибка

                Примеры:
                >>> table = Table("wood", 500, 110)  # инициализация экземпляра класса
                """
        if not isinstance(material, str):
            raise TypeError("Material should be string type")
        self.material = material
        if not isinstance(width, (int, float)):
            raise TypeError("Width should be int or float type")
        if width <= 0:
            raise ValueError("Width should be positive")
        self.width = width
        if not isinstance(length, (int, float)):
            raise TypeError("Length should be int or float type")
        if length <= 0:
            raise ValueError("Length should be positive")
        self.length = length

    def area_calculation(self) -> float:
        """
        Рассчитывает площадь поверхности стола.

        :return: площадь стола

        >>> table = Table("wood", 100, 234)
        >>> table.area_calculation()
        """
        ...

    def is_wooden(self) -> bool:
        """
        Функция, которая проверяет, является ли стол деревянным

        :return: Является ли стол деревянным

        Примеры:
        >>> table = Table("metal", 100, 200)
        >>> table.is_wooden()
        """
        ...

class Book:
    def __init__(self, author: str, name: str, year: int):
        """
         Создание и подготовка к работе объекта "Книга"

        :param author: автор книги
        :param name: название книги
        :param year: год издания книги
        :raise TypeError: если типы данных неправильные, то ошибка
        :raise ValueError: год издания книги не может быть отрицательным

        Примеры:
        >>> book = Book("Пушкин А.С.", "Евгений Онегин", 1988)  # инициализация экземпляра класса
        """
        if not isinstance(author, str):
            raise TypeError("Author should be string type")
        self.author = author
        if not isinstance(name, str):
            raise TypeError("Name should be string type")
        self.name = name
        if not isinstance(year, int):
            raise TypeError("Year should be int type")
        if year < 0:
            raise ValueError("Year should be non-negative")

    def get_description(self) -> str:
        """
        Возвращает краткое описание книги

        :return: Строка с названием книги и автором

        Пример:
        >>> book = Book("Пушкин А.С.", "Евгений Онегин", 1988)
        >>> book.get_description()
        """
        ...

    def is_antique(self) -> bool:
        """
        Проверяет, является ли книга антикварной

        :return: Является ли книга антикварной

        >>> book = Book("Пушкин А.С.", "Евгений Онегин", 1988)
        >>> book.is_antique()
        """
        ...

class Galaxy:
    def __init__(self, name: str, number_of_stars: int, age: (int, float)):
        """
         Создание и подготовка к работе объекта "Галактика"

        :param name: название галактики
        :param number_of_stars: количество звезд галактики
        :param age: возраст галактики
        :raise TypeError: если типы данных неправильные, то ошибка
        :raise ValueError: возраст и количество звезд галактики не может быть отрицательным или равным нулю

        Примеры:
        >>> galaxy = Galaxy("Млечный путь", 233, 1988)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Name should be string type")
        self.name = name
        if not isinstance(number_of_stars, int):
            raise TypeError("Number of stars should be int type")
        if number_of_stars <= 0:
            raise ValueError("Number of stars should be positive")
        self.number_of_stars = number_of_stars
        if not isinstance(age, int):
            raise TypeError("Age should be int or float type")
        if age <= 0:
            raise ValueError("Age should be positive")
        self.age = age

    def get_info(self) -> str:
        """
        Возвращает строку, содержащую краткую информацию о галактике

        :return: Описание галактики
        >>> galaxy = Galaxy("Млечный путь", 214, 1244)
        >>> galaxy.get_info()
        """
        ...

    def update_age(self, new_age: (int, float)) -> None:
        """
        Обновляет возраст галактики

        :param new_age: Новый возраст галактики
        :raise ValueError: новый возраст галактики должен быть положительным
                           (однако, он может стать меньше, т.к. прошлые данные могли быть неверными)
        :raise TypeError: если тип данных неверный, то ошибка

        >>> galaxy = Galaxy("Млечный путь", 123, 1234532)
        >>> galaxy.update_age(413444)
        """
        if new_age <= 0:
            raise ValueError("New age should be positive")
        if not isinstance(new_age, (int, float)):
            raise TypeError("New age should be int or float type")
        self.age = new_age



if __name__ == "__main__":
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
