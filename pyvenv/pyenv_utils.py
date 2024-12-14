import shutil
import subprocess

def is_pyenv_installed():
    """Check if PyEnv is installed on the system."""
    return shutil.which("pyenv") is not None

def ensure_pyenv_installed():
    """Ensure that PyEnv is installed, or guide the user to install it."""
    if not is_pyenv_installed():
        print("PyEnv is not installed. Please install it by following the instructions at https://github.com/pyenv/pyenv.")
        exit(1)

def get_pyenv_version():
    """Get the current version of PyEnv."""
    if not is_pyenv_installed():
        return None

    try:
        result = subprocess.run(["pyenv", "--version"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None