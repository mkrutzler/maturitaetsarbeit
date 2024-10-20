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


# Make a number two digit long for better printing
def makeTwoDigit(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)
