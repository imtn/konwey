import threading
import queue

import math
import random

#vars
print_queue = queue.Queue() #a queue of tuples, where a tuple consists of final x, and the associated kon
#in left, out right
global commands = ['x=x+1','x=x+2','x=x-1']
seed = [1];

class live(threading.Thread):

    def __init__(self, threads_queue, kon):
        threading.Thread.__init__(self)
        self.threads_queue = threads_queue
        self.kon = kon

    def run(self):
        x = 1
        for num in self.kon:
            eval(commands[num])
        threads_queue.appendleft((x, self.kon))

def procreate():
    #while (true)
    #run kon
    live(print_queue, seed).start()
    #after it runs, get info from print_queue
    final_x, kon = print_queue.get()
    #for num of x, create a new kon that is slightly modified from old kon

    #run that

def edit_kon(kon):
    #40% add, 30% edit, 20% nothing, 10 % delete
    new_kon = list(kon)
    choice = random.randint(0,99)
    lines = math.floor(math.sqrt(random.randint(0, len(kon))))
    if (choice < 39): #add
        for _ in range(lines):
            new_kon.append(random.randint(0, len(commands)-1))
    elif (choice < 69): #edit
        for _ in range(lines):
            line = random.randint(len(new_kon))
            new_kon[line] = random.randint(0, len(commands)-1)
    elif (choice < 79): #delete
        for _ in range(lines):
            del new_kon[random.randint(0, len(new_kon))]

    return new_kon

if __name__ == "__main__":
    procreate()
