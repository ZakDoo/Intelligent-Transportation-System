import os
import pandas as pd
from datetime import datetime
import os.path
import shutil


def files_into_batches(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = os.listdir(input_folder)
    num_files = len(files)
    batch_size = (num_files + 13 - 1) // 13

    for i in range(0, num_files, batch_size):
        batch_files = files[i:i + batch_size]
        batch_folder = os.path.join(output_folder, f'batch_{i // batch_size + 1}')
        os.makedirs(batch_folder, exist_ok=True)
        for file in batch_files:
            file_path = os.path.join(input_folder, file)
            shutil.copy(file_path, batch_folder)



def process_txt(root_folder, output_folder):
    # Function to replace second integer with corresponding word
    def replace_second_integer(second_integer):
        replacements = {
            '0': 'Ambulance',
            '1': 'Motorcycle',
            '2': 'Bus',
            '3': 'Tractor',
            '4': 'Car',
            '5': 'Truck',
            '6': 'Person',
            '7': 'Bicycle'
        }
        return replacements.get(second_integer, second_integer)

    # Set to store the unique first integers across all TXT files
    first_integers = set()

    # Function to process the text files in a folder
    def process_folder(folder_path):
        # Get the folder name to create the new text file
        folder_name = os.path.basename(folder_path)
        output_file = os.path.join(output_folder, f"{folder_name}.txt")

        # Set to store the unique first integers within the current folder
        folder_first_integers = set()

        # Process each text file in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        line = line.strip()
                        if line:
                            integers = line.split()
                            if len(integers) >= 2:
                                first_integer = integers[0]
                                second_integer = integers[1]
                                if first_integer not in first_integers:
                                    first_integers.add(first_integer)
                                    folder_first_integers.add(first_integer)
                                    replaced_second_integer = replace_second_integer(second_integer)
                                    output_line = f"{first_integer} {replaced_second_integer}\n"
                                    with open(output_file, 'a') as output:
                                        output.write(output_line)

        # Remove duplicates from the output file
        with open(output_file, 'r') as file:
            lines = file.readlines()
            lines = list(set(lines))
        with open(output_file, 'w') as file:
            file.writelines(lines)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Traverse each folder in the root folder
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            process_folder(folder_path)



def VType_csv(folder_path, output_csv):
    # Lists to store the integer and string values
    integers = []
    strings = []

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            # Read each line in the file
            with open(file_path, "r") as file:
                for line in file:
                    # Split the line by whitespace
                    elements = line.split()
                    if len(elements) >= 2:
                        # Extract the integer and string values from the line
                        try:
                            integer_value = int(elements[0])
                            string_value = elements[1]
                            integers.append(integer_value)
                            strings.append(string_value)
                        except ValueError:
                            pass

    # Create a DataFrame from the lists of integers and strings
    data = pd.DataFrame({"Vehicle ID": integers, "Vehicle Type": strings})

    # Write the data to a CSV file
    data.to_csv(output_csv, index=False)

def VCount_CSV(folder_path, csv_file):
    data = []
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                first_integer = int(lines[0].split()[0])
                count = len(lines)
                data.append([current_time, count, 1, 100])

    df = pd.DataFrame(data, columns=["Time", "Lane 1 Flow (Veh/5 Minutes)", "# Lane Points", "% Observed"])
    if os.path.isfile(csv_file):
        existing_df = pd.read_csv(csv_file)
        df = pd.concat([existing_df, df], ignore_index=True)

    df.to_csv(csv_file, index=False)
