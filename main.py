import random
import time


# класс фермы
class Farm:
    def __init__(self):
        self.animals = []
        self.all_products = {}

    # функция добавления животного
    def add_animal(self, animal):  # животное, его продукт, единица измерения продукта
        self.animals.append(animal)

    # продукция за 1 сбор
    def get_results(self):
        self.products = {}
        self.animals.sort(key=lambda x: x.name)
        for i in self.animals:
            if i.name not in self.products:
                self.products[i.name] = random.randint(i.x, i.y)
            else:
                self.products[i.name] += random.randint(i.x, i.y)
        for i in self.products:
            if i not in self.all_products:
                self.all_products[i] = self.products[i]
            else:
                self.all_products[i] += self.products[i]

    # продукция за все время
    def get_global_results(self):
        print("собрано за неделю: " + str(self.all_products))
        print("------------------------------------")

    # количество животных каждого вида
    def get_count(self):
        self.animals.sort(key=lambda x: x.name)
        a = set([i.name for i in self.animals])
        print("количество различных видов животных:")
        for i in a:
            print(i, [i.name for i in self.animals].count(i))
        print("------------------------------------")


# класс животного
class Animal:
    number = 1

    def __init__(self, name, x, y):
        self.number = Animal.number  # уникальный регистрационный номер
        Animal.number += 1
        self.name = name  # вид животного
        self.x = x  #  минимальное кол-во продокта,
        self.y = y  # максимальное кол-во продокта,


# Инициализация фермы с животными
#------Система должна добавить животных в хлев (10 коров и 20 кур).------
farm = Farm()
for i in range(10):
    farm.add_animal(Animal("Корова", 8, 12))
for i in range(20):
    farm.add_animal(Animal("Курочка", 0, 1))
#------Вывести на экран информацию о количестве каждого типа животных на ферме.------
farm.get_count()


def auto_run():  #запуск скрипта на неделю
    start = time.time()
    c = 0
    while True:
        if time.time() - start > 86400:  # если разница между запуском и текущим временем равна 86400сек (24 часа). Для проверки можно поменять на 1 секунду
            start = time.time()
            c += 1
            farm.get_results()  # сбор продукции
            if c == 7:  # после 7 дней сбора продукции
                farm.get_global_results()  # подсчет продукции за неделю
                return


#------7 раз (неделю) произвести сбор продукции (подоить коров и собрать яйца у кур)------
#------Вывести на экран общее кол-во собранных за неделю шт. яиц и литров молока.------
auto_run()

#------Добавить на ферму ещё 5 кур и 1 корову (съездили на рынок, купили животных)------
for i in range(5):
    farm.add_animal(Animal("Курочка", 0, 1))
farm.add_animal(Animal("Корова", 8, 12))

#------Снова вывести информацию о количестве каждого типа животных на ферме.------
farm.get_count()

#------Снова 7 раз (неделю) производим сбор продукции и выводим результат на экран.------
auto_run()
