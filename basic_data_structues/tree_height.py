buf_size, num_of_els = (int(inp) for inp in input().split(' '))
queue, start_time = [], 0

def packet_proc(time_dif):
    if queue and time_dif - queue[0] >= 0:
            queue.pop(0)

def start_time_checker(start_time, arrive) :
    if arrive >= start_time:
        start_time = arrive
    return start_time, start_time + duration


for packet in range(num_of_els):
    arrive, duration = (int(inp) for inp in input().split(' '))

    packet_proc(arrive)

    if len(queue) != buf_size:
        printer, start_time = start_time_checker(start_time, arrive)
        queue.append(start_time)
        print(printer)
    else:
        print(-1)
