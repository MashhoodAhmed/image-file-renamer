import os

count = 0
folder_location = input("Enter the folder location: ")

files = sorted(os.listdir(folder_location))

for file in files:
    filename, extension = os.path.splitext(file)

    if extension.lower() in [".jpg", ".jpeg", ".png"]:
        count += 1
        new_name = f"product_{str(count).zfill(3)}{extension}"
        old_file = os.path.join(folder_location, file)
        new_file = os.path.join(folder_location, new_name)

        # Safety check
        if not os.path.exists(new_file):
            os.rename(old_file, new_file)
        else:
            print(f"Skipped {file} (target already exists)")

print(f"Renamed {count} image files successfully.")
