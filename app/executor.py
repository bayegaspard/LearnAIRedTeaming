# flask_app/app/executor.py

from app.utils import run_command

class ServiceManager:
    def run_service(self, service_name):
        if service_name == 'ctfd':
            self.start_ctfd()
        elif service_name == 'challenge1':
            self.start_challenge('challenge1', 9001)
        elif service_name == 'challenge2':
            self.start_challenge('challenge2', 9002)

    def start_ctfd(self):
        run_command(['docker', 'compose', 'up', 'ctfd', '-d'], 
                    "CTFd started successfully at http://127.0.0.1:8000", 
                    "CTFd startup failed!")

    def start_challenge(self, challenge_name, port):
        run_command(['docker', 'compose', 'up', challenge_name, '-d'], 
                    f"{challenge_name} started! Connect to port {port}.", 
                    f"Failed to start {challenge_name}.")
