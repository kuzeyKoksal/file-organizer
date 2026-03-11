# File Organizer

A simple Python script that automatically organizes files in a folder based on their file extensions.

## Description
This project scans a selected folder and sorts files into different directories depending on their file type. For example, image files are moved to an Images folder, documents to a Documents folder, and videos to a Videos folder. The goal of this project is to demonstrate how Python can be used to automate simple file management tasks.

## Features
- Detects file types based on file extensions
- Automatically creates folders if they do not exist
- Moves files into the appropriate folders
- Supports multiple file categories such as images, documents, and videos

## Technologies Used
- Python
- os module
- shutil module

## How to Run
1. Clone the repository  
git clone https://github.com/yourusername/file-organizer.git  

2. Navigate to the project directory  
cd file-organizer  

3. Run the script  
python file_organizer.py  

4. Enter the folder path you want to organize when prompted.

## Example
Before running the script:

Downloads  
photo.png  
video.mp4  
report.pdf  
notes.txt  

After running the script:

Downloads  
Images/  
photo.png  

Videos/  
video.mp4  

Documents/  
report.pdf  
notes.txt  

## Purpose
This project was created to practice fundamental programming concepts such as loops, conditionals, working with directories, and building simple automation tools using Python.
