from sys import argv
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

def next_dice(n=6):
    # genarate all the permutations of 2 dice
    for f in range(1,n+1):
        for s in range(1,n+1):
             yield f,s

def calc(goal, mem, depth = 1, first = 0, second = 0):
    #generate uniq key
    key = ( goal, first, second, depth ) 
    #check if we have the answer
    if key in mem:
        return mem[key]
    #Check if we are at the goal
    if first + second == goal:
        return 1
    elif first + second > goal:
        # Dont expand if we overreached in the search 
        return 0
    else:
        #expand all the posible dice throws
        res = []
        for f , s in next_dice():
            res.append(calc(goal - first - second, mem, depth+1, f, s))
        # calculate the propobility
        value = sum(map(lambda x: x/len(res), res))
        # save the value
        mem[key] = value
        return value

def plot(data):
    # this is for plotting purpose
    index = list(range(1,len(data)+1))
    _ , ax = plt.subplots(1, 1)
    ax.grid()
    plt.bar(index, data)
    plt.ylabel('Propobility')
    plt.xlabel('Steps')
    plt.xticks(index)
    plt.show()

def main(n):
    res = []
    for i in range(1,n):
        mem = {}
        res.append(round(calc(i, mem)*100,2))
    #plot the result
    plot(res)

if __name__ == "__main__":
    if len(argv) == 2:
        main(int(argv[1]))
    else:
        #default run for 20 tiles
        main(20)
