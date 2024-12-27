import os
import subprocess
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='backup_report.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define source directory and remote server details
SOURCE_DIR = '/path/to/source_directory'
REMOTE_USER = 'remote_user'
REMOTE_HOST = 'remote_host'
REMOTE_DIR = '/path/to/remote_directory'

def backup_directory():
    try:
        # Construct the rsync command
        command = f"rsync -avz {SOURCE_DIR} {REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}"
       
        # Run the rsync command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
       
        # Check result
        if result.returncode == 0:
            logging.info("Backup successful.")
            print("Backup successful.")
        else:
            logging.error(f"Backup failed. Error: {result.stderr}")
            print("Backup failed. Check the log for details.")
   
    except Exception as e:
        logging.error(f"Exception during backup: {e}")
        print("An error occurred during the backup. Check the log for details.")

if __name__ == "__main__":
    backup_directory()