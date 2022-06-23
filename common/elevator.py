import random
from common.person import Keycard, Person
import time
import sys


class Elevator:
    def __init__(self, name: str, description: str, stories: int, position: int, weight: float, use_keycard: bool):
        """
        The elevator has allways a button in every storie
        """
        self.name = name
        self.description = description
        self.stories = stories
        self.position = position
        self.weight = weight
        self.use_keycard = use_keycard
        self.alarm = False
        self.state = 0
        self.direction_up = True
        self.valid_codes = list(range(10**5, 10**6))[::2]
        self.stories_requested = []
        self.people = []

    

    def text_state(self):
        if self.state == 0:
            return 'stoped'
        if self.state == 1:
            return 'going up'
        if self.state == 2:
            return 'going down'

    def get_state(self):
        print('Storie {} {}'.format(self.position, self.text_state()))
        return self.state

    def stop(self):
        self.state = 0

    def go_up(self):
        self.state = 1
        print(self.position, end=' ', flush=True)
        time.sleep(0.5)
        self.position += 1

    def go_down(self):
        self.state = 2
        print(self.position, end=' ', flush=True)
        time.sleep(0.5)
        self.position -= 1

    def door(self, action = 'Open'):
        if action == 'Open':
            print('Door opening on storie {}'.format(self.position))
            time.sleep(2)
        elif action == 'Close':
            print('Door closing on storie {}'.format(self.position))
            time.sleep(2)

    def balance(self):
        print('Checking the load of the {}: '.format(self.description.lower()), end= '')
        load = 0
        for person in self.people:
            load += person.weight + person.additional_weight
        
        print('{} kg'.format(load))
        if load > self.weight:
            self.alarm = True
            print('Maximum load reached {}'.format(self.weight))
        else:
            self.alarm = False
   
    def check_keycard_serial_number(self):
        
        print('Checking before move')
        isvalid = False
        while not isvalid:
            for person in self.people:
                if person.keycard:
                    if person.keycard.get_SN() in self.valid_codes:
                        isvalid = True
            
            if not isvalid:
                print("There are not valid keycard")
                self.door_sequence()

    def peeople_exchange(self):
        
        while True:
            self.menu()
            self.balance()
            
            if not self.alarm:
                break

    def door_sequence(self):

        self.door('Open')
        self.peeople_exchange()
        self.door('Close')

    def go_to_stories(self, stories):
        for storie in stories:
                if self.state == 0:
                    self.move(storie)
                    self.door_sequence()

    def move(self, storie: int):
    
        if self.use_keycard:
            self.check_keycard_serial_number()

        print('* Moving to storie: {}'.format(storie))
        print('Storie ', end='')
        while self.position != storie:
            if self.direction_up:
                self.go_up()
            else:
                self.go_down()
        print()

        self.state = 0
        self.get_state()
            
        self.stories_requested.remove(storie)

    from common.request import run_request, request, directions_requested, get_minimal_direction
    from common.options import validate, insert_name, get_weight, list_people, validate_option, menu