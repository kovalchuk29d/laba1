# Лабораторна робота №1. Основи Python
# Варіант: _1_ 
# ПІБ: Ковальчук Діана

while True:
    try:
        length = float(input("Введіть довжину прямокутника (см): ")) 
        width = float(input("Введіть ширину прямокутника (см): "))
        if length <= 0 or width <= 0:
            raise ValueError("Довжина та ширина повинні бути додатними числами.")
        break
    except ValueError as e:
        print(f"Помилка: {e} Спробуйте ще раз.")

# Обчислення площі та периметру
area = length * width
perimeter = 2 * (length + width)

# Виведення результатів
print("\nРезультати обчислень:")
print(f"Площа прямокутника: {area:.2f} см²")
print(f"Периметр прямокутника: {perimeter:.2f} см")

