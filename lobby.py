import string
import random

active_codes = ['']

def create_code(length, active_codes):
    code = ''
    characters = string.ascii_uppercase + string.digits
    print(random.choice(characters))
    while code in active_codes:
        code = ''.join(random.choice(characters) for i in range(length))
    active_codes.append(code)
    return code


class Lobby:
    def __init__(self, admin):
        global active_codes
        self.code = create_code(4, active_codes)
        self.approve_required = False
        self.players = []
        self.admins = [admin]
        self.agent_history = []
        self.map_history = []
        self.agent_draft = False
        self.map_type = 0
        #map types are as follows, 
        #0 = Admin picks map Bo1
        #1 = Players pick map Bo1
        #2 = Players pick map Bo3
        #3 = Players pick map Bo5