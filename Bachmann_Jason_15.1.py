import multiprocessing
import time
import random
from datetime import datetime

def worker():
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    
    print(f"Process {multiprocessing.current_process().name} - Time: {datetime.now().strftime('%H:%M:%S.%f')}")

if __name__ == '__main__':
    processes = []

    for _ in range(3):
        process = multiprocessing.Process(target=worker)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()