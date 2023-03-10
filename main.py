import csv
import datetime
with open("Menu.txt", "w") as file:
    file.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: Sade Pizza\n")
    file.write("* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n")
    file.write("* Teşekkür ederiz!")


class Pizza:
    def __init__(self, description, cost):
        self.__description = description
        self.__cost = cost

    def get_description(self):
        return self.__description

    def get_cost(self):
        return self.__cost


class ClassicPizza(Pizza):
    def __init__(self):
        description = "Klasik Pizza"
        cost = 25.0
        super().__init__(description, cost)


class MargheritaPizza(Pizza):
    def __init__(self):
        description = "Margarita Pizza"
        cost = 30.0
        super().__init__(description, cost)


class TurkishPizza(Pizza):
    def __init__(self):
        description = "Türk Pizza"
        cost = 28.0
        super().__init__(description, cost)


class DominosPizza(Pizza):
    def __init__(self):
        description = "Dominos Pizza"
        cost = 35.0
        super().__init__(description, cost)


class Decorator:
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        pass

    def get_cost(self):
        pass
class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
        self.cost = 2.0

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar"
        self.cost = 3.0

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri"
        self.cost = 4.0

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et"
        self.cost = 5.0

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğan"
        self.cost = 2.5

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mısır"
        self.cost = 2.5

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost
import csv

# Pizza seçenekleri ve fiyatları
PIZZA_OPTIONS = {
    "Margherita": 10.0,
    "Pepperoni": 12.0,
    "Vegetarian": 11.5,
    "Hawaiian": 13.5,
    "Meat Lovers": 14.5
}

# Sos seçenekleri ve sınıfları
SAUCE_OPTIONS = {
    "Zeytin": Zeytin,
    "Mantar": Mantar,
    "Keçi Peyniri": KeciPeyniri,
    "Et": Et,
    "Soğan": Sogan,
    "Mısır": Misir
}

def print_menu():
    print("PIZZA MENÜSÜ:")
    for pizza, price in PIZZA_OPTIONS.items():
        print(f"- {pizza}: {price} TL")
    print("\nSOS SEÇENEKLERİ:")
    for sauce in SAUCE_OPTIONS:
        print(f"- {sauce}")

def get_pizza_choice():
    choice = input("Lütfen bir pizza seçiniz: ")
    while choice not in PIZZA_OPTIONS:
        choice = input("Lütfen geçerli bir pizza seçeneği giriniz: ")
    return choice

def add_sauce(pizza):
    while True:
        choice = input("Eklemek istediğiniz sosun adını girin veya çıkmak için 'q' basın: ")
        if choice == 'q':
            break
        elif choice in SAUCE_OPTIONS:
            sauce_class = SAUCE_OPTIONS[choice]
            pizza = sauce_class(pizza)
        else:
            print("Geçerli bir sos seçeneği girin.")
    return pizza

def get_order_info():
    name = input("İsim: ")
    id_no = input("TC Kimlik Numarası: ")
    card_no = input("Kredi Kartı Numarası: ")
    cvv = input("Kredi Kartı CVV: ")
    return name, id_no, card_no, cvv

def write_order_to_database(order_info, pizza):
    name, id_no, card_no, cvv = order_info
    with open('Orders_Database.csv', mode='a', newline='') as order_file:
        writer = csv.writer(order_file)
        writer.writerow([name, id_no, card_no, pizza.get_description(), pizza.get_cost(), cvv])
    print("Sipariş kaydedildi.")

def main():
    print_menu()
    pizza_choice = get_pizza_choice()
    pizza = Pizza(pizza_choice, PIZZA_OPTIONS[pizza_choice])
    pizza = add_sauce(pizza)
    order_info = get_order_info()
    write_order_to_database(order_info, pizza)

if __name__ == "__main__":
    main()
