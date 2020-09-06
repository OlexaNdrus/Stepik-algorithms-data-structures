_, array_str = input(), list(int(x) for x in input().split(' '))

permutation_list = []


def push_down(heap, ind, size):
    left_child_ind, right_child_ind, next_ind = ind * 2, (ind * 2) + 1, ind
    if left_child_ind <= size and heap[left_child_ind - 1] <= heap[next_ind - 1]:
        next_ind = left_child_ind
    if right_child_ind <= size and heap[right_child_ind - 1] <= heap[next_ind - 1]:
        next_ind = right_child_ind
    if ind != next_ind:
        permutation_list.append((next_ind - 1, ind - 1))
        heap[next_ind - 1], heap[ind - 1] = heap[ind - 1], heap[next_ind - 1]
        push_down(heap, next_ind, size)


def build_heap(arr):
    for i in range(int(len(arr) / 2), 0, -1):
        push_down(arr, i, len(arr))


build_heap(array_str)
print(len(permutation_list))
for i, j in permutation_list:
    print(j, i)
