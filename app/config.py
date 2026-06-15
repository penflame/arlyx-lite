from pathlib import Path
import yaml

CONFIG_PATH = Path("/app/configs/arlyx-lite.yaml")

def load_config():
    with CONFIG_PATH.open("r") as f:
        return yaml.safe_load(f)

config = load_config()
