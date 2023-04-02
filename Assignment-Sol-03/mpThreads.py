# Importing Required Modules
from multiprocessing import Process

# Class to Handle multiprocessing
class mProcessing(object):
    # Constructor for MultiThreadProcessing Class
    def __init__(self, function_name, arg_list, no_of_processes):
        self.function_name = function_name
        self.no_of_processes = no_of_processes
        self.arg_list = arg_list

    # Method to Start Processes Using Multiprocessing
    def multi_process_run(self):
        process_list = []
        # Splitting Task over No. of Processes
        tprocess = int(len(self.arg_list) / self.no_of_processes)
        splitted_list = [self.arg_list[i:i + tprocess] for i in range(0, len(self.arg_list), tprocess)]

        for item in splitted_list:
            proc = Process(target=self.function_name, args=(item,))
            process_list.append(proc)
            proc.start()

        for proc in process_list:
            proc.join()

# Function To Read Items in List
def read_item(list1= []):
    print(list1)

if __name__ == "__main__":
    # Taking required inputs from user
    arg_list = list(map(str, input("Enter Values Separated by Space: ").split()))
    no_of_processes = int(input("Enter No. of Processes : \t"))

    obj1 = mProcessing(read_item,arg_list, no_of_processes)           # object Creation

    obj1.multi_process_run()                                           # function call

