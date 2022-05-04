import environ
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).parent.parent.parent
APP_DIR = ROOT_DIR / "{{ project_name }}"
env = environ.Env()
environ.Env.read_env(str(ROOT_DIR / ".env"))
