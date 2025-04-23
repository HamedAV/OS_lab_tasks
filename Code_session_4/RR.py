from queue import Queue

def round_robin_scheduling(processes, time_quantum, context_switch_time=2):
    processes.sort(key=lambda p: p['arrival_time'])
    ready_queue = Queue()
    time = 0
    i = 0 
    completed = []
    print("\nGantt Chart:")
    print("------------")

    while i < len(processes) or not ready_queue.empty():
        while i < len(processes) and processes[i]['arrival_time'] <= time:
            ready_queue.put(processes[i])
            i += 1
        
        if ready_queue.empty():
            time = processes[i]['arrival_time']
            continue

        p = ready_queue.get()

        exec_time = min(p['remaining_burst_time'], time_quantum)
        if 'start_time' not in p:
            p['start_time'] = time

        time += exec_time
        p['remaining_burst_time'] -= exec_time

        while i < len(processes) and processes[i]['arrival_time'] <= time:
            ready_queue.put(processes[i])
            i += 1

        if p['remaining_burst_time'] > 0:
            ready_queue.put(p)
        else:
            p['completion_time'] = time
            p['waiting_time'] = p['completion_time'] - p['arrival_time'] - p['burst_time']
            p['turnaround_time'] = p['completion_time'] - p['arrival_time']
            completed.append(p)

        time += context_switch_time 
        print(f"| {p['pid']} ", end='')

    print("|")
    print("------------")
    
    print("\nProcess Table:")
    print("PID\tArrival\tBurst\tStart\tCompletion\tWaiting\tTurnaround")
    total_waiting = 0
    total_turnaround = 0
    for p in completed:
        total_waiting += p['waiting_time']
        total_turnaround += p['turnaround_time']
        print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['start_time']}\t{p['completion_time']}\t\t{p['waiting_time']}\t{p['turnaround_time']}")

    n = len(processes)
    print(f"\nAverage Waiting Time: {total_waiting / n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround / n:.2f}")

process_list = [
    {'pid': 1, 'arrival_time': 2, 'burst_time': 7, 'remaining_burst_time': 7},
    {'pid': 2, 'arrival_time': 4, 'burst_time': 4, 'remaining_burst_time': 4},
    {'pid': 3, 'arrival_time': 6, 'burst_time': 1, 'remaining_burst_time': 1},
    {'pid': 4, 'arrival_time': 8, 'burst_time': 4, 'remaining_burst_time': 4},
]

time_quantum = 3

round_robin_scheduling(process_list, time_quantum)
