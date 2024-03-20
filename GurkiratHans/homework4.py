def check_file_size(filepath):
    try:
        # Open the file in read mode
        with open(filepath, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Check if the length of content is greater than 1
            return len(content) > 1
    except FileNotFoundError:
        print("File not found.")
        return False

# Test the function
file_path = input("Enter the filepath: ")
print(check_file_size(file_path))