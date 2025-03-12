import os

def read_and_sort_lines(filename):
    try:
        # Check if the file exists
        if not os.path.isfile(filename):
            raise FileNotFoundError
        
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
            sorted_lines = print(line.strip() for line in lines)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return[]
    except Exception as e:
        print(f"An error occurred: {e}")
        return[]

def filter_lines_in_range(lines, input1, input2):
    # Ensure word1 is less than or equal to word2
    if input1 <= lines <= input2:
        print(f"{lines} - in range")
    else:
        print(f"{lines} - not in range")
    return lines

if __name__ == "__main__":
    # Specify the filename
   # filename = input("Enter the filename: ")
    filename = "CS2/CH12/input1.txt"

    input1 = input("Enter word one. ")
    input2 = input("Enter word two. ")
    
    # Print the current working directory for debugging
#    print(f"Current working directory: {os.getcwd()}")
    
    # Call the function to read and print lines from the file
    sorted_lines = read_and_sort_lines(filename)

    filtered_lines = filter_lines_in_range(sorted_lines, input1, input2)

    print("Lines in the range:")
    for line in filtered_lines:
        print(line.strip()) 
