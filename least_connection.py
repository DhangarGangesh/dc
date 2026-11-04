
import csv

# Workers and their active connections
workers = {
    "Worker_1": 3,
    "Worker_2": 1,
    "Worker_3": 2
}

# Read jobs from CSV
with open("workload_13.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        job = row["job_id"]

        # Find worker with minimum connections
        worker = min(workers, key=workers.get)

        print("\nIncoming Job:", job)
        print("Assigned to:", worker)

        # Update connections
        workers[worker] += 1

        print("Updated Connections:", workers)

# Display final worker connections
print("\nFinal Worker Connections:")

for worker, count in workers.items():
    print(worker, ":", count)

print("\nLeast Connections Scheduling Completed!")
