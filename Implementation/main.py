# question: Research/MLFQ-Example/kernel/proc.c: 314
#           why no else: or case: for everything else why just nothing = break


# IMPLEMENT THE BASICS AS WELL!!!!!!!


#########################################
##                                     ##
##                MLFQ                 ##
##                                     ##
#########################################

class Process:
    def __init__(self, pid, priority, burst_time):
        self.pid = pid
        self.priority = priority
        self.burst_time = burst_time

def print_state():
    print("testing")