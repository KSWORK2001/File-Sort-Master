import os

# Set the directory path where the files are located
directory_path = 'enter desired folder path here'

# Prompt the user for the desired file type
file_type = input("Enter the desired file type (e.g. txt): ")

# Get a list of all the files in the directory
files = os.listdir(directory_path)

# Loop through each file in the directory
for file in files:

    # Check if the file has the desired file type
    if file.endswith('.' + file_type):

        # Open the file and read the contents
        with open(os.path.join(directory_path, file), 'r') as f:
            contents = f.read()

        # Sort the contents of the file
        sorted_contents = ''.join(sorted(contents))

        # Write the sorted contents back to the file
        with open(os.path.join(directory_path, file), 'w') as f:
            f.write(sorted_contents)
