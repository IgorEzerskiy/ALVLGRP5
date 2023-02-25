"""
В головному файлі програми (app.py або main.py) весь код, який знаходиться в блоці
if __name__ == ‘__main__’ перенести в нову функцію main() і викликати цю функцію в
name == main блоці.
Огорнути виклик функції main() в блок try/except.
У разі виникнення винятку EmailAlreadyExistsException
записати в файл logs.txt повідомлення у вигляді: %дата% %час% | %traceback%
"""
import csv
import datetime
import traceback


class EmailAlreadyExistsException(Exception):
    pass


"""
some_mail@mail.com\n
some_another_mail@mail.com\n
"""

"some_mail@mail.com"
"some_Mail@gmail.com"


class Employee:
    def __init__(self, name, last_name, date_of_birth,email):
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.validate()
        self.save_email()
        self._last_action = datetime.datetime.now()

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"

    @property
    def age(self):
        """
        calculate full years of employee
        :return:
        """

    @property
    def last_action(self):
        return self._last_action

    @last_action.setter
    def last_action(self, dt_obj):
        self._last_action = dt_obj

    def save_email(self):
        with open('emails.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'email'])
            writer.writeheader()
            writer.writerow({"name": self.name, "email": self.email})

    def validate(self):
        with open('emails.csv') as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=['name', 'email'])
            if self.email.strip() in (x['email'] for x in reader):
                raise EmailAlreadyExistsException


def main():
    emp1 = Employee('alex', 'mercer', 'alex@mail.com')
    print(emp1.full_name)



if __name__ == '__main__':
    try:
        main()
    except Exception:
        a = traceback.format_exc()
        print(a)
