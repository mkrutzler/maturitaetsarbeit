#########################################
#                                       #
#                 MLFQ                  #
#                                       #
#########################################

import sys
import process
import queue_list as queue


class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg


def print_state():
    print("Current State:")

def mlfq(queues):
    quantum = 2
    for queue_index in range(len(queues)-1):
        while queues[queue_index].processes != []:
            queues[queue_index].__str__()
            inp = input("press enter to continue")
            for process in queues[queue_index].processes:
                process.allotment += quantum
                process.runtime += quantum
                if process.is_finished() == True:
                    print("process", process.pid, "finished")
                    queues[queue_index].remove_process(process)
                    continue
                else:
                    if process.allotment >= queues[queue_index].max_allotment:
                        process.allotment == 0
                        queues[queue_index].remove_process(process)
                        queues[queue_index + 1].add_process(process)
                    else:
                        continue


                    
            




if __name__ == "__main__":
    try:
        print("TODO: CREATE TABLE")
        queues = [ queue.Queue(0,6), queue.Queue(1,8), queue.Queue(2,12), queue.Queue(3,16), queue.Queue(4,24), queue.Queue(5,-1) ]
        i = 0
        for queue in queues:
            i += 1
            queue.add_process(process.Process(i,i*4+3))
        mlfq(queues)
    except CustomError as e:
        print("An Exception occured: ", e.msg)
    except Exception:
        print("Unexpected error: ", sys.exc_info()[0])
        raise
