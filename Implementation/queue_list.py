class Queue:
    def __init__ (self, priority, max_allotment):
        self.priority = priority  # Should be an int
        self.processes = []  # Keeps track of all processes
        self.max_allotment = max_allotment # -1 for no max allotment, also TODO: check this for proper values

    def __str__(self):
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print(f"| QUEUE          {self.priority} |")
        print(f"| max_allotment  {self.max_allotment} |")
        print(f"| processes      {len(self.processes)} |")
        print("|                  |")
        for process in self.processes:
            process.__str__()
        print("\n")
    
    def add_process(self, process):
        process.priority = self.priority
        self.processes.append(process)

    def remove_process(self, process):
        self.processes.remove(process)
    
def print_queues():
    print("Hello")