from typing import List
from .elevator import Elevator


class Building:

    def __init__(self, stories: int):
        self.stories = stories + 1
        self.elevators = []

    def add_elevators(self, elevators):
        for elevator in elevators:
            lift = Elevator(name=elevator['name'],
                            description=elevator['description'],
                            stories=self.stories,
                            position=elevator['position'],
                            weight=elevator['weight'],
                            use_keycard=elevator['use_keycard'])
            
            self.elevators.append(lift)

    def request(self, **kwargs):
        for elevator in self.elevators:
            if elevator.name in kwargs:
                elevator.request(kwargs[elevator.name])

    def run_request(self):
        for elevator in self.elevators:
            elevator.run_request()