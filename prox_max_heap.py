import sys

class priorityQueue:

    def __init__(self, Arr):
        self.Arr = [0]
        self.Arr.extend(Arr)
        self.length = len(Arr)
        self.build_max_heap()

    def maximum(self):
        # Return the root element of heap O(1)
        return self.Arr[1]

    def pop(self):
        # To extract the task with maximum priority O(Log N)
        if self.length == 0:
            print("No tasks to pop!")
        
        _max = self.Arr[1]
        self.Arr[1] = self.Arr[self.length]
        self.length = self.length - 1
        self.max_heapify(1)

        return _max

    def max_heapify(self, i):
        #O(Log N)
        left = 2 * i
        right = 2 * i + 1

        if((left <= self.length) and ((self.Arr[left].time < self.Arr[i].time) or (self.Arr[left].priority > self.Arr[i].priority and self.Arr[left].time == self.Arr[i].time))):
            largest = left
        else:
            largest = i

        if((right <= self.length) and ((self.Arr[right].time < self.Arr[largest].time) or (self.Arr[right].priority > self.Arr[largest].priority and self.Arr[right].time == self.Arr[largest].time))):
            largest = right

        if(largest != i):
            self.swap(i, largest)
            self.max_heapify(largest)

    def build_max_heap(self):
        #O(N)
        for i in range(int(self.length/2), 0, -1):
            self.max_heapify(i)
        
    def swap(self, i, j):
        self.Arr[i], self.Arr[j] = self.Arr[j], self.Arr[i]


def parseCsv(name):
    result = []
    
    with open(name) as f:
        lis=[line.strip().split(",") for line in f]
        for x in lis:
            if(len(x) > 1):
                if(len(x) ==2):
                    x.append(0)
                else:
                    x[2] = int(x[2].strip())

                _task = Task(x[0].strip()[1:-1], x[1].strip()[1:-1], x[2])
                result.append(_task)
    
    return result


if(len(sys.argv) < 3):
    print("Invalid number of arguments\n")
    print("The terminal command should look like this:\npython3 queueProcess.py sample.csv \"2017/02/10 4:59\"")
    exit(0)

a = parseCsv(sys.argv[1])

current_time = parser.parse(sys.argv[2])

a = [x for x in a if x.time >= current_time]

tasks = priorityQueue(a)

for i in range(0, tasks.length):
    tmp = tasks.Arr[1].time
    
    if(tmp > current_time):
        diff = (tmp - current_time).total_seconds()
        time.sleep(diff)
        current_time = tmp

        # Pluralising
        minute = "minutes" if diff//60 > 1 else "minute"

        # To optimize further, the processes can be run using multi-threading in real case scenario
        print("-- After another " + format(int(diff//60)) + " "+minute+" --")

    y = tasks.pop()
    print("Current time [ " +  format(y.time) + "  ] , Event " + format(y.name) + " Processed | Priority " + format(y.priority))