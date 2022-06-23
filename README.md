# Elevator System - Python

# Solution:

- Console program for simulate an elevator

- A building that has to be initialized with the number of `stories`.

- Then the necessary elevators must be added with the `name`, `description`, maximum `weight` of load, initial `position`, and if it `use_keycard`.

- It is passed a dictionary, each for elevator, of the sotories requested.

- Input can be edited in `./main.py`.

- Each elevator has below capabilites :
    -  Move up and down
    -  Open and close door
    -  Exchange people into the elevator
    -  Keycard could be requested in the elevator before it moves
    -  Inform current position
    -  Alarm of overload
    -  Autodetect the optimal direction

- Keycards are created to a person

# How to Run:

1. [OPTIONAL] - Create and activate a python3 virtualenv.

2. It does not require specific modules, but a `requirements.txt` is provided for a virtual enviroment:

    `pip install -r requirements.txt`

3. [OPTIONAL] - Change the inputs in `./main.py`

4. `python main.py`


# Imporvements:

1. Error handling could be improved.

2. Take input from user or a config file rather than hardcoding it.

3. Add buttons to the elevator system to input new stories.

4. Add unit test scripts

5. It could be added a timer to automatically close the elevator door

# Test Input Details :

1. Building of `stories = 50`.

2. List of elevatros:
    - Public Elevator:
        - `name: 'public_elevator'`
        - `description: 'Public elevator'`
        - `weight: 1000`
        - `position: 24`
        - `use_keycard: True`
    - Freight Elevator:
        - `name: 'freight_elevator'`
        - `description: 'Freight elevator'`
        - `weight: 3000`
        - `position: 25`
        - `use_keycard: False`
     
3. List of stories requested:
    - `"public_elevator": [5, 45, 35, 15, 24, 37]`
    - `"freight_elevator": [45, 35, 13, 4, 53]`
