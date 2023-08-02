def input_data():
    n = int(input("\nEnter total number of processes: "))
    processes = []
    for i in range(n):
        process_name = input(f"Enter the name of process {i}: ")
        processes.append(process_name)

    m = int(input("\nEnter the number of resources: "))

    all_resources = []
    max_resources = []
    for i in range(n):
        print(f"\nEnter allocation matrix for process {i}:")
        allocation = list(map(int, input().split()))
        all_resources.append(allocation)

    for i in range(n):
        print(f"Enter max resources for process {i}:")
        max_res = list(map(int, input().split()))
        max_resources.append(max_res)

    need_resources = [[max_resources[i][j] - all_resources[i][j] for j in range(m)] for i in range(n)]

    available_resources = list(map(int, input("\nEnter available resources: ").split()))

    return n, m, processes, all_resources, max_resources, need_resources, available_resources


def is_less_than_need(request, need_resources, process_id):
    return all(request[i] <= need_resources[process_id][i] for i in range(len(request)))


def is_less_than_available(request, available_resources):
    return all(request[i] <= available_resources[i] for i in range(len(request)))


def request_resources(processes, all_resources, need_resources, available_resources):
    process_id = int(input("\nEnter the process ID that is requesting: "))
    request = list(map(int, input("Enter the requested resources: ").split()))

    if not is_less_than_need(request, need_resources, process_id):
        print("\nProcess is requesting more resources than needed. Request cannot be granted.")
        return

    if not is_less_than_available(request, available_resources):
        print("\nProcess must wait. Not enough resources available.")
        return

    for i in range(len(request)):
        available_resources[i] -= request[i]
        all_resources[process_id][i] += request[i]
        need_resources[process_id][i] -= request[i]

    print("\nRequest granted. Resources allocated.")


def find_safe_sequence(all_resources, processes, need_resources, available_resources):
    n = len(processes)
    m = len(available_resources)
    work = available_resources[:]
    finish = [False] * n
    safe_sequence = []

    while True:
        process_found = False
        for i, process in enumerate(processes):
            if not finish[i] and all(need_resources[i][j] <= work[j] for j in range(m)):
                work = [work[j] + all_resources[i][j] for j in range(m)]
                finish[i] = True
                safe_sequence.append(process)
                process_found = True

        if not process_found:
            break

    if all(finish):
        print("\nSystem is in a safe state.")
        print("Safe sequence:", " -> ".join(safe_sequence))
    else:
        print("\nSystem is not in a safe state.")


def print_data(n, m, processes, all_resources, max_resources, need_resources, available_resources):
    print("\nNumber of processes =", n)
    print("Number of resources =", m)
    print("\nPID\t Max \t Allocated \t Need")
    for i, process in enumerate(processes):
        print(process, end="\t")
        print(" ".join(str(max_resources[i][j]) for j in range(m)), end="\t\t")
        print(" ".join(str(all_resources[i][j]) for j in range(m)), end="\t\t")
        print(" ".join(str(need_resources[i][j]) for j in range(m)))


def main():
    n, m, processes, all_resources, max_resources, need_resources, available_resources = None, None, None, None, None, None, None

    while True:
        print("\nMenu:")
        print("1. Input Data")
        print("2. Request Resources")
        print("3. Find Safe Sequence")
        print("4. Print Data")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n, m, processes, all_resources, max_resources, need_resources, available_resources = input_data()
        elif choice == 2:
            if n is None:
                print("Please input data first.")
            else:
                request_resources(processes, all_resources, need_resources, available_resources)
        elif choice == 3:
            if n is None:
                print("Please input data first.")
            else:
                find_safe_sequence(all_resources,processes, need_resources, available_resources)
        elif choice == 4:
            if n is None:
                print("Please input data first.")
            else:
                print_data(n, m, processes, all_resources, max_resources, need_resources, available_resources)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()