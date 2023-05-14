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
