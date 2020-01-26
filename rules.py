def check(pieces, firsttap, from_x, from_y, to_x, to_y):

  # pawn_rules

  final_pos = pieces[to_x][to_y]
  first_char = final_pos[0]
  if(firsttap == "wp" and first_char != "w"):
    if(to_y != from_y and pieces[to_x][to_y] == "-"):
        return False
    if(from_x == 6):
      if(to_x==4 and to_y == from_y):
        return True
    if (to_x == (from_x - 1) and (abs(to_y - from_y) == 0 or abs(to_y - from_y) == 1 )):
        return True
  if (firsttap == "bp" and first_char != "b" ):
    if (to_y != from_y and pieces[to_x][to_y] == "-"):
      return False
    if (from_x == 1):
      if (to_x == 3 and to_y == from_y):
        return True
    if (to_x == (from_x + 1) and (abs(to_y - from_y) == 0 or abs(to_y - from_y) == 1 )):
        return True
  return False
