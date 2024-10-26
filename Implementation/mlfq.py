#########################################
#                                       #
#                 MLFQ                  #
#                                       #
#########################################

import sys
import process
import queue_list


class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg


def print_state():
    print("Current State:")



if __name__ == "__main__":
    try:
        queue1 = queue_list.Queue(0)
        queue1.add_process(process.Process(1, 20))
        queue1.add_process(process.Process(3, 5))
        queue1.add_process(process.Process(2, 10))
        print(queue1.__str__())
    except CustomError as e:
        print("An Exception occured: ", e.msg)
    except Exception:
        print("Unexpected error: ", sys.exc_info()[0])
        raise
