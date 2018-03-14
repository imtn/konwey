import threading
import queue

import math
import random

#vars
print_queue = queue.Queue() #a queue of tuples, where a tuple consists of final x, and the associated kon
#in left, out right
commands = ['x=x+1','x=x+2','x=x-1']
seed = [0];

class live(threading.Thread):

    def __init__(self, threads_queue, kon):
        threading.Thread.__init__(self)
        self.threads_queue = threads_queue
        self.kon = kon

    def run(self):
        x = 1
        comm = ""
        for num in self.kon:
            comm += commands[num] + "\n"
        comm += "self.threads_queue.put((x, self.kon))"
        exec(comm)

def procreate():
    kon_queue = [seed]
    for _ in range(5):
        print(_)
        while(len(kon_queue) > 0):
            live(print_queue, kon_queue.pop()).start()
        while(not print_queue.empty()):
            new_x, kon = print_queue.get()
            if new_x > 0:
                for __ in range(new_x):
                    kon_queue.append(mutate(kon))
            print("X: " + str(new_x) + " - KON: " + str(kon))
    #run new kon

def mutate(kon): #edit_kon
    #40% add, 30% edit, 20% nothing, 10 % delete
    new_kon = list(kon)
    choice = random.randint(0,99)
    lines = math.floor(math.sqrt(random.randint(0, len(kon))))
    if (choice < 39): #add
        for _ in range(lines):
            new_kon.append(random.randint(0, len(commands)-1))
    elif (choice < 69): #edit
        for _ in range(lines):
            line = random.randint(0, len(new_kon)-1)
            new_kon[line] = random.randint(0, len(commands)-1)
    elif (choice < 79): #delete
        for _ in range(lines):
            if len(new_kon) > 1:
                del new_kon[random.randint(0, len(new_kon)-1)]

    return new_kon

if __name__ == "__main__":
    procreate()
