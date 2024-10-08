class Coffee:
    def __init__(self, type_coffee, with_sugar=False, syrup=None):
        self.type_coffee = type_coffee
        self.with_sugar = with_sugar
        self.syrup = syrup

    def __str__(self):
        sugar_str = "с сахаром" if self.with_sugar else "без сахара"
        syrup_str = f"сиропом {self.syrup}" if self.syrup else "без сиропа"
        return f"{self.type_coffee} ({sugar_str}, {syrup_str})"


def main():
    coffee_options = {
        1: "Капучино",
        2: "Латте",
        3: "Эспрессо"
    }

    print("Выберите кофе:")
    for key, value in coffee_options.items():
        print(f"{key}. {value}")

    choice = int(input("Введите номер кофе: "))
    if choice not in coffee_options:
        print("Неверный выбор. Попробуйте снова.")
        return

    type_coffee = coffee_options[choice]

    sugar_options = ["да", "нет"]
    sugar_choice = input("Хотите сахар? (да/нет): ").strip().lower()
    if sugar_choice not in sugar_options:
        print("Неверный выбор. Попробуйте снова.")
        return

    with_sugar = sugar_choice == "да"

    syrup_options = ["Карамель", "Шоколад", "Ваниль"]
    print("Выберите сироп или введите '0' для отказа:")
    for i, syrup in enumerate(syrup_options, start=1):
        print(f"{i}. {syrup}")
    print("0. Нет сиропа")

    syrup_choice = int(input("Введите номер сиропа: "))
    syrup = None
    if syrup_choice in range(1, len(syrup_options) + 1):
        syrup = syrup_options[syrup_choice - 1]
    elif syrup_choice != 0:
        print("Неверный выбор. Попробуйте снова.")
        return

    coffee = Coffee(type_coffee, with_sugar, syrup)

    print(f"Ваш заказ: {coffee}")


if __name__ == "__main__":
    main()
