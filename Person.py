from datetime import datetime


class Person:
    def __init__(self, surname, first_name, birth_date, nickname='nickname'):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        self.birth_date = datetime(self.__create_date(birth_date, 0), self.__create_date(birth_date, 1),
                                   self.__create_date(birth_date, 2))

    def get_age(self):
        return str(int((datetime.now() - self.birth_date).days / 365))

    def get_fullname(self):
        return self.surname + " " + self.first_name

    def __create_date(self, string_date, index):
        return int(string_date.split('-')[index])


if __name__ == '__main__':
    person = Person("Іванов", "Іван", "2001-12-20")
    print(person.get_age())
    print(person.get_fullname())
