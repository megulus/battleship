# Battleship

**Game Overview**

Battleship is a game played on a board with n x m holes placed in a grid pattern. Players place model ships of different lengths in the holes in horizonal or vertical orientation. Players take turns guessing grid positions (e.g., 'B8'). If the position is occupied by a ship, that position on the grid is hit. Otherwise, the shot is a miss. Once all of the positions of the ship have been hit, the ship is sunk.

**Project Motivation**

I'm trying to improve my fundamentals in data structures and procedural decomposition. I thought that this problem represented some fun challenges in both areas.

**Code Overview**

The game currently has 3 classes - Ocean, Ship and ShipLocation. Currently, it can simulate the basic game action, i.e., striking a location in the Ocean and receiving feedback on whether that strike constitutes a miss, hit or sink(ing) of a Ship.

**Next Steps**

1. *Validation and Error handling.* The constructors and methods currently assume good data inputs. E.g., the Ocean constructor assumes that the array of ShipLocations contains valid ShipLocations (non-clashing, fully contained on board), and both strike() methods assume a valid Ocean coordinate and Ship position argument (respectively). 

2. *Unit testing.* I'd like to use this project as a chance to practice writing unit tests.

3. *Build game player.* Build a proper interactive 1-player game, where the player can input coordinates and receive feedback (miss, hit, sink, invalid coordinate?).

4. *Randomize ShipLocations.* Currently, the ShipLocations are hard-coded. I would like to randomize these with each new Ocean instantiation. The difficulty here is in making sure the locations 1) keep the ships fully on the board and 2) do not clash with any other ships.