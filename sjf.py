def sjf(n):
    process_queue = []
    wait_time = 0
    turnaround_time = 0
    current_time = 0
    for i in range(n):
        process_name = input(f"Enter the process name for process {i+1}: ")
        process_burst_time = int(input(f"Enter the burst time for process {i+1}: "))
        process_queue.append((process_name, process_burst_time))
    process_queue.sort(key=lambda x: x[1])
    print("Process\tBurst Time\tWait Time\tTurnaround Time")
    for i in range(n):
        current_time += process_queue[i][1]
        wait_time = current_time - process_queue[i][1]
        turnaround_time = current_time
        print(f"{process_queue[i][0]}\t\t{process_queue[i][1]}\t\t{wait_time}\t\t{turnaround_time}")
    print("Average Wait Time:", wait_time / n)
    print("Average Turnaround Time:", turnaround_time / n)

n = int(input("Enter the number of processes: "))
sjf(n)

