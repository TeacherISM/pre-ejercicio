import os
import zipfile
import shutil

def create_package():
    # Define the directories and files to include in the package
    directories_to_include = ['src']
    files_to_include = ['app.py', 'requirements.txt']

    # Create a temporary directory to store the package contents
    temp_directory = 'temp_package'
    os.makedirs(temp_directory, exist_ok=True)

    try:
        # Copy directories to the temporary directory
        for directory in directories_to_include:
            copy_directory(directory, temp_directory)

        # Copy files to the temporary directory
        for file in files_to_include:
            copy_file(file, temp_directory)

        # Create the .zip file
        package_name = 'your_package.zip'
        with zipfile.ZipFile(package_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(temp_directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, temp_directory)
                    zipf.write(file_path, relative_path)

        print(f"Package '{package_name}' created successfully!")

    finally:
        # Clean up the temporary directory
        if os.path.exists(temp_directory):
            remove_directory(temp_directory)

def copy_directory(source, destination):
    destination_directory = os.path.join(destination, os.path.basename(source))
    shutil.copytree(source, destination_directory)

def copy_file(source, destination):
    destination_file = os.path.join(destination, os.path.basename(source))
    shutil.copy2(source, destination_file)

def remove_directory(directory):
    shutil.rmtree(directory)

if __name__ == '__main__':
    create_package()