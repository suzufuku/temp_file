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