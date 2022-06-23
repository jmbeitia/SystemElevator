import random

class Keycard:
    def __init__(self):
        self.__serial_number = self.generate_SN()
        

    def generate_SN(self):
        serial_number = random.randrange(10**5, 10**6, 1)
        print('The serial number is', serial_number)
        return serial_number

    def get_SN(self):
        return self.__serial_number


class Person:
    def __init__(self, name: str, weight: float, additional_weight: float):
        self.name = name
        self.weight = weight
        self.additional_weight = additional_weight
        self.keycard = None

    def get_total_weight(self):
        return self.weight + self.additional_weight

    def obtain_keycard(self):
        self.keycard = Keycard()

    def __str__(self):
        response = 'Name: {}, Weight: {} and Additional weight: {}'.format(self.name, self.weight, self.additional_weight)
        return response
    def __repr__(self):
        return str((self.name, self.weight, self.additional_weight))
