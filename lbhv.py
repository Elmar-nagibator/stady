class Animal:
    def __init__(self, name, age, weight, habitat, diet):
        self.name = name
        self.age = age
        self.weight = weight
        self.habitat = habitat
        self.diet = diet

    def make_sound(self):
        print(f"{self.name} издает звук")

    def eat(self):
        print(f"{self.name} кушает {self.diet}")


class Bear(Animal):
    def __init__(self, name, age, weight, habitat, diet, fur_color):
        super().__init__(name, age, weight, habitat, diet)
        self.fur_color = fur_color

    def do_salto(self):
        print(f"{self.name} делает сальто на шаре!")

    def ballet_spin(self):
        print(f"{self.name} крутится как в балете!")


class Dolphin(Animal):
    def __init__(self, name, age, weight, habitat, diet, jump_height):
        super().__init__(name, age, weight, habitat, diet)
        self.jump_height = jump_height

    def jump_water(self):
        print(f"{self.name} выпрыгивает из воды на {self.jump_height} метров!")

    def spit_water(self):
        print(f"{self.name} плюется водой!")


class ZooShow:
    def __init__(self):
        self.bear = Bear("Балу", 5, 200, "Лес", "Мясо", "Коричневый")
        self.dolphin = Dolphin("Доди", 3, 100, "Море", "Рыба", 4)

    def start(self):
        print("--- Выберите шоу ---")
        print("1 - Шоу Медведя")
        print("2 - Шоу Дельфина")
        choice = input("Ваш выбор (1 или 2): ")

        if choice == "1":
            print("\nВы выбрали шоу Медведя!")
            self.bear.make_sound()
            self.bear.do_salto()
            self.bear.ballet_spin()
        elif choice == "2":
            print("\nВы выбрали шоу Дельфина!")
            self.dolphin.make_sound()
            self.dolphin.jump_water()
            self.dolphin.spit_water()
        else:
            print("Неверный ввод!")
            return

        print("\n--- Покупка билета ---")
        print("1 - Обычный (500 сом)")
        print("2 - VIP (1200 сом)")
        ticket = input("Выберите билет (1 или 2): ")

        if ticket == "2":
            print("\nВы купили VIP билет за 1200 сом.")
        else:
            print("\nВы купили Обычный билет за 500 сом.")
            
        print("Приятного просмотра!")



show = ZooShow()
show.start()