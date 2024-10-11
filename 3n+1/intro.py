import matplotlib.pyplot as plt
import time

import numpy as np
import sys

n=0

while True:
    try:
        n=int(input("Enter a number: "))    #this validates the input
        if n < 1:
            print("Invalid input ")      #if the user enters a number that is 0 or negative it starts the process again
            continue
        else:
            break
    except:
        print("Invalid input ")
        continue


def sequence(n):
    loops=0

    while True:
        if n == 1:     #if n == 1 loop breaks
            return loops
            break
        elif n % 2 == 0: #checks if n is even
            n = n / 2
            loops = loops + 1   #everytime the number goes through the process the loop counter increases by 1
            continue
        else:
            n = n * 3 + 1  #checks if the number is odd
            loops = loops + 1
            continue
        break

#this section of code allows the user to enter which numbers in a range they would like to display on a chart
r = int(input("Enter a number you want to go up to: "))


rangelist=[]
numberlist=[]

timestart = time.process_time()

for i in range(0,r):
    rangelist.append(sequence(i+1))
    numberlist.append(i+1)
    #print(rangelist)
    #print(numberlist)

#bar chart
x = numberlist
y = rangelist
plt.xlabel("Number")
plt.ylabel("Number of loops")
plt.title("Collatz Conjecture")
plt.bar(x,y)
plt.savefig("barchart.png")

#line graph

'''x = np.array([numberlist])
y = np.array([rangelist])

plt.plot(x, y)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
plt.savefig("linegraph.png")'''

timestop = time.process_time()
print("Elapsed time:", timestop - timestart)