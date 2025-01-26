# Organize Downloads Folder

 🌟 This folder contains all the relevant files and code samples associated with **[Organize Your Messy Downloads Folder with Python](https://henrychan.tech/organize-your-messy-downloads-folder-with-python/)** from the **[Henry's Dev Journey](https://henrychan.tech/)** blog!

This Python script helps you organize your Downloads folder by categorizing files into different types, such as Images, Documents, Executables, Compressed files, Videos, and Audio. The script moves files into corresponding folders, making it easier to keep your Downloads directory organized and clean.

## Features
- Automatically categorizes files into predefined types (e.g., Images, Documents, etc.).
- Creates new folders for each category if they do not already exist.
- Prevents overwriting by renaming files with the same name (e.g., `filename_1`, `filename_2`, etc.).
- Works on both Windows and macOS.

## Prerequisites
- Python 3.x

## Usage
To run the script, open a terminal or command prompt and use the following command:

```bash
python organize_downloads.py
```

### Optional Arguments
- `-p` or `--path`: Specify the path to the Downloads folder you want to organize. If this argument is not provided, the script will use the default Downloads folder for your system.

Example:

```bash
python organize_downloads.py -p "path/to/your/folder"
```

## File Categories
The script organizes files into the following categories:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`, `.webp`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt`, `.csv`, `.rtf`, `.odt`
- **Executables**: `.exe`, `.msi`, `.bat`, `.sh`, `.dmg`
- **Compressed**: `.zip`, `.rar`, `.tar`, `.gz`, `.7z`
- **Videos**: `.mp4`, `.mov`, `.wmv`, `.flv`, `.avi`, `.mkv`, `.webm`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.ogg`, `.flac`
- **Others**: Any files that do not fall under the above categories.

## Example Output
After running the script, your Downloads folder will have subfolders for each category, such as:

```
Downloads/
├── Images/
├── Documents/
├── Executables/
├── Compressed/
├── Videos/
├── Audio/
└── Others/
```

## Notes
- If a file with the same name already exists in the target folder, the script will rename the new file by appending a counter (e.g., `_1`, `_2`) to prevent overwriting.
- The script is compatible with both Windows and macOS.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements.

## Acknowledgements
- Inspired by the need to keep my Downloads folder organized and free of clutter.

