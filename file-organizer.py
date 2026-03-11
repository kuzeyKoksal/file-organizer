import os
import shutil

folder_path = input("Enter folder path: ")

image_extensions = [".png", ".jpg", ".jpeg"]
video_extensions = [".mp4", ".mov"]
document_extensions = [".pdf", ".txt", ".docx"]

files = os.listdir(folder_path)

for file in files:

    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    file_extension = os.path.splitext(file)[1]

    if file_extension in image_extensions:
        folder_name = "Images"

    elif file_extension in video_extensions:
        folder_name = "Videos"

    elif file_extension in document_extensions:
        folder_name = "Documents"

    else:
        folder_name = "Others"

    target_folder = os.path.join(folder_path, folder_name)

    if not os.path.exists(target_folder):
        os.mkdir(target_folder)

    shutil.move(file_path, target_folder)

print("Files organized successfully!")
