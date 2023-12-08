def cheking_values(filename, check):

    with open(filename, 'r') as file:
        lines = file.readlines()
        a = 0
        for line in lines:
            values = line.split()
            if len(values) == 2:
                time, value = values
                if float(value) > float(check):
                    print(f"Час: {time}, Значення: {value}")
                    a =+ 1
        if a == 0:
            print("Значення не знайдено. Перевірте, що ви ввели все вірно.")
            print("Введіть значення ААА(наприклад: 124)")
        print(" ")
while True:
    print("Введіть значення ААА(наприклад: 124)")
    check_value = input("Введіть значення AAA або (q) щоб вийти: ")
    if check_value == "q":
        print("Дякуюємо за використання, повертайтесь ще!")
        break
    cheking_values("Value.txt", check_value)
