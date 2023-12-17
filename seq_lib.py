# TODO: Your solutions here...

# PROBLEM 1
def zip( s, t ):
  # gets length of list s and t
  a = len(s) 
  b = len(t)
  
  # size of new list
  size = 0

  # check for smaller list size, size of new list
  if(a<b):
    size = a
  else:
    size = b

  # creates empty list of size 'size'
  newList = [None] * size
  
  # loop through newList
  for i in range(size):
    # create tuple for index i
    myTuple = (s[i], t[i])
    # insert tuple into newList at index i
    newList[i] = myTuple

  # returns newList
  return newList

# PROBLEM 2
def find_period( s ):
  # initialize periodic as false
  periodic = False

  # size of list s
  size = len(s)

  # list cannot be periodic if the size is 0
  if(size == 0):
    return -1

  # p = size of the periodic, assumed it is 1 to begin wtih
  p = 1

  while (p < size):
    # periodic. sublist of elements of s
    per = s[0:p]
    # periodic = True

    # current index of period list
    pListIndex = 0

    # keep track if a previous test failed or not
    failedLoopTest = False

    for i in range(size):  
      if(( size % p == 0 ) and ( failedLoopTest == False )):
        print(str(s[i]) + ", " + str(per[pListIndex]))
        if(s[i] == per[pListIndex]):
          periodic = True
        else:
          periodic = False
          failedLoopTest = True
        
        # increment pListIndex
        pListIndex += 1
        if(pListIndex == len(per)):
          pListIndex = 0
    
    # for i in range(size) end.

    if(periodic == True):
      return p
    else:
      p += 1    
  # while (p < size) end.

  return -1

     
  #   # HINT
  #   # s[0:p] * (len(s)//p) == s

  #   p = p+1
  # BASED ON THE HINT:
  # s[0:p] gives you the periodic
  # len(s) // p gives the number of periodics in the list
  # multiplying the periodic size times the number of periodics in the list should return the list size!

  if(periodic == False):
   return -1
  else:
    return p
  # else:
  #   return 
