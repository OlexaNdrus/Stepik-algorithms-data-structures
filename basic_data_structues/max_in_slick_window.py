from collections import deque

len_of_arr = int(input())
arr = [int(n) for n in input().split(' ')]
window = int(input())


def max_every_window(arr, window):
    main_queue, minor_queue = deque(maxlen=window), deque(maxlen=window)

    def stack_swaper():
        max_el = 0
        for _ in range(window):
            swap_el = main_queue.pop()[0]
            if swap_el > max_el:
                max_el = swap_el
            minor_queue.append([swap_el, max_el])
        print(max_el)


    def window_add(window):
        max_el = 0
        for el in arr[window-1::-1]:
            if el > max_el:
                max_el = el
            minor_queue.append([el, max_el])
        print(max_el)

    window_add(window)
    max_el = 0
    for el in arr[window:]:
        if el > max_el:
            max_el = el
        main_queue.append([el, max_el])
        minor_queue.pop()
        if len(main_queue) == window:
            stack_swaper()
            max_el = 0
        else:
            print(max(minor_queue[-1][1], max_el))


max_every_window(arr, window)
