import os
import shutil

def format_folder(directory):
    # Dictionary to map folder names to file extensions
    folder_map = {
        "Images": {".jpg", ".jpeg", ".png"},
        "Videos": {".mp4", ".mkv"},
        "Music": {".mp3", ".wav"}
    }
    
    # Get user-defined folder names or skip if "no"
    folder_names = {
        "Images": input("Enter the folder name for your images (type 'no' if there are no images): ").strip(),
        "Videos": input("Enter the folder name for your videos (type 'no' if there are no videos): ").strip(),
        "Music": input("Enter the folder name for your music (type 'no' if there are no songs): ").strip()
    }

    # Set current working directory
    cwd = os.getcwd()
    os.chdir(directory)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Ensure it's a file, not a directory
        if os.path.isfile(file_path):
            moved = False  # Track if the file was moved
            
            # Check file extensions against each category
            for category, extensions in folder_map.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    folder_name = folder_names[category]
                    if folder_name.lower() != "no":
                        os.makedirs(folder_name, exist_ok=True)
                        shutil.move(file_path, folder_name)
                    moved = True
                    break
            
            # Move to 'Others' if it didn't match any category
            if not moved:
                os.makedirs("Others", exist_ok=True)
                shutil.move(file_path, "Others")
    
    os.chdir(cwd)  # Return to original directory

if __name__ == "__main__":
    directory = input("Enter the directory: ").strip()
    if os.path.isdir(directory):
        format_folder(directory)
        print("Files organized successfully. Thanks for using!")
    else:
        print("Invalid directory. Please try again.")
