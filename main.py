from common.elevator import Elevator
from common.building import Building
from common.person import Keycard, Person

def main():

    stories = 50

    elevators = [{'name': 'public_elevator',
                  'description': 'Public elevator',
                  'weight': 1000,
                  'position': 24,
                  'use_keycard': True
                  },
                 {'name': 'freight_elevator',
                  'description': 'Freight elevator',
                  'weight': 3000,
                  'position': 25,
                  'use_keycard': False
                  }]

    building = Building(stories=stories)

    building.add_elevators(elevators)

    stories_request = {
        "public_elevator": [5, 45, 35, 15, 24, 37],
        "freight_elevator": [45, 35, 13, 4, 53]
    }
    building.request(**stories_request)
    building.run_request()


if __name__ == '__main__':

    main()
