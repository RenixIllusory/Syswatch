# syswatch/cli.py
from core import get_cpu_usage, get_memory_usage, get_disk_usage, get_top_processes
from utils import format_bytes



def main():
    while True:
        print("\n=== SysWatch Menu ===")
        print("1. CPU Usage")
        print("2. Memory Usage")
        print("3. Disk Usage")
        print("4. Top Processes")
        print("5. Exit")

        choice = input("Выберите опцию (1-5): ").strip()

        if choice == "1":
            print(f"CPU Usage: {get_cpu_usage()}%")
        elif choice == "2":
            mem_percent, mem_used, mem_total = get_memory_usage()
            print(f"Memory Usage: {mem_percent}% ({format_bytes(mem_used)}/{format_bytes(mem_total)})")
        elif choice == "3":
            disk_percent, disk_used, disk_total = get_disk_usage()
            print(f"Disk Usage: {disk_percent}% ({format_bytes(disk_used)}/{format_bytes(disk_total)})")
        elif choice == "4":
            n = input("Сколько топ процессов показать?").strip()
            if n.isdigit():
                n = int(n)
                for pid, name, cpu, mem in get_top_processes(n):
                    print(f"PID: {pid}, Name: {name}, CPU: {cpu}%, Mem: {mem:.2f}%")
            else:
                print("Введите число!")
        elif choice == "5":
            print("")
            break
        else:
            print()

if __name__ == "__main__":
    main()
