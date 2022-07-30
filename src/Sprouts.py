#!/usr/bin/python3
class Sprouts():
  def __init__(self, N):
    self.board = [0] * N
    self.moves = []

  def __str__(self):
    """
    Function: __str__: @Override
    Override __str__ to print board state when called on instance of Sprouts object
    """
    s  = "Board:\n"
    nodes = ""
    conns = ""
    for i in range(len(self.board)):
      nodes += f"\t {i+1} "
      conns += f"\t[{self.board[i]}]"
    s += f"{nodes}\n{conns}\n"
    s += f"Moves:\t{self.moves}\n"
    return s

  def __moveIsValid(self, move):
    """
    Function: moveIsValid(move)
    @param  move: integer move array
    @return isValid: boolean validity of move given board state
    """
    start = move[0]
    end   = move[-1]
    maxNode = len(self.board)
    if start>maxNode or end>maxNode:
      return False
    elif self.board[start-1]>=3 or self.board[end-1]>=3:
      return False
    return True

  def move(self, move):
    """
    Function move(move):
    @param  move: integer move array
    @return isValid: boolean validity of move given board state
    """
    isValid = self.__moveIsValid(move)
    if not isValid:
      return isValid
    # Move is valid
    start = move[0]
    end   = move[-1]
    # Increment node counters
    self.board[start-1]+=1
    self.board[end-1]+=1
    self.board.append(2)
    # Append move to move array
    self.moves.append(move)
    return isValid

if __name__ == "__main__":
  s = Sprouts(4)
  print(s)
  while s.move([1,2]):
    print("=================")
    print(s)
