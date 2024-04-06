def celsius_to_fahrenheit(celsius):
    # Перевод из градусов Цельсия в градусы Фаренгейта
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    # Перевод из градусов Фаренгейта в градусы Цельсия
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    # Выбор типа конвертации
    conversion_type = input("Выберите тип конвертации (C2F для перевода из Цельсия в Фаренгейты, F2C для перевода из Фаренгейтов в Цельсии): ")
    
    while conversion_type not in ["C2F", "F2C"]:
        # Некорректный тип конвертации, требуется повторный ввод
        print("Ошибка! Некорректный тип конвертации.")
        conversion_type = input("Выберите тип конвертации (C2F для перевода из Цельсия в Фаренгейты, F2C для перевода из Фаренгейтов в Цельсии): ")
    
    # Ввод температуры
    temperature = float(input("Введите температуру: "))
    
    while temperature < -273.15:
        # Некорректное значение температуры, требуется повторный ввод
        print("Ошибка! Некорректное значение температуры.")
        temperature = float(input("Введите температуру: "))
    
    if conversion_type == "C2F":
        # Выполнение конвертации из Цельсия в Фаренгейты
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"{temperature} градусов Цельсия равно {converted_temperature} градусов Фаренгейта.")
    elif conversion_type == "F2C":
        # Выполнение конвертации из Фаренгейтов в Цельсии
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"{temperature} градусов Фаренгейта равно {converted_temperature} градусов Цельсия.")

if __name__ == '__main__':
    main()