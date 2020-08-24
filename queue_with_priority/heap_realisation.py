from math import floor


class HeapNode:
    def __init__(self, value):
        self.data = [value]

    def __str__(self):
        return str(self.data)

    def print_heap(self, index=1):
        element = self.data[index-1]
        left, right = self.left_child(index), self.right_child(index)
        print(f'Element {element} with index {index} has children: {left, right}')
        if self.has_left(index):
            self.print_heap(index*2)
        if self.has_right(index):
            self.print_heap((index*2)+1)

    def get_max(self):
        return self.data[0]

    def get_height(self):
        counter, ind= 1, len(self.data)
        while ind != 1:
            counter += 1
            ind = floor(ind/2)
        return counter

    def has_left(self, index):
        child_index = index * 2
        if child_index - 1 < len(self.data):
            return True

    def has_right(self, index):
        child_index = (index*2) + 1
        if child_index - 1 < len(self.data):
            return True

    def left_child(self, index):
        if self.has_left(index):
            return self.data[(index*2)-1]

    def right_child(self, index):
        if self.has_right(index):
            return self.data[(index*2)]

    def insert(self, value):
        el_ind = len(self.data) + 1
        self.data.append(value)
        self.push_up(el_ind)

    def push_up(self, ind):
        if ind == 1:
            return
        parent_ind = floor(ind/2)
        if self.data[parent_ind - 1] < self.data[ind - 1]:
            self.data[parent_ind - 1], self.data[ind - 1] = self.data[ind - 1], self.data[parent_ind - 1]
            self.push_up(parent_ind)

    def push_down(self, ind):
        left_child_ind, right_child_ind, next_ind = ind*2, (ind*2)+1, ind
        if left_child_ind <= len(self.data) and self.data[left_child_ind-1] > self.data[next_ind-1]:
            next_ind = left_child_ind
        if right_child_ind <= len(self.data) and self.data[right_child_ind-1] > self.data[next_ind-1]:
            next_ind = right_child_ind
        if ind != next_ind:
            self.data[next_ind - 1], self.data[ind - 1] = self.data[ind - 1], self.data[next_ind - 1]
            self.push_down(next_ind)

    def extract_max(self):
        last_el, max_el = self.data[-1], self.data[0]
        self.data[0] = last_el
        self.data.pop()
        self.push_down(1)
        return max_el

    def remove(self, ind):
        if len(self.data) >= ind > 0:
            value = self.data[-1]
            self.data[ind-1] = value
            self.data.pop()
            if value > self.data[floor(ind/2)]:
                self.push_up(ind)
            else:
                self.push_down(ind)
        else:
            print('Wrong index to remove')

    def change_priority(self, index, priority):
        old_priority = self.data[index-1]
        self.data[index - 1] = priority
        if priority > old_priority:
            self.push_up(index)
        else:
            self.push_down(index)


start_node = HeapNode(2)
start_node.insert(5)
start_node.insert(9)
start_node.insert(0)
start_node.insert(1)
start_node.insert(11)
start_node.insert(15)
start_node.insert(100)
start_node.insert(0)

print(start_node)
print(start_node.get_max())
print(start_node.get_height())
print(start_node.extract_max())

start_node.remove(1)
start_node.remove(1)
start_node.print_heap()
print(start_node)

start_node.change_priority(1, 15)
start_node.print_heap()
print(start_node)
start_node.change_priority(3, 16)
start_node.print_heap()
print(start_node)
