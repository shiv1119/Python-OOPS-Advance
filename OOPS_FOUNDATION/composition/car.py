from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class ElectricEngine(Engine):
    def start(self):
        print("Electric Engine started")

class PetrolEngine(Engine):
    def start(self):
        print("Petrol engine started")

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()

car1 = Car(PetrolEngine()).start()
car2 = Car(ElectricEngine()).start()