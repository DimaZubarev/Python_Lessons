""""
number = int(input("Ведіть число, будь ласка: "))
if number % 2:
    print(f"{number}  не парне число")
else:
    print(f"{number} парне число")
"""
# тенарний оператор, коли if та else пишуться в один рядок, це не гарна практика
number = int(input("Ведіть число, будь ласка: "))
print(f"{number} не парне") if number % 2 else print(f"{number} парне число")
