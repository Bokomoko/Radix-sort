def radixSort( vector ):
  winput = list(vector) #create copy of input vector
  # calc number of passes = number of digits of max
  passes = math.ceil(math.log10(max(vector)))
  woutput =[]
  wdivider = 1 
  for i in range(passes) :
    # empty output
    woutput = [0]*len(winput)
    # restart counters
    numbers = [0]*10
    # counts how many times each digit occurred
    for elem in winput  :
      digit = (elem // wdivider) % 10 
      numbers[int(digit)] +=1
    #prefix sum !! This is the trick !
    for w in range(1,10):
      numbers[w] += numbers[w-1]
    
    #now moving from input to outuput
    for elem in winput[::-1]:
      digit = (elem // wdivider) % 10
      woutput[numbers[digit]-1] = elem 
      numbers[digit] -= 1  # one less elem with that digit
    
    winput = woutput
    del woutput
    wdivider *= 10

  return woutput
    

# main program begins here
import random 
import math

# read unsorted data from file
myList = list(map(int,open("unsorted.dat", "r").read().split(",")))

coisa = radixSort(myList)
print(coisa)