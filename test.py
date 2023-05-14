from unittest import TestCase, main
from main import *
import os


class ProgramTest(TestCase):
    def test_name_correcting(self):
        self.assertEqual(correct_name('илья'), 'Илья')
        self.assertEqual(correct_name('Василий'), 'Василий')
        self.assertEqual(correct_name('Hello'), EMPTY_TEXT)
        self.assertEqual(correct_name('123федя123'), 'Федя')
        self.assertEqual(correct_name('89463765473'), EMPTY_TEXT)

    def test_age_correcting(self):
        self.assertEqual(correct_age('123'), '123')
        self.assertEqual(correct_age('Мне 50 лет'), '50')
        self.assertEqual(correct_age('Не знаю'), EMPTY_TEXT)
        self.assertEqual(correct_age(''), EMPTY_TEXT)

    def test_phone_correcting(self):
        self.assertEqual(correct_phone('87654321098'), '+7 (765) 432-10-98')
        self.assertEqual(correct_phone('12345678901'), EMPTY_TEXT)
        self.assertEqual(correct_phone('+8(111)111-1-1-1-1'), '+7 (111) 111-11-11')
        self.assertEqual(correct_phone('Нет телефона'), EMPTY_TEXT)

    def test_email_correcting(self):
        self.assertEqual(correct_email('hello@mail.ru'), 'hello@mail.ru')
        self.assertEqual(correct_email('hello-world@mail...ru'), 'hello-world@mail.ru')
        self.assertEqual(correct_email('hello@@@@mail..ru'), 'hello@mail.ru')
        self.assertEqual(correct_email('hello@mail@google.com'), EMPTY_TEXT)

    def test_opening(self):
        test_path = 'test_opening.txt'
        test_content = 'test'
        with open(test_path, 'w', encoding='utf-8') as file:
            file.write(test_content)
        self.assertEqual(open_input(test_path), [test_content])
        os.remove(test_path)

    def test_len_fields(self):
        test_content = 'Сидоров 17 +78478558260 donec@icloud.com'
        expected = 'Некорректная строка\n'
        self.assertEqual(correct_all([test_content]), expected)

    def test_correcting_one_line(self):
        test_query = ['1Игорь1|Мне 50 лет|+8(111)111-1-1-1-1|hello-world@mail...ru']
        expected = 'Игорь|50|+7 (111) 111-11-11|hello-world@mail.ru\n'
        self.assertEqual(correct_all(test_query), expected)

    def test_correcting_some_lines(self):
        test_query = ['василий|10|83452654674|abc@abc.ru',
                      '-ВАНЯ-|пять|8345267|van@@@mail.ru',
                      '1|1|1|1']
        expected = 'Василий|10|+7 (345) 265-46-74|abc@abc.ru\n' +\
                   f'Ваня|{EMPTY_TEXT}|{EMPTY_TEXT}|van@mail.ru\n' +\
                   f'{EMPTY_TEXT}|1|{EMPTY_TEXT}|{EMPTY_TEXT}\n'
        self.assertEqual(correct_all(test_query), expected)

    def test_save_file(self):
        test_path = 'test_saving.txt'
        test_content = 'test'
        save_result(test_content, test_path)
        with open(test_path, 'r', encoding='utf-8') as file:
            from_file = file.read()
        self.assertEqual(from_file, test_content)
        os.remove(test_path)


if __name__ == '__main__':
    main()
