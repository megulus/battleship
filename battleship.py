class Ocean(object):
  def __init__(self, x, y, ship_locations):
    pass
    # an ocean - i.e. a game board - is a 2D coordinate plane of length x and height y
    # constructor - take a list of ship locations
    # ocean methods
    # - return an array of ShipLocations
    # - strike(coordinate) - return hit, miss or sink - check whether coordinate is occupied by a ship. 
    #   If so, which ship? Call strike() method on the position of the ship occupying the coordinate and determine whether the hit sinks the ship

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
    
    # ship properties:
    # - length
    # * ship does NOT know its location
    # ship methods:
    # - is_sunk() - looks at each of its positions, returns true if all have been hit, false otherwise 
    # - strike(int position) - called by Ocean? In this scenario, player will hit coordinates in an ocean, and the ocean will 
    #   call this method (if coordinate occupied by a ship) on the position of ship in that ocean coordinate

class ShipLocation(object):
  def __init__(self, ship, x, y, orientation):
    pass
    
    # create an instance of ShipLocation with an instance of Ship at location (x, y) and orientation 'H' or 'V'
    # a ship location can
    # - return a location (start coordinate, orientation)
    # - return a ship

SHIP_LOCATIONS = [
  # ShipLocation(Ship(3), 0, 0, 'H'),
  # ...  
]

if __name__ == "__main__":
    pass