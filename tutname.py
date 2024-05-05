import os
import shutil

# Get the directory path from the user
dir_path = input("Enter the directory path: ")

# Get a list of all subdirectories in the given directory
for subdir in os.listdir(dir_path):
    subdir_path = os.path.join(dir_path, subdir)
    
    # Check if it's a directory
    if os.path.isdir(subdir_path):
        # If the directory name contains "onlinetext", delete it
        if "onlinetext" in subdir:
            shutil.rmtree(subdir_path)
        else:
            # Inside each subdirectory, get a list of all files
            for filename in os.listdir(subdir_path):
                old_file_path = os.path.join(subdir_path, filename)
                
                # Construct the new file name using the subdirectory name and the file extension from the original file name
                new_file_name = f"{subdir}{os.path.splitext(filename)[1]}"
                new_file_path = os.path.join(subdir_path, new_file_name)
                
                # Rename (move) the file to its new name
                shutil.move(old_file_path, new_file_path)
