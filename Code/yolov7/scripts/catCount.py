import os

folder_path = r"C:\Users\abdel\OneDrive - The British University in Egypt\Desktop\train\labels"  # Replace with the actual path to your folder

# Dictionary to store the count for each category
count_dict = {
    '0': 'Ambulance',
    '1': 'Motorcycle',
    '2': 'Bus',
    '3': 'Tractor',
    '4': 'Car',
    '5': 'Truck',
    '6': 'Person',
    '7': 'Bicycle'
}

# Initialize count for each category to 0
category_count = {category: 0 for category in count_dict.values()}

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as f:
            for line in f:
                first_char = line.strip()[0]
                if first_char in count_dict:
                    category = count_dict[first_char]
                    category_count[category] += 1

# Print the counts
for category, count in category_count.items():
    print(f"{category}: {count}")
