class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        :param make: Производитель транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self._make = make
        self._model = model
        self._year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.
        """
        return f"{self._year} {self._make} {self._model}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление транспортного средства.
        """
        return f"Vehicle(make='{self._make}', model='{self._model}', year={self._year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.

        :return: Сообщение о запуске двигателя.
        """
        return "Двигатель запущен."


class Car(Vehicle):
    """
    Класс легкового автомобиля, наследующий от Vehicle.
    """

    def __init__(self, make: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param make: Производитель легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей в легковом автомобиле.
        """
        super().__init__(make, model, year)
        self.doors = doors

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        Переопределяет метод базового класса для добавления информации о количестве дверей.
        """
        return f"{super().__str__()} с {self.doors} дверями"

    def start_engine(self) -> str:
        """
        Запускает двигатель легкового автомобиля.

        Переопределяет метод базового класса, чтобы добавить дополнительное сообщение о запуске двигателя.

        :return: Сообщение о запуске двигателя с указанием типа автомобиля.
        """
        return f"{super().start_engine()} Это легковой автомобиль."


class Truck(Vehicle):
    """
    Класс грузового автомобиля, наследующий от Vehicle.
    """

    def __init__(self, make: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        :param make: Производитель грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param capacity: Грузоподъемность грузового автомобиля в тоннах.
        """
        super().__init__(make, model, year)
        self.__capacity = capacity  # Приватный атрибут для грузоподъемности

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        Переопределяет метод базового класса для добавления информации о грузоподъемности.
        """
        return f"{super().__str__()} с грузоподъемностью {self.__capacity} тонн"

    def load_cargo(self, weight: float) -> str:
        """
        Загружает груз в грузовой автомобиль.

        :param weight: Вес груза в тоннах.

        :return: Сообщение о загрузке груза или предупреждение о превышении грузоподъемности.
        """
        if weight > self.__capacity:
            return "Ошибка: превышена грузоподъемность."
        return f"Груз {weight} тонн загружен."


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2024, 4)
    print(car)
    print(car.start_engine())
    truck = Truck("Volvo", "FH16", 2024, 12.0)
    print(truck)
    print(truck.load_cargo(15.0))
