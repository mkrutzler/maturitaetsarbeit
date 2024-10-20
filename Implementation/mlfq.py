# question: Research/MLFQ-Example/kernel/proc.c: 314
#           why no else: or case: for everything else why just nothing = break


#########################################
#                                       #
#                 MLFQ                  #
#                                       #
#########################################

import sys
import process


class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg


class Queue:
    def __init__(self, priority):
        self.priority = priority  # Should be an int
        self.processes = []  # Keeps track of all processes

    def __str__(self):
        print("Queue")


# Make a number two digit long for better printing
def makeTwoDigit(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)


def print_state():
    print("Current State:")


def main():
    process1 = process.Process(1, 10)
    print(process1.__str__())
    print("main")


try:
    main()
except CustomError as e:
    print("An Exception occured: ", e.msg)
except Exception:
    print("Unexpected error: ", sys.exc_info()[0])
    raise
