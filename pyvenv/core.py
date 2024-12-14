import os
import subprocess
from pyvenv.pyenv_utils import is_pyenv_installed

BASE_DIR = os.path.expanduser("~/.pyvenv_envs")

# Ensure the base directory exists
def ensure_base_dir():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

# Create a virtual environment
def create_virtual_environment(name, version):
    ensure_base_dir()

    env_path = os.path.join(BASE_DIR, name)

    if os.path.exists(env_path):
        print(f"Virtual environment '{name}' already exists at {env_path}")
        return

    if not is_pyenv_installed():
        print("PyEnv is not installed. Please install PyEnv and try again.")
        return

    print(f"Creating virtual environment '{name}' with Python {version}...")
    try:
        subprocess.run(["pyenv", "install", "-s", version], check=True)
        subprocess.run(["pyenv", "virtualenv", version, name], check=True)
        print(f"Virtual environment '{name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to create virtual environment '{name}'. {e}")

# List all virtual environments
def list_virtual_environments():
    ensure_base_dir()
    envs = os.listdir(BASE_DIR)

    if not envs:
        print("No virtual environments found.")
        return

    print("Available virtual environments:")
    for env in envs:
        print(f"- {env}")

# Activate a virtual environment
def activate_virtual_environment(name):
    env_path = os.path.join(BASE_DIR, name)

    if not os.path.exists(env_path):
        print(f"Virtual environment '{name}' does not exist.")
        return

    activate_script = os.path.join(env_path, "bin", "activate")

    if not os.path.exists(activate_script):
        print(f"Activation script not found for '{name}'.")
        return

    print(f"To activate the virtual environment, run:\nsource {activate_script}")