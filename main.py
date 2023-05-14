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
