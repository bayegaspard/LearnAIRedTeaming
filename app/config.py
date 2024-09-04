# flask_app/app/config.py

class Config:
    SECRET_KEY = 'your_secret_key_here'
    MODEL_PATH = "models/ggml-vicuna-13b-q4_0.bin"
    MODEL_URL = "https://huggingface.co/vicuna/ggml-vicuna-13b-1.1/resolve/main/ggml-vicuna-13b-q4_0.bin"
    MODEL_MD5 = "dfe5d1e30242d63a72d06f7bee5edf80"
    AI_IMAGES = [
        "rootcauz/ai-base:0.0.1",
        "rootcauz/ai-ctfd:0.0.2"
    ]
