from common.person import Person

def validate(self, text):
    if text in ['y', 'n']:
        return text
    else:
        print('Error. Try again')


def insert_name(self):

    response = ''
    while response == '':
        response = input('Name: ')
        if response == '':
            print('Try again')

    return response


def get_weight(self, text):

    while True:
        response = input('{} weight: '.format(text))
        try:
            response = float(response)
            break
        except:
            print('Error, try again')
    return response

def list_people(self):
    if self.people:
        for index, person in enumerate(self.people):
            print(index + 1, ")", person)
        return True
    else:
        print('Empty elevator')
        return False

def validate_option(self, list_options):
    
    while True:
        option = input('Choose one number: ')
        if option in list_options:
            option = int(option)
            break
        else:
            print('Try again')
    
    return option
        

def menu(self):

    response = None
    while response not in ['y', 'n']:
        response = input('Wish to enter o leave person? [y]/n: ') or 'y'
        response = self.validate(response)

    if response == 'y':
        while True:
            print(
            '''
            Menu:
             1. Enter person
             2. Leave people
             3. List people
             4. Exit
            '''.replace('   ', ''))
            option = self.validate_option(['1', '2', '3', '4'])

            if option == 1:
                name = self.insert_name()
                weight = self.get_weight('Person')
                additional_weight = self.get_weight('Additional')

                person = Person(name, weight, additional_weight)
                response = input('Generate keycard? [y]/n: ') or 'y'
                response = self.validate(response)
                if response == 'y':
                    person.obtain_keycard()

                print(person)
                self.people.append(person)

            
            elif option == 2:

                result = self.list_people()
                if result:
                    print('Choose wich person leaves. Cero to go back')
                    options = list(map(str, range(1,len(self.people)+1)))
                    options.append('0')
                    response = self.validate_option(options)
                    if response != 0:
                        del self.people[response - 1]

            
            elif option == 3:
                self.list_people()
            
            elif option == 4:
                break


    elif response == 'n':
        pass