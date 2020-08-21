buf_size, num_of_els = (int(inp) for inp in input().split(' '))
queue, start_time = [], 0

def queue_add_packet(arrive, duration):
    if len(queue) != buf_size:
        queue.append([arrive, duration])
    else:
        return True

def packet_proc(time_dif):
    if queue:
        time_dif -= queue[0][0]

        if time_dif - queue[0][1] >= 0:
            queue.pop(0)

def start_time_checker(start_time, arrive) :
    if arrive >= start_time:
        return arrive, arrive + duration
    else:
        return start_time, start_time + duration


for packet in range(num_of_els):
    arrive, duration = (int(inp) for inp in input().split(' '))

    packet_proc(arrive)

    if not queue_add_packet(arrive, duration):
        printer, start_time = start_time_checker(start_time, arrive)
        queue[-1][0] = printer
        print(printer)
    else:
        print(-1)




