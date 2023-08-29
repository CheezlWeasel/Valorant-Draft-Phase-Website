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

  def __init__(self, admin, name, draft_type, series_type):
    global active_codes
    self.name = name  #string
    self.code = create_code(4, active_codes)
    self.admins = [admin]
    self.omega_team = Omega_team() #attackers (left side)
    self.Alpha_team = Alpha_team() #defenders (right side)
    self.agent_history = []
    self.map_history = []
    self.agent_draft = draft_type  #Boolean
    self.series_type = series_type  #string
    self.all_maps = True
    #series types are as follows,A  
    #A = Admin picks map  Bo1
    #R = random map pick  Bo1
    #BO1 = Players pick map Bo1
    #BO3 = Players pick map Bo3
    #BO5 = Players pick map Bo5

class Omega_team:

  def __init__(self):
    self.name = ''
    self.captain = '' 
    self.players = [] 
    self.coach = ''

class Alpha_team:

  def __init__(self):
    self.name = ''
    self.captain = '' 
    self.players = [] 
    self.coach = '' 

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
