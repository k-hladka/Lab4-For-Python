from Person import Person


def modifier(filename):
    with open(filename, 'r+', newline='') as file:
        findex = 0
        length = 0
        nickname = 'nickname'
        for line in file:
            match findex:
                case 0:
                    surname = line.strip()
                    length += len(surname)
                case 1:
                    first_name = line
                    length += len(first_name)
                case 2:
                    birth_date = line
                case 3:
                    nickname = line
            findex += 1

        person = Person(surname, first_name, birth_date, nickname)
        file.seek(length)
        nickname = '' if nickname == 'nickname' else nickname
        file.write('\n' + person.get_fullname() + birth_date + nickname + '\n' + person.get_age())


if __name__ == "__main__":
    modifier('file.txt')
