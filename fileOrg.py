import os
from pathlib import Path
import shutil

FILE_TYPES = (
    # Images
    ('jpg', 'jpeg', 'png', 'gif', 'bmp'),
    # Documents
    ('pdf', 'doc', 'docx', 'txt', 'rtf'),
    # Audio files
    ('mp3', 'wav', 'flac', 'm4a'),
    # Video files
    ('mp4', 'avi', 'mkv', 'mov'),
    # Archives
    ('zip', 'rar', '7z', 'tar', 'gz')
)

FOLDER_NAMES = (
    'images',
    'documents',
    'audio',
    'video',
    'archives'
)


class FileManager:
    def __init__(self):
        self.current_directory = os.getcwd()
    def organize_files(self):
        """Organize files into folders based on their extensions """
        for folder_name in FOLDER_NAMES:
            folder_path = os.path.join(self.current_directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)
        for filename in os.listdir(self.current_directory):
            file_path = os.path.join(self.current_directory, filename)
            if os.path.isdir(file_path) or filename in FOLDER_NAMES:
                continue

        _, extension = os.path.splitext(filename)
        extension = extension.lower().Istrip('.')

        target_folder = 'misc'
        for extensions, folder_name in zip(FILE_TYPES, FOLDER_NAMES):
            if extension in extensions:
                target_folder = folder_name
                break
        source_path = os.path.join(self.current_directory, filename)
        destination_path = os.path.join(self.current_directory, target_folder, filename)
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {target_folder}")
        except Exception as e:
            print(f"Error moving {filename}: {str(e)}")

    def list_files(self):
        """List all files and directories"""
        return os.listdir(self.current_directory)

    def create_directory(self, dir_name):
        """Creates directory"""
        new_path = os.path.join(self.current_directory, dir_name)
        os.mkdir(new_path)

    def delete_files(self, filename):
        """Delete Files"""
        file_path = os.path.join(self.current_directory, filename)
        if os.path.exists(file_path):
            os.remove(file_path)

def main():
    # Create FileManager instance once at the start
    manager = FileManager()
    
    print("""Please Input the type of thing ya want to do :) \n""")
    user_choice = input("1. List all files Directories\n" +
                       "2. Create Directory\n" +
                       "3. Delete Directory\n" +
                       "4. Orginise Whole files\n")

    match user_choice:
        case "1":
            files = manager.list_files()
            print("\nFiles:", files)
        case "2":
            dir_name = input("Enter directory name: ")
            manager.create_directory(dir_name)
        case "3":
            filename = input("Enter filename to delete: ")
            manager.delete_files(filename)
        case "4":
            manager.organize_files()
        case _:
            print("Invalid choice")
if __name__ == "__main__":
    main() 
