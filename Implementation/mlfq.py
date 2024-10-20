# question: Research/MLFQ-Example/kernel/proc.c: 314
#           why no else: or case: for everything else why just nothing = break


#########################################
#                                       #
#                 MLFQ                  #
#                                       #
#########################################

import sys


class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg


class Process:
    def __init__(self, pid, burst_time):
        # TODO: Limit each of these to max 99
        self.pid = pid
        self.priority = 0  # Processes start at Priority 0
        self.burst_time = burst_time

    def __str__(self):
        str_pid = makeTwoDigit(self.pid)
        str_priority = makeTwoDigit(self.priority)
        str_burst_time = makeTwoDigit(self.burst_time)

        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("| Process:    ", str_pid, " |")
        print("| Priority:   ", str_priority, " |")
        print("| Burst Time: ", str_burst_time, " |")
        print("|__________________|")


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
    process1 = Process(1, 10)
    print(process1.__str__())
    print("main")


try:
    main()
except CustomError as e:
    print("An Exception occured: ", e.msg)
except Exception:
    print("Unexpected error: ", sys.exc_info()[0])
    raise
