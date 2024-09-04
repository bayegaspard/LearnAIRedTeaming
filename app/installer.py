# flask_app/app/installer.py

import hashlib
import pathlib
import requests
import shutil
from tqdm.auto import tqdm
from app.config import Config
from app.utils import run_command, check_file_integrity

class InstallationManager:
    def install(self):
        if not self.check_model_presence():
            self.download_model()
        self.pull_docker_images()

    def check_model_presence(self):
        if check_file_integrity(Config.MODEL_PATH, Config.MODEL_MD5):
            return True
        return False

    def download_model(self):
        model_url = Config.MODEL_URL
        model_path = pathlib.Path(Config.MODEL_PATH).expanduser().resolve()
        with requests.get(model_url, stream=True) as r:
            r.raise_for_status()
            with open(model_path, 'wb') as f, tqdm(total=int(r.headers.get('content-length', 0)), unit='B', unit_scale=True) as bar:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    bar.update(len(chunk))

    def pull_docker_images(self):
        for image in Config.AI_IMAGES:
            run_command(['docker', 'pull', image], f"Pulled Docker image: {image}", f"Failed to pull Docker image: {image}")
