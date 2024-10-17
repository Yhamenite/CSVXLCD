import os
import sys
import numpy as np
import pandas as pd
import functools as ft



def main():
    # This block is for getting the input directory from the user, store all files in a list for later processing, and creating the output directory
    input_directory = get_input_directory()
    files = list_files(input_directory)
    output_directory = check_and_create_output_dir()


    # Get all deletion ranges from the user
    deletion_ranges = get_deletion_ranges()
    
    # Convert the deletion ranges provided by the user to pandas index
    pandas_index = ranges_as_pandas_index(deletion_ranges)

    # Prepare the list of columns to be deleted
    columns_to_be_deleted = columns_to_delete(pandas_index)

    # Process all the files in the input directory
    process_files(columns_to_be_deleted,files,input_directory,output_directory)



def to_color(string, color):
    color_code = {  'blue': '\033[34m',
                    'yellow': '\033[33m',
                    'green': '\033[32m',
                    'red': '\033[31m'
                    }
    return color_code[color] + str(string) + '\033[0m'


def get_input_directory():
    return input(f"{to_color("[*]","blue")} Please provide the input directory: ")
    

# Store all the files in the input directory in a list for later processing
def list_files(input_directory):
    files = os.listdir(input_directory)
    if (len(files) == 0):
        sys.exit(f"{to_color("[X]", "red")} There are no files in the provided directory")
    print(f"{to_color("[+]","green")} Files found in {input_directory}!")
    print()
    return files


# Create the output directory, and returns its name
def check_and_create_output_dir():
    print(to_color("[*]","blue")+" "+"Creating output directory")

    # Check to see if the directory exists, if not then create one
    if os.path.exists("03-deleted_unwanted_features"):
        print(to_color("[-]","yellow")+" "+"Output directory: 03-deleted_unwatned_featues already exists!")
        print()
    else:
        os.mkdir("03-deleted_unwanted_features")
        print(to_color("[+]","green")+" "+"Output directory: 03-deleted_unwanted_features has been created successfully!")
        print()
    return "03-deleted_unwanted_features"


# Convert Excel column letter to pandas df.columns[] index
# Example: excel2pandas("A") ---Output---> 1 
def excel2pandas(x): 
    return ft.reduce(lambda s,a:s*26+ord(a)-ord('A')+1, x, 0) - 1


# Get the deletion ranges from user
def get_deletion_ranges():
    # Educating user to use the correct syntax
    print(to_color("[*]", "blue")+" "+"Please insert as many ranges as you want, make sure to follow the following syntax: A,F,AO,BD")
    print("This will delete the following ranges from the file: [A->F], [AO->BD]")

    # Putting ranges to list
    ranges = input("Deletion ranges: ")
    ranges_split = ranges.split(",")
    
    # Converting every letter in the range to upper case letters
    ranges_split = capitalize_elements(ranges_split)
    print()

    # Check to see whether the nubmer of inputs is correct
    if (check_even(len(ranges_split)) == True):

        # Print the deletion ranges
        print(to_color("[+]","green")+" "+"The ranges that will be deleted are:")
        for interval in range(len(ranges_split)):
            if (check_even(interval) == True):
                print(f"[{ranges_split[interval]} ---> {ranges_split[interval+1]}]")
    else:
        print(to_color("[X]","red"), "The number of passed inputs is not correct! Each range must have a start and an end.")
        sys.exit()

    print()
    return ranges_split


def capitalize_elements(list):
    capitalized_list = []
    for element in list:
        capitalized_list.append(element.upper())
    return capitalized_list


# Returns true if the nubmer is even, false otherwise
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    

# Converts the ranges provided by the user to pandas index
def ranges_as_pandas_index(list):
    pandas_index = []
    print(to_color("[*]","blue")+" "+"Converting ranges to pandas index")
    for element in list:
        pandas_index.append(excel2pandas(element))
    print(to_color("[+]","green")+" "+"Ranges converted to pandas index successfully!")
    print()
    return pandas_index


# Returns the list of columns to be deleted
def columns_to_delete(pandas_index):
    columns_to_be_deleted = []
    print(to_color("[*]","blue")+" "+"Preparing the list of columns to be deleted")
    for x in range(0, len(pandas_index), 2):
        columns_to_be_deleted.extend(range(pandas_index[x], pandas_index[x+1]+1))
    print(to_color("[+]","green")+" "+"List of columns to be deleted prepared successfully!")
    print()
    return columns_to_be_deleted


def process_files(columns_to_be_deleted,files,input_directory,output_directory):
    # print(columns_to_be_deleted)
    for file in files:
        df = pd.read_csv(input_directory+"\\"+file)
        print(df.shape[1], file)
    sys.exit()
    # print(excel2pandas("GE"))
    # print(files[152])
    # df = pd.read_csv(input_directory+"\\"+files[153])
    # print(df.columns[186])
    # sys.exit()
    counter = 1
    print(to_color("[*]","blue")+" "+"Processing files")
    for file in files:
        df = pd.read_csv(input_directory+"\\"+file)
        df.drop(df.columns[columns_to_be_deleted], axis=1).to_csv(output_directory+"\\"+file, index = False)
        print(f"{to_color("[+]","green")} File: {file} processed successfully! (number #{counter})")
        files.remove(file)
        counter += 1
    print()
    print(f"{to_color("[*]","blue")} Processed {counter - 1} files successfully!")



if __name__ == "__main__":
    main()