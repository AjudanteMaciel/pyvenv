import argparse
from pyvenv.core import create_virtual_environment, list_virtual_environments, activate_virtual_environment
from pyvenv.pyenv_utils import ensure_pyenv_installed


def main():
    parser = argparse.ArgumentParser(description="PyVenv: Manage your Python virtual environments with PyEnv.")
    
    subparsers = parser.add_subparsers(title="Commands", dest="command", required=True)

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new virtual environment")
    create_parser.add_argument("name", help="Name of the virtual environment")
    create_parser.add_argument("--version", help="Python version to use", required=True)

    # List command
    subparsers.add_parser("list", help="List all virtual environments")

    # Activate command
    activate_parser = subparsers.add_parser("activate", help="Activate a virtual environment")
    activate_parser.add_argument("name", help="Name of the virtual environment")

    args = parser.parse_args()

    # Ensure pyenv is installed
    ensure_pyenv_installed()

    # Handle commands
    if args.command == "create":
        create_virtual_environment(args.name, args.version)
    elif args.command == "list":
        list_virtual_environments()
    elif args.command == "activate":
        activate_virtual_environment(args.name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
