import os
import shutil

# SOURCE FOLDER
source_folder = input("Enter folder path: ").strip()

# CHECK IF FOLDER EXISTS
if not os.path.exists(source_folder):
    print("Folder does not exist!")
    exit()

# FILE TYPES
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".odt", ".xlsx"],
    "Music": [".mp3", ".wav", ".m4a", ".m4b"],
    "Applications": [".exe", ".msi"]
}


# CREATE FOLDERS
def create_folders():

    folders = [
        "Images",
        "Documents",
        "Videos",
        "Music",
        "Applications",
        "Others"
    ]

    for folder in folders:

        folder_path = os.path.join(source_folder, folder)

        if not os.path.exists(folder_path):

            os.mkdir(folder_path)

            print(f"Created folder: {folder}")


# ORGANIZE FILES
def organize_files():

    files = os.listdir(source_folder)

    moved_count = 0

    for file in files:

        src = os.path.join(source_folder, file)

        # Skip folders
        if not os.path.isfile(src):
            continue

        name, extension = os.path.splitext(file)

        extension = extension.lower()

        found = False

        for folder, extensions in file_types.items():

            if extension in extensions:

                dest = os.path.join(source_folder, folder, file)

                # Skip duplicate filenames
                if os.path.exists(dest):

                    print(f"Skipping {file} (already exists)")
                    found = True
                    break

                shutil.move(src, dest)

                print(f"{file} moved to {folder}")

                moved_count += 1

                found = True

                break

        # Move uncategorized files
        if not found:

            others_dest = os.path.join(source_folder, "Others", file)

            if not os.path.exists(others_dest):

                shutil.move(src, others_dest)

                print(f"{file} moved to Others")

                moved_count += 1

    print("-" * 40)
    print(f"{moved_count} files organized successfully")


# RUN FUNCTIONS
create_folders()
organize_files()
