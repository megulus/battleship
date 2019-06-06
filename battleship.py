class Ocean(object):
  def __init__(self, x, y, ship_locations):
    self.ocean = [[{ 'ship': None, 'position': None } for i in range(x)] for j in range(y)]
    self.ship_locations = ship_locations
    for location in ship_locations:
      ship = location.ship
      length = ship.length
      orientation = location.orientation
      x = location.x
      y = location.y
      self.ocean[x][y]['ship'] = ship
      self.ocean[x][y]['position'] = 0
      for i in range(1, length):
        if orientation == 'H':
          self.ocean[x + i][y]['ship'] = ship
          self.ocean[x + i][y]['position'] = i
        if orientation == 'V':
          self.ocean[x][y + i]['ship'] = ship
          self.ocean[x][y + i]['position'] = i

  def strike(self, x, y):
    coordinate = self.ocean[x][y]
    if coordinate['ship']:
      ship = coordinate['ship']
      position = coordinate['position']
      ship.strike(position)
      if ship.is_sunk():
        return 'SUNK!'
      else:
        return 'HIT!'
    return 'MISS'

class Ship(object):
  def __init__(self, length):
    self.length = length
    self.__positions = [False] * length

  def is_sunk(self):
    for pos in self.__positions:
      if pos == False:
        return False
    return True

  def strike(self, position):
    self.__positions[position] = True
    
class ShipLocation(object):
  def __init__(self, ship, x, y, orientation):
    self.ship = ship
    self.x = x
    self.y = y
    self.orientation = orientation

SHIP_LOCATIONS = [
  ShipLocation(Ship(3), 0, 0, 'H'),
  ShipLocation(Ship(2), 3, 2, 'V')
]
OCEAN = Ocean(5, 5, SHIP_LOCATIONS)

def main():
  print('OCEAN.strike(3, 0)', OCEAN.strike(3, 0))
  print('OCEAN.strike(2, 0)', OCEAN.strike(2, 0))
  print('OCEAN.strike(3, 3)', OCEAN.strike(3, 3))
  print('OCEAN.strike(3, 2)', OCEAN.strike(3, 2))

if __name__ == "__main__":
  main()
