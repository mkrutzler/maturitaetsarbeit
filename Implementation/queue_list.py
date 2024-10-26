class Queue:
    def __init__ (self, priority):
        self.priority = priority  # Should be an int
        self.processes = []  # Keeps track of all processes

    def __str__(self):
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print(f"| QUEUE          {self.priority} |")
        print("|                  |")
        for process in self.processes:
            process.__str__()
    
    def add_process(self, process):
        process.priority = self.priority
        self.processes.append(process)

    def remove_process(self, process):
        process.priority = self.priority
        self.processes.remove(process)