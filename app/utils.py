# flask_app/app/utils.py

import hashlib
import subprocess
import pathlib

def check_file_integrity(file_path, expected_md5):
    if not pathlib.Path(file_path).exists():
        return False
    
    with open(file_path, 'rb') as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    
    return file_hash.hexdigest() == expected_md5

def run_command(command, success_message, failure_message):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(success_message)
    except subprocess.CalledProcessError as e:
        print(failure_message)
        print(e.stderr)
