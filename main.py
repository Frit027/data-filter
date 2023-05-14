import re


EMPTY_TEXT = ' - '


# Функция для исправления фамилии (первого поля)
def correct_name(query):
    # Для его корректировки нужно удалить все символы кроме
    # русских букв, а затем выполнить функцию capitalize(),
    # Примеры:
    # Было: '->юров123<-',    стало: 'Юров'
    # Было: '-=**hello**=-',  стало: ' - '

    corrected = re.sub(r'[^а-яА-Я]+', '', query)
    if len(corrected) > 0:
        return corrected.capitalize()
    else:
        return EMPTY_TEXT


# Функция для исправления возраста (второго поля)
def correct_age(query):
    # Удаляем из строки все, что не является цифрами,
    # Примеры:
    # Было: '4xy5a', стало: '45'
    # Было: 'abc',   стало: ' - '

    corrected = re.sub(r'\D+', '', query)
    if len(corrected) > 0:
        return corrected
    else:
        return EMPTY_TEXT


# Функция для исправления номера телефона (третьего поля)
def correct_phone(query):
    # Удаляем все символы кроме цифр и смотрим, сколько получилось цифр в итоге.
    # В номере телефона их должно быть 11, при этом первая из них должна быть либо 7, либо 8.
    # Если цифр меньше или больше 11, либо если первая из них не 7 или 8, то номер
    # можно считать некорректным, поэтому возвращаем пустую строку.
    # Примеры:
    # Было: '85674x3y65267', стало: '+7 (567) 436-52-67'
    # Было: '123456',        стало: ' - '

    corrected = re.sub(r'\D+', '', query)
    if len(corrected) == 11 and corrected[0] in '78':
        part1 = corrected[1:4]
        part2 = corrected[4:7]
        part3 = corrected[7:9]
        part4 = corrected[9:11]
        return f'+7 ({part1}) {part2}-{part3}-{part4}'
    else:
        return EMPTY_TEXT


if __name__ == '__main__':
    with open('input.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('output.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            line_content = line.rstrip().split('|')
            if len(line_content) != 4:
                file.write('Некорректная строка\n')
                continue
            name, age, phone, email = line_content
