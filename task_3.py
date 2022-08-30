number = int(input("Введіть будь ласка, трьох значне, позитивне або негативне ціле число: "))
sign = "позитивним" if number > 0 else "негативним"
if number == 0:
    print("Число 0")
elif len(str(abs(number))) == 1:
    print(f"Ви ввели число {number}, яке є {sign}, і складається з 1 цифри")
elif len(str(abs(number))) == 2:
    print(f"Ви ввели число {number}, яке є {sign}, і складається з 2 цифр")
elif len(str(abs(number))) == 3:
    print(f"Ви ввели число {number}, яке є {sign}, і складається з 3 цифр")
else:
    print(f"Ви ввели число {number}, яке є задовгим числом")
