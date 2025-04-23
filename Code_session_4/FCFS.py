def read_processes_from_file(filename):
    processes = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 3:
                pid, arrival, burst = parts
                processes.append({
                    'pid': pid,
                    'arrival_time': int(arrival),
                    'burst_time': int(burst)
                })
    return processes

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival_time'])
    
    time = 0
    total_waiting = 0
    total_turnaround = 0

    print("\nGantt Chart:")
    print("------------")
    
    for p in processes:
        if time < p['arrival_time']:
            time = p['arrival_time']
        p['start_time'] = time
        p['completion_time'] = time + p['burst_time']
        p['waiting_time'] = time - p['arrival_time']
        p['turnaround_time'] = p['completion_time'] - p['arrival_time']
        time = p['completion_time']
        print(f"| {p['pid']} ", end='')

        total_waiting += p['waiting_time']
        total_turnaround += p['turnaround_time']

    print("|")
    print("------------")

    print("\nProcess Table:")
    print("PID\tArrival\tBurst\tStart\tCompletion\tWaiting\tTurnaround")
    for p in processes:
        print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['start_time']}\t{p['completion_time']}\t\t{p['waiting_time']}\t{p['turnaround_time']}")

    n = len(processes)
    print(f"\nAverage Waiting Time: {total_waiting / n:.2f}")
    print(f"Average Turnaround Time: {total_turnaround / n:.2f}")



filename = "fifo.txt"
processes = read_processes_from_file(filename)
fcfs_scheduling(processes)
