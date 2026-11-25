import subprocess
import config

def get_data():
    result = subprocess.run(
        f"upsc {config.conf['ups_name']}", 
        shell=True, 
        capture_output=True, 
        text=True
    )

    return parse_data(result.stdout)

def parse_data(input_data):
    parsed_data = {}
    left = ""
    right = ""
    for line in input_data.strip().split('\n'):
        left, right = line.split(':', 1)
        parsed_data[left.strip()] = right.strip()
    return parsed_data