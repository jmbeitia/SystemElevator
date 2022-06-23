def run_request(self):

    N = 100
    print('-'*N)
    print('*'*10, self.description, '*'*10)
    print('Stories requested:', self.stories_requested)

    stories_requested_up, stories_requested_down = self.directions_requested()
    self.get_minimal_direction(stories_requested_up, stories_requested_down)

    if self.position in self.stories_requested:
        self.door_sequence()
        self.stories_requested.remove(self.position)

    for _ in range(2):

        if self.direction_up and len(stories_requested_up) > 0:
            print('Direction up', '_'*20)
            print('Going to {} stories and is on {} storie'.format(stories_requested_up, self.position))
            self.go_to_stories(stories_requested_up)

        elif not self.direction_up and len(stories_requested_down) > 0:
            print('Direction down', '_'*20)
            print('Going to {} stories and is on {} storie'.format(stories_requested_down, self.position))
            self.go_to_stories(stories_requested_down)

        self.direction_up = not self.direction_up

def request(self, stories_requested):

    for storie in list(set(stories_requested)):
        if not storie in self.stories_requested:
            self.stories_requested.append(storie)

def directions_requested(self):

    self.stories_requested.sort()
    
    stories_requested_up = [storie for storie in self.stories_requested if storie > self.position]
    stories_requested_down = [storie for storie in self.stories_requested if storie < self.position]        
    stories_requested_down.sort(reverse=True)

    return stories_requested_up, stories_requested_down

def get_minimal_direction(self, stories_requested_up, stories_requested_down):

    if len(stories_requested_up) > 0:
        distance_up = abs(stories_requested_up[0] - self.position)
    else:
        distance_up = 0

    if len(stories_requested_down) > 0:
        distance_down = abs(stories_requested_down[0] - self.position)
    else:
        distance_down = 0

    if distance_up <= distance_down:
        self.direction_up = True
    else:
        self.direction_up = False