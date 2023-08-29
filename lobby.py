import string
import random

active_codes = []


def create_code(length, active_codes):
  characters = string.ascii_uppercase + string.digits
  code = ''.join(random.choice(characters) for i in range(length))
  print(random.choice(characters))
  while code in active_codes:
    code = ''.join(random.choice(characters) for i in range(length))
  active_codes.append(code)
  return code


class Lobby:

  def __init__(self, admin, name, draft_type, map_type):
    global active_codes
    self.name = name  #string
    self.code = create_code(4, active_codes)
    self.players = []
    self.admins = [admin]
    self.captains = []
    self.coaches = []
    self.team_names = ['', '']  #team 1 is attack, team 2 is defence
    self.agent_history = []
    self.map_history = []
    self.agent_draft = draft_type  #Boolean
    self.map_type = map_type  #integer
    self.all_maps = True
    #map types are as follows,
    #0 = Admin picks map Bo1
    #1 = Players pick map Bo1
    #2 = Players pick map Bo3
    #3 = Players pick map Bo5

  def undo_agent(self):
    if self.agent_history[0] != 0:
      del self.agent_history[-1]
    else:
      print('undo failed')
    if len(self.agent_history) == 0:
      self.agent_history = [0]

  def undo_map(self):
    if self.map_history[0] != 0:
      del self.map_history[-1]
    else:
      print('undo failed')
    if len(self.map_history) == 0:
      self.map_history = [0]
