import logging
import os

def setup_logging():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file_path = os.path.join(log_dir, "server.log")
    logging.basicConfig(
        level=logging.DEBUG, 
        format="%(asctime)s - %(levelname)s - %(message)s", 
        handlers=[
            logging.FileHandler(log_file_path), 
            logging.StreamHandler() 
        ]
    )
    return logging.getLogger()

