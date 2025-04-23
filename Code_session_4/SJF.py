def sjf_scheduling_with_context_switch(processes, context_switch_time=1):
    
    time = 0
    total_waiting = 0
    total_turnaround = 0
    completed = 0
    n = len(processes)
    ordered_processes = []
    print("\nGantt Chart:")
    print("------------")
    
    while completed < n:
        available_processes = [p for p in processes if p['arrival_time'] <= time and not p.get('completed', False)]

        if available_processes:
            available_processes.sort(key=lambda x: x['burst_time'])
            p = available_processes[0]
            if time < p['arrival_time']:
                time = p['arrival_time']

            p['start_time'] = time
            p['completion_time'] = time + p['burst_time']
            p['waiting_time'] = time - p['arrival_time']
            p['turnaround_time'] = p['completion_time'] - p['arrival_time']
            p['completed'] = True

            time = p['completion_time']
            completed += 1
            print(f"| {p['pid']} ", end='')
            ordered_processes.append(p)
            total_waiting += p['waiting_time']
            total_turnaround += p['turnaround_time']

            if completed < n:
                time += context_switch_time

        else:
            time += 1

    print("|")
    print("------------")

    print("\nProcess Table:")
    print("PID\tArrival\tBurst\tStart\tCompletion\tWaiting\tTurnaround")
    for p in ordered_processes:
        print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['start_time']}\t{p['completion_time']}\t\t{p['waiting_time']}\t{p['turnaround_time']}")

    print(f"\nAverage Waiting Time: {total_waiting / n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround / n:.2f}")

process_list = [
    {'pid': 1, 'arrival_time': 1, 'burst_time': 7},
    {'pid': 2, 'arrival_time': 2, 'burst_time': 4},
    {'pid': 3, 'arrival_time': 4, 'burst_time': 1},
    {'pid': 4, 'arrival_time': 5, 'burst_time': 4},
]

sjf_scheduling_with_context_switch(process_list)
