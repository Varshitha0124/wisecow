import psutil
import logging


logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')


CPU_THRESHOLD = 80 
MEMORY_THRESHOLD = 80 
DISK_THRESHOLD = 80 
def monitor_system():

    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')

 
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory_usage}%')


    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High Disk usage detected: {disk_usage}%')

  
    process_count = len(psutil.pids())
    logging.info(f'Number of running processes: {process_count}')

if __name__ == "__main__":
    monitor_system()
    print("System health monitoring complete. Check 'system_health.log' for details.")
