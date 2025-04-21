
import threading
import time
from task_heart_rate import heart_rate_task
from task_oxygen_level import oxygen_level_task

def task_scheduler():
    while True:
        t1 = threading.Thread(target=heart_rate_task)
        t2 = threading.Thread(target=oxygen_level_task)

        t1.start()
        time.sleep(0.1)
        t2.start()

        t1.join()
        t2.join()
        time.sleep(5)  # Wait before next cycle

if __name__ == "__main__":
    task_scheduler()
