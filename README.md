File Organizer Script
Overview

This script organizes files in a specified directory into categorized folders based on their file extensions. It automatically sorts images, videos, music, and other files into separate folders. If a file doesn't match any of the predefined categories, it is moved to an "Others" folder.
Features

    Sorts files into the following categories:
        Images: .jpg, .jpeg, .png
        Videos: .mp4, .mkv
        Music: .mp3, .wav
    Allows the user to specify custom folder names for each category, or skip if not needed.
    If a file doesn't match any of the categories, it is moved to the "Others" folder.
    Ensures that folders are created only when needed.
    User-friendly prompts to guide the process.

Requirements

    Python 3.x

No additional libraries are needed for this script; it uses only built-in Python modules such as os and shutil.
Usage

    Clone or Download the Script: Download or clone the script to your local machine.

    Run the Script:
        Open a terminal and navigate to the directory where the script is saved.
        Run the script with the following command:

        python file_organizer.py

    Input Directory:
        When prompted, enter the full path of the directory you want to organize.

    Folder Names:
        You will be asked to enter folder names for the following categories:
            Images: Enter the folder name where images should be moved, or type 'no' to skip.
            Videos: Enter the folder name where videos should be moved, or type 'no' to skip.
            Music: Enter the folder name where music files should be moved, or type 'no' to skip.
        If you type 'no', the files will not be moved to any folder for that category.

    File Sorting:
        The script will check all files in the given directory and move them to the appropriate folder based on their extension. Files that don’t match any specified category will be moved to a folder named "Others."

    Completion:
        Once the files are organized, the script will display a confirmation message: "Files organized successfully. Thanks for using!"

Example

If you have a folder with the following files:

    image1.jpg
    movie.mp4
    song.mp3
    document.pdf

The script will ask for the folder names:

    For images: "Images"
    For videos: "Videos"
    For songs: "Music"

After running the script, the files will be sorted into:

    Images/
    Videos/
    Music/
    Others/ (for the document.pdf file)

Notes

    Ensure the specified directory exists and contains files for the script to organize.
    If the folder names you provide already exist, the script will add files to those folders without creating duplicates.

License

This script is open source and available for personal or educational use. Modify and distribute it as per your needs.
