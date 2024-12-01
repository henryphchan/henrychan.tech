import os
import shutil
import argparse
from collections import defaultdict
from pathlib import Path

def get_download_path():
    if os.name == 'nt':  # Windows
        return Path.home() / 'Downloads'
    else:  # macOS (or Unix-like systems)
        return Path.home() / 'Downloads'

def create_destination_folders(base_path, categories):
    folders = {}
    for category in categories:
        category_folder = base_path / category
        category_folder.mkdir(exist_ok=True)
        folders[category] = category_folder
    return folders

def get_file_category(file_extension, categories):
    for category, extensions in categories.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def move_file(src_path, dest_folder):
    dest_path = dest_folder / src_path.name
    counter = 1
    while dest_path.exists():
        new_name = f"{src_path.stem}_{counter}{src_path.suffix}"
        dest_path = dest_folder / new_name
        counter += 1
    shutil.move(str(src_path), str(dest_path))

def main():
    parser = argparse.ArgumentParser(description='Organize your Downloads folder.')
    parser.add_argument('-p', '--path', type=str, help='Path to the Downloads folder')
    args = parser.parse_args()

    downloads_path = Path(args.path) if args.path else get_download_path()

    # Define file type categories
    categories = {
        'Images': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'},
        'Documents': {'.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.csv', '.rtf', '.odt'},
        'Executables': {'.exe', '.msi', '.bat', '.sh', '.dmg'},
        'Compressed': {'.zip', '.rar', '.tar', '.gz', '.7z'},
        'Videos': {'.mp4', '.mov', '.wmv', '.flv', '.avi', '.mkv', '.webm'},
        'Audio': {'.mp3', '.wav', '.aac', '.ogg', '.flac'},
    }

    # Create destination folders if they don't exist
    destination_folders = create_destination_folders(downloads_path, list(categories.keys()) + ['Others'])

    # Organize files
    for file in downloads_path.iterdir():
        if file.is_file():
            category = get_file_category(file.suffix, categories)
            move_file(file, destination_folders[category])

if __name__ == '__main__':
    main()