def round_robin(n, quantum):
    process_queue = []
    wait_time = [0] * n
    turnaround_time = [0] * n
    total_time = 0
    for i in range(n):
        process_name = input(f"Enter the process name for process {i+1}: ")
        process_burst_time = int(input(f"Enter the burst time for process {i+1}: "))
        process_queue.append((process_name, process_burst_time))
    i = 0
    while process_queue:
        process = process_queue.pop(0)
        if process[1] > quantum:
            total_time += quantum
            process_queue.append((process[0], process[1] - quantum))
        else:
            total_time += process[1]
            wait_time[i] = total_time - process[1]
            turnaround_time[i] = wait_time[i] + process[1]
            i += 1
    print("Process\tBurst Time\tWait Time\tTurnaround Time")
    for i in range(n):
        print(f"{process_queue[i][0]}\t\t{process_queue[i][1]}\t\t{wait_time[i]}\t\t{turnaround_time[i]}")
    print("Average Wait Time:", sum(wait_time) / n)
    print("Average Turnaround Time:", sum(turnaround_time) / n)

n = int(input("Enter the number of processes: "))
quantum = int(input("Enter the time quantum: "))
round_robin(n, quantum)
