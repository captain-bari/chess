def check(pieces, firsttap, from_x, from_y, to_x, to_y):

 #Universal False
  final_pos = pieces[to_x][to_y]
  first_char = final_pos[0]

  if(firsttap[0] == first_char):
    return False






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
      
   #bishop_rules


  if(firsttap == "wb" and ( abs(to_x - from_x) == abs(to_y - from_y))):
    for i, j in zip(range(from_x+1,8),range(from_y+1,8)):
      curr_pos = pieces[i][j]
      first_charcurr = curr_pos[0]
      if (first_charcurr == "w"):
        break
      if( (to_x == i and to_y == j) and first_charfinal != "w" ):
        return True
    for i, j in zip(range(from_x-1,-1,-1),range(from_y-1,-1,-1)):
      curr_pos = pieces[i][j]
      first_charcurr = curr_pos[0]
      if (first_charcurr == "w"):
        break
      if ((to_x == i and to_y == j) and first_charfinal != "w"):
        return True
    for i, j in zip( range(from_x + 1,8),range(from_y - 1,-1,-1) ):
      curr_pos = pieces[i][j]
      first_charcurr = curr_pos[0]
      if (first_charcurr == "w"):
        break
      if ((to_x == i and to_y == j) and first_charfinal != "w"):
        return True
    for i, j in zip( range(from_x - 1, -1, -1), range(from_y + 1, 8) ):
      curr_pos = pieces[i][j]
      first_charcurr = curr_pos[0]
      if (first_charcurr == "w"):
        break
      if ((to_x == i and to_y == j) and first_charfinal != "w"):
        return True
       
       
       
       
        # rook rules

  if firsttap == "wr" or firsttap == "br":
    if from_x == to_x:
      if from_y>to_y:
        for i in range(to_y+1 , from_y):
          if pieces[from_x][i] != "-":
            return False
        return True

      if from_y < to_y:
        for i in range(from_y + 1, to_y ):
          if pieces[from_x][i] != "-":
            return False
        return True

    if from_y == to_y:
      if from_x>to_x:
        for i in range(to_x+1 , from_x):
          if pieces[i][from_y] != "-":
            return False
        return True
      if from_x < to_x:
        for i in range(from_x + 1, to_x):
          if pieces[i][from_y] != "-":
            return False
        return True
  
  
  
  #Universal return False
  return False
