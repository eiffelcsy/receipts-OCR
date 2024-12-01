import os

def remove_duplicate_files(directory):
    try:
        files = os.listdir(directory)

        duplicate_files = [file for file in files if '(' in file and ')' in file]

        for file in duplicate_files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file}")
            else:
                print(f"Skipped (not a file): {file}")

        print("Cleanup completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

directory_path = "./dataset/test"
remove_duplicate_files(directory_path)
