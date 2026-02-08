import doctest
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        pass

    @abstractmethod
    def stop_engine(self) -> None:
        pass

class Computer(ABC):
    def __init__(self, brand: str, ram: int, storage: int):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    @abstractmethod
    def boot(self) -> None:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass

class Smartphone(Computer):
    def __init__(self, brand: str, model: str, ram: int, storage: int):
        super().__init__(brand, ram, storage)
        self.model = model

    @abstractmethod
    def make_call(self, number: str) -> None:
        pass

    @abstractmethod
    def take_photo(self) -> None:
        pass

class Car(Vehicle):
    def start_engine(self) -> None:
        print(f"{self.make} {self.model} engine started.")

    def stop_engine(self) -> None:
        print(f"{self.make} {self.model} engine stopped.")

class Laptop(Computer):
    def boot(self) -> None:
        print(f"{self.brand} laptop is booting up.")

    def shutdown(self) -> None:
        print(f"{self.brand} laptop is shutting down.")

class MobilePhone(Smartphone):
    def __init__(self, brand: str, model: str, ram: int, storage: int):
        super().__init__(brand, model, ram, storage)

    def boot(self) -> None:
        print(f"{self.brand} smartphone is booting up.")

    def shutdown(self) -> None:
        print(f"{self.brand} smartphone is shutting down.")

    def make_call(self, number: str) -> None:
        print(f"Calling {number} from {self.brand} {self.model}.")

    def take_photo(self) -> None:
        print(f"Taking a photo with {self.brand} {self.model}.")

if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2025)
    car.start_engine()
    car.stop_engine()

    laptop = Laptop("Dell", 16, 512)
    laptop.boot()
    laptop.shutdown()

    smartphone = MobilePhone("Apple", "iPhone 16", 6, 256)
    smartphone.boot()
    smartphone.shutdown()
    smartphone.make_call("+79000000000")
    smartphone.take_photo()
