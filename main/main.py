import psutil

def get_system_memory_info():
    mem = psutil.virtual_memory()
    total_memory = mem.total // (1024 * 1024)  # Convert to MB
    available_memory = mem.available // (1024 * 1024)  # Convert to MB
    return total_memory, available_memory
    print(f"Total Memory: {total_memory} MB")

total_memory, available_memory = get_system_memory_info()
print(f"Total Memory: {total_memory} MB")

if a == b:
    pass

def example_function():
    if x > y:
        print("x is greater than y.")
        if x - y > 5:
            print("The difference is more than 5.")
            if x % 2 == 0:
                print("x is even.")
                if y % 2 == 0:
                    print("y is also even.")
                else:
                    pass