from math import floor


class HeapNode:
    def __init__(self,value = 0, array = None):
        self._data = [value]
        if array:
            self._data = list(array)

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    @property
    def heap_data(self):
        return self._data

    def print_heap(self, index=1):
        element = self._data[index - 1]
        left, right = self.left_child(index), self.right_child(index)
        print(f'Element {element} with index {index} has children: {left, right}')
        if self.has_left(index):
            self.print_heap(index*2)
        if self.has_right(index):
            self.print_heap((index*2)+1)

    def get_max(self):
        return self._data[0]

    def get_height(self):
        counter, ind= 1, len(self._data)
        while ind != 1:
            counter += 1
            ind = floor(ind/2)
        return counter

    def has_left(self, index):
        child_index = index * 2
        if child_index - 1 < len(self._data):
            return True

    def has_right(self, index):
        child_index = (index*2) + 1
        if child_index - 1 < len(self._data):
            return True

    def left_child(self, index):
        if self.has_left(index):
            return self._data[(index * 2) - 1]

    def right_child(self, index):
        if self.has_right(index):
            return self._data[(index * 2)]

    def insert(self, value):
        el_ind = len(self._data) + 1
        self._data.append(value)
        self.push_up(el_ind)

    def push_up(self, ind):
        if ind == 1:
            return
        parent_ind = floor(ind/2)
        if self._data[parent_ind - 1] < self._data[ind - 1]:
            self._data[parent_ind - 1], self._data[ind - 1] = self._data[ind - 1], self._data[parent_ind - 1]
            self.push_up(parent_ind)

    def push_down(self, ind, size):
        left_child_ind, right_child_ind, next_ind = ind*2, (ind*2)+1, ind
        if left_child_ind <= size and self._data[left_child_ind - 1] > self._data[next_ind - 1]:
            next_ind = left_child_ind
        if right_child_ind <= size and self._data[right_child_ind - 1] > self._data[next_ind - 1]:
            next_ind = right_child_ind
        if ind != next_ind:
            self._data[next_ind - 1], self._data[ind - 1] = self._data[ind - 1], self._data[next_ind - 1]
            self.push_down(next_ind, size)

    def extract_max(self):
        last_el, max_el = self._data[-1], self._data[0]
        self._data[0] = last_el
        self._data.pop()
        self.push_down(1, len(self.heap_data))
        return max_el

    def remove(self, ind):
        if len(self._data) >= ind > 0:
            value = self._data[-1]
            self._data[ind - 1] = value
            self._data.pop()
            if value > self._data[floor(ind / 2)]:
                self.push_up(ind)
            else:
                self.push_down(ind, len(self.heap_data))
        else:
            print('Wrong index to remove')

    def change_priority(self, index, priority):
        old_priority = self._data[index - 1]
        self._data[index - 1] = priority
        if priority > old_priority:
            self.push_up(index)
        else:
            self.push_down(index, len(self.heap_data))

    @staticmethod
    def build_heap(arr):
        unordered_heap = HeapNode(array=arr)
        for i in range(int(len(arr)/2), 0, -1):
            unordered_heap.push_down(i, len(arr))
        return unordered_heap

    @staticmethod
    def heap_sort(arr):
        heap_arr = HeapNode.build_heap(arr)
        size = len(heap_arr)
        for ind in range(size-1, 0, -1):
            heap_arr.heap_data[ind], heap_arr.heap_data[0] = \
                heap_arr.heap_data[0], heap_arr.heap_data[ind]
            heap_arr.push_down(1, ind)
        return heap_arr.heap_data


start_node = HeapNode(value= 2)
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

new_node = HeapNode.build_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
new_node.print_heap()
print(new_node)
print(HeapNode.heap_sort([8, 4, 5, 2, 1, 11, 16, 50, 0, 7]))
