from math import ceil


class MinHeapNode:
    def __init__(self, proccess_num):
        self.data = [(0, num) for num in range(proccess_num)]

    def insert(self, value, proc):
        el_ind = len(self.data)
        self.data.append((value, proc))
        self.push_up(el_ind)

    def push_up(self, ind):
        if ind == 0:
            return
        parent_ind = ceil(ind/2 - 1)
        if self.data[parent_ind] > self.data[ind]:
            self.data[parent_ind], self.data[ind] = self.data[ind], self.data[parent_ind]
            self.push_up(parent_ind)

    def push_down(self, ind, size):
        if size == 0:
            return

        left_child_ind, right_child_ind, next_ind = (ind * 2) + 1, (ind * 2) + 2,  ind

        if left_child_ind < size and self.data[left_child_ind] < self.data[next_ind]:
            next_ind = left_child_ind

        if right_child_ind < size and self.data[right_child_ind] < self.data[next_ind]:
            next_ind = right_child_ind

        self.data[next_ind], self.data[ind] = self.data[ind], self.data[next_ind]

        if ind != next_ind:
            self.push_down(next_ind, size)

    def extract_min(self):
        last_el, min_el = self.data[-1], self.data[0]
        self.data[0] = last_el
        self.data.pop()
        self.push_down(0, len(self.data))
        return min_el

num_of_processes, _ = (int(i) for i in input().split(' '))
tasks = (int(i) for i in input().split(' '))

heap = MinHeapNode(num_of_processes)
for task in tasks:
    proc_start, ind_of_proc = heap.extract_min()
    heap.insert(proc_start+task, ind_of_proc)
    print(ind_of_proc, proc_start)

