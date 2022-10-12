# Inheritance concept
print("Inheritance concept\n\n")


class Person:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def getName(self):
        return self.name


class Employee(Person):
    def __init__(self, name, lastName, job):
        Person.__init__(self, name, lastName)

        self.job = job


# objects
emp = Employee("safiullah", "jalalzai", "Eng")
print("Employee Name    :    " + emp.name)
print("Employee LastName:    " + emp.lastName)
print("Employee Job     :    " + emp.job)


# ploymorphism concept

print("\n\nploymorphism concept\n\n")


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animals eat different Food")


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def eat(self):
        print("cat eat meat")


# instance
animal = Animal("animl")
animal.eat()

cat = Cat("Mycay")
cat.eat()


# Encapsolation concept
print("\n\n Encapsolation concept\n\n")


class Product:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getId(self):
        return self.__id


# instance

product = Product(1, "pen")
print("product: " + product.getName())
product.setName("book")
print("product: " + product.getName())


# Abustruction concept

print("\n\nAbustruction concept\n\n")

from abc import ABC, abstractmethod


class Book(ABC):
    @abstractmethod
    def bookTitle(self):
        pass


class History(Book):
    def bookTitle(self):
        print("book title is history")


# instance

history = History()
history.bookTitle()
