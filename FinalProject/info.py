from datetime import datetime as dt
import re
#from abc import ABC, abstractmethod


class Record:

    def __init__(self, name, phones='', birthday='', email='', status='', note=''):

        self.birthday = birthday
        self.name = name
        self.phones = phones
        self.email = email
        self.status = status
        self.note = note

    def days_to_birthday(self):
        current_datetime = dt.now()
        self.birthday = self.birthday.replace(year=current_datetime.year)
        if self.birthday >= current_datetime:
            result = self.birthday - current_datetime
        else:
            self.birthday = self.birthday.replace(year=current_datetime.year + 1)
            result = self.birthday - current_datetime
        return result.days


class Field():

    #@abstractmethod
    def __getitem__(self):
        pass


class Name(Field):
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value


class Phone(Field):

    def __init__(self, value=''):
        while True:
            self.value = []
            if value:
                self.values = value
            else:
                self.values = input("Phones(+12digits) (Введіть номер телефона + і дванадцять цифр): ")
            try:
                for number in self.values.split(' '):
                    if re.match('^\+\d{12}$', number) or number == '':
                        result = f"{number[0]}{number[1]}{number[2]}{number[3]}({number[4]}{number[5]}){number[6]}{number[7]}{number[8]}-{number[9]}{number[10]}-{number[11]}{number[12]}"
                    # if re.match('^\+48\d{9}$', number) or re.match('^\\+38\d{10}$', number) or number == '':
                        self.value.append(result)
                    else:
                        raise ValueError
            except ValueError:
                print('Incorrect phone number format! Please provide correct phone number format.')
            else:
                break

    def __getitem__(self):
        return self.value


class Birthday(Field):

    def __init__(self, value=''):
        while True:
            if value:
                self.value = value
            else:
                self.value = input("Birthday date(dd/mm/YYYY): ")
            try:
                if re.match('^\d{2}/\d{2}/\d{4}$', self.value):
                    self.value = dt.strptime(self.value.strip(), "%d/%m/%Y")
                    break
                elif self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect date! Please provide correct date format.')

    def __getitem__(self):
        return self.value


class Email(Field):

    def __init__(self, value=''):
        while True:

            if value:
                self.value = value
            else:
                self.value = input("Email: ")
            try:
                #if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', self.value) or self.value == '':
                if re.match ("^[-a-z0-9!#$%&'*+/=?^_`{|}~]+(?:\.[-a-z0-9!#$%&'*+/=?^_`{|}~]+)*@(?:[a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?\.)*(?:aero|arpa|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|[a-z][a-z])$", self.value) or self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect email! Please provide correct email.')

    def __getitem__(self):
        return self.value


class Status(Field):

    def __init__(self, value=''):
        while True:
            self.status_types = ['', 'family', 'friend', 'work']
            if value:
                self.value = value
            else:
                self.value = input("Type of relationship (family, friend, work): ")
            try:
                if self.value in self.status_types:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('There is no such status!')

    def __getitem__(self):
        return self.value


class Note(Field):
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value
