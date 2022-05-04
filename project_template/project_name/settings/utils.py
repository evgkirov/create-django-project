import environ
from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent.parent
BASE_DIR = ROOT_DIR / "{{ project_name }}"
env = environ.Env()
environ.Env.read_env(str(ROOT_DIR / ".env"))
