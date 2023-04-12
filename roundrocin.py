def round_robin(processes, time_slice):
    n = len(processes)
    completed_processes = []
    while len(processes) > 0:
        for i in range(n):
            if processes[i][1] > 0:
                processes[i][1] -= time_slice
                if processes[i][1] <= 0:
                    completed_processes.append(processes[i][0])
                    processes.pop(i)
                    n -= 1
                    i -= 1
    return completed_processes

# Example usage
processes = [["P1", 10], ["P2", 5], ["P3", 8], ["P4", 2]]
time_slice = 2
completed_processes = round_robin(processes, time_slice)
print(completed_processes)