from colorama import Fore, Style, init
from pathlib import Path
import sys

init(convert=True)

def visualize_directory_structure(directory_path, indent=0):
    
    path = Path(directory_path)
    if not path.is_dir():
        print(f"{Fore.RED}Error: The specified path is not a directory.{Style.RESET_ALL}")
        return

    for item in path.iterdir():
        if item.is_dir():
            print(f"{' ' * indent}{Fore.BLUE} {item.name}/{Style.RESET_ALL}")  # Виведення назви піддиректорії синім кольором
            visualize_directory_structure(item, indent + 4)  # Рекурсивний виклик для відображення вмісту піддиректорії
        else:
            print(f"{' ' * indent}{Fore.GREEN} {item.name}{Style.RESET_ALL}")  # Виведення назви файлу зеленим кольором

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python script.py /path/to/directory{Style.RESET_ALL}")
    else:
        directory_path = sys.argv[1]
        visualize_directory_structure(directory_path)