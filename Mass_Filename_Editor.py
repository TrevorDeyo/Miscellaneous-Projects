import os

def filename_editor(directory):

    target = " .mp3"

    for filename in os.listdir(directory):
        if target in filename:
            new_filename = filename.replace(target, ".mp3")
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            if os.path.exists(new_path):
                print(f"Skipped renameing {filename} as {new_filename}. File already exists.")
                continue
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")

directory = "C:/Users/tdeyo/Desktop/Code/MiscProjects/mp4s"
filename_editor(directory)