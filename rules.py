def check(pieces, firsttap, from_x, from_y, to_x, to_y):

 #Universal False
  final_pos = pieces[to_x][to_y]
  first_char = final_pos[0]

  if(firsttap[0] == first_char):
    return False






# pawn_rules

  final_pos = pieces[to_x][to_y]
  first_char = final_pos[0]
  if (firsttap == "wp" and first_char != "w"):
      if (to_y != from_y and pieces[to_x][to_y] == "-"):
          return False
      if (from_x == 6):
          if (to_x == 4 and to_y == from_y):
              return True
      if (to_x == (from_x - 1) and ( abs(to_y - from_y) == 0)and pieces[to_x][to_y]=="-"):
          return True
      if (to_x == (from_x - 1) and (abs(to_y - from_y) == 1)):
          return True
  if (firsttap == "bp" and first_char != "b"):
      if (to_y != from_y and pieces[to_x][to_y] == "-"):
          return False
      if (from_x == 1):
          if (to_x == 3 and to_y == from_y):
              return True
      if (to_x == (from_x + 1) and ( abs(to_y - from_y) == 0)and pieces[to_x][to_y]=="-"):
          return True
      if (to_x == (from_x + 1) and ( abs(to_y - from_y) == 1)):
          return True

   #bishop_rules


  if((firsttap == "wb" or firsttap == "bb") and ( abs(to_x - from_x) == abs(to_y - from_y))):
    for i, j in zip(range(from_x+1,8),range(from_y+1,8)):
      curr_pos = pieces[i][j]
      first_charcurr = curr_pos[0]
      if ((to_x == i and to_y == j)):
        return True
      if (first_charcurr == "w" or first_charcurr == "b"):
        break

    for i, j in zip(range(from_x-1,to_x-1,-1),range(from_y-1,to_y-1,-1)):
      curr_pos = pieces[i][j]
      first_charcurr = curr_pos[0]
      if ((to_x == i and to_y == j)):
        return True
      if (first_charcurr == "w" or first_charcurr == "b"):
        break

    for i, j in zip( range(from_x + 1,8),range(from_y - 1,-1,-1) ):
      curr_pos = pieces[i][j]
      first_charcurr = curr_pos[0]
      if ((to_x == i and to_y == j)):
        return True
      if (first_charcurr == "w" or first_charcurr == "b"):
        break

    for i, j in zip( range(from_x - 1, -1, -1), range(from_y + 1, 8) ):
      curr_pos = pieces[i][j]
      first_charcurr = curr_pos[0]
      if ((to_x == i and to_y == j)):
        return True
      if (first_charcurr == "w" or first_charcurr == "b"):
        break
       
  #basic king rules
    if firsttap == "bk" or firsttap == "wk":
        x1 = from_x + 1
        y1 = from_y + 1
        if (x1 == to_x and y1 == to_y):
            return True
        x2 = from_x - 1
        y2 = from_y - 1
        if (x2 == to_x and y2 == to_y):
            return True
        x3 = from_x
        y3 = from_y - 1
        if (x3 == to_x and y3 == to_y):
            return True
        x4 = from_x
        y4 = from_y + 1
        if (x4 == to_x and y4 == to_y):
            return True
        x5 = from_x + 1
        y5 = from_y
        if (x5 == to_x and y5 == to_y):
            return True
        x6 = from_x - 1
        y6 = from_y
        if (x6 == to_x and y6 == to_y):
            return True
        x7 = from_x - 1
        y7 = from_y + 1
        if (x7 == to_x and y7 == to_y):
            return True
        x8 = from_x + 1
        y8 = from_y - 1
        if (x8 == to_x and y8 == to_y):
            return True
        else:
            return False
         
    #queen rules
    if ((firsttap == "wq" or firsttap == "bq") and (abs(to_x - from_x) == abs(to_y - from_y))):
        for i, j in zip(range(from_x + 1, 8), range(from_y + 1, 8)):
            curr_pos = pieces[i][j]
            first_charcurr = curr_pos[0]
            if ((to_x == i and to_y == j)):
                return True
            if (first_charcurr == "w" or first_charcurr == "b"):
                break

        for i, j in zip(range(from_x - 1, to_x - 1, -1), range(from_y - 1, to_y - 1, -1)):
            curr_pos = pieces[i][j]
            first_charcurr = curr_pos[0]
            if ((to_x == i and to_y == j)):
                return True
            if (first_charcurr == "w" or first_charcurr == "b"):
                break

        for i, j in zip(range(from_x + 1, 8), range(from_y - 1, -1, -1)):
            curr_pos = pieces[i][j]
            first_charcurr = curr_pos[0]
            if ((to_x == i and to_y == j)):
                return True
            if (first_charcurr == "w" or first_charcurr == "b"):
                break

        for i, j in zip(range(from_x - 1, -1, -1), range(from_y + 1, 8)):
            curr_pos = pieces[i][j]
            first_charcurr = curr_pos[0]
            if ((to_x == i and to_y == j)):
                return True
            if (first_charcurr == "w" or first_charcurr == "b"):
                break
    if firsttap == "wq" or firsttap == "bq":
        if from_x == to_x:
            if from_y > to_y:
                for i in range(to_y + 1, from_y):
                    if pieces[from_x][i] != "-":
                        return False
                return True

            if from_y < to_y:
                for i in range(from_y + 1, to_y):
                    if pieces[from_x][i] != "-":
                        return False
                return True

        if from_y == to_y:
            if from_x > to_x:
                for i in range(to_x + 1, from_x):
                    if pieces[i][from_y] != "-":
                        return False
                return True
            if from_x < to_x:
                for i in range(from_x + 1, to_x):
                    if pieces[i][from_y] != "-":
                        return False
                return True


    
   #knight rules
  if firsttap == "bh" or firsttap == "wh":
    print("knight move")
    x1 = from_x + 1
    y1 = from_y + 2
    if (x1 == to_x and y1 == to_y):
      return True
    x2 = from_x + 1
    y2 = from_y - 2
    if (x2 == to_x and y2 == to_y):
      return True
    x3 = from_x - 2
    y3 = from_y + 1
    if (x3 == to_x and y3 == to_y):
      return True
    x4 = from_x - 2
    y4 = from_y - 1
    if (x4 == to_x and y4 == to_y):
      return True
    x5 = from_x + 2
    y5 = from_y + 1
    if (x5 == to_x and y5 == to_y):
      return True
    x6 = from_x + 2
    y6 = from_y - 1
    if (x6 == to_x and y6 == to_y):
      return True
    x7 = from_x - 1
    y7 = from_y + 2
    if (x7 == to_x and y7 == to_y):
      return True
    x8 = from_x - 1
    y8 = from_y - 2
    if (x8 == to_x and y8 == to_y):
      return True
    else:
      return False
     
       
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
  
  #castling



  c=0
  b=0

  if(firsttap == "wk"):


    for i in range(5,7):
      curr_pos = pieces[7][i]
      first_charcurr = curr_pos[0]
      if(first_charcurr == "w" or first_charcurr == "b"):
        c=1

    for i in range(3,0,-1):
      curr_pos = pieces[7][i]
      first_charcurr = curr_pos[0]
      if (first_charcurr == "w" or first_charcurr == "b"):
         b = 1

  if((from_x == 7 and from_y == 4) and c == 0):
    if(to_x == 7 and to_y == 6):
      pieces[7][7]="-"
      pieces[7][5]="wr"

  if ((from_x == 7 and from_y == 4) and b == 0):
    if (to_x == 7 and to_y == 2):
      pieces[7][0] = "-"
      pieces[7][3] = "wr"

  d=0
  e=0
  if (firsttap == "bk"):
    for i in range(5, 7):
      curr_pos = pieces[0][i]
      first_charcurr = curr_pos[0]
      if (first_charcurr == "w" or first_charcurr == "b"):
        d = 1
    for i in range(3,0,-1):
      curr_pos = pieces[0][i]
      first_charcurr = curr_pos[0]
      if (first_charcurr == "w" or first_charcurr == "b"):
        e = 1

  if ((from_x == 0 and from_y == 4) and e == 0):
    if (to_x == 0 and to_y == 6):
      pieces[0][7] = "-"
      pieces[0][5] = "br"

  if ((from_x == 0 and from_y == 4) and e == 0):
    if (to_x == 0 and to_y == 2):
      pieces[0][0] = "-"
      pieces[0][3] = "br"
  return True
  
  #Universal return False
  return False
