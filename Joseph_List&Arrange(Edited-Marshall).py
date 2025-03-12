import os

def read_and_sort_lines(filename):
    try:
        # Check if the file exists
        if not os.path.isfile(filename):
            raise FileNotFoundError
        
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read all lines from the file
            """The line below was changed because the file was first being
                read then stripped originally.
                For better readability, the file needs to be separated first,
                then read the file's information to prepare for sorting."""
            lines = [line.strip() for line in file.readlines()]
            
            """This function below sorts the line alphabetically."""
            lines.sort()

            return lines

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return[]

    except Exception as error:
        print(f"An error occurred: {error}")
        return[]


def filter_lines_in_range(lines, input1, input2):
    """Learned that lines being a list and input1 and input2 being a
        string is a comparasion that doesn't work. To fix it we needed
        to 'iterate over each line' to check it it's within the range."""

    filtered_lines = [] # Empty list to store appended sorted objects.

    """This loop through each element in the list (filtered_lines)
        and compares the individual strings to input1 and input2,
        rather than trying to compare the entire list."""    
    for line in lines:
        if input1 <= line <= input2:
            print(f"{line} - in range")
            filtered_lines.append(line)
        
        else:
            print(f"{line} - not in range")

    return filtered_lines # Returned the newly filtered lines instead of original list.

if __name__ == "__main__":
    # Inputs for filename and Range:
    filename = input("Enter txt file name: ")
    input1 = input("Enter word one. ")
    input2 = input("Enter word two. ")
    
    # Print the current working directory for debugging
#    print(f"Current working directory: {os.getcwd()}")
    
    # Call the function to read and print lines from the file
    sorted_lines = read_and_sort_lines(filename)

    if not sorted_lines:
        print("No lines to process.")
    else:
        filtered_lines = filter_lines_in_range(sorted_lines, input1, input2)

        """ I took out these lines 
                print("Lines in the range:")
                for line in filtered_lines:
                    print(line)
            because it was printing an extra sorted list except it
            didn't include the ' - in range' next to the words
            between ammoniated and millennium."""
