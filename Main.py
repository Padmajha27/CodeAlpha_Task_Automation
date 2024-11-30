import os
import shutil

def organize_files(folder_path):
    # Define categories and file extensions
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Others": []
    }

    # Create subfolders for each category
    for category in file_categories.keys():
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)

    # Organize files
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move files to appropriate folders
        moved = False
        for category, extensions in file_categories.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_path, category, file))
                moved = True
                break

        # If no match, move to 'Others'
        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file))

    print("Files organized successfully!")

# Provide the folder path to organize
folder_to_organize = input("Enter the folder path to organize: ")
organize_files(folder_to_organize)
