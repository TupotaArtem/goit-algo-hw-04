import sys
from pathlib import Path
from colorama import init, Fore

def print_directory_structure(directory, indent=""):
    try:
        entries = sorted(directory.iterdir(), key=lambda e: (not e.is_dir(), e.name.lower()))
        for entry in entries:
            if entry.is_dir():
                print(f"{indent}{Fore.BLUE}{entry.name}/{Fore.RESET}")
                print_directory_structure(entry, indent + "    ")  # Рекурсивний виклик
            else:
                print(f"{indent}{Fore.GREEN}{entry.name}{Fore.RESET}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Access denied: {directory}{Fore.RESET}")

def main():
    init(autoreset=True)  # Автоматично скидає колір після кожного виводу
    
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Usage: python script.py <directory_path>{Fore.RESET}")
        return
    
    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Error: Path does not exist.{Fore.RESET}")
        return
    if not path.is_dir():
        print(f"{Fore.RED}Error: Provided path is not a directory.{Fore.RESET}")
        return
    
    print(f"{Fore.CYAN}Directory structure of: {path}{Fore.RESET}")
    print_directory_structure(path)

if __name__ == "__main__":
    main()
