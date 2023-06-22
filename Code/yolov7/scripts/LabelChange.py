import os

input_folder = r"C:\Users\abdel\OneDrive - The British University in Egypt\Desktop\train/labels"
output_folder = r"C:\Users\abdel\OneDrive - The British University in Egypt\Desktop\train\labelsNew"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)

        with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
            for line in input_f:
                if line.strip():
                    first_char = line[0]
                    if first_char == '0':
                        modified_line = '2' + line[1:]
                    elif first_char == '1':
                        modified_line = '4' + line[1:]
                    elif first_char == '2':
                        modified_line = '1' + line[1:]
                    elif first_char == '3':
                        modified_line = '5' + line[1:]
                    else:
                        modified_line = line

                    output_f.write(modified_line)
