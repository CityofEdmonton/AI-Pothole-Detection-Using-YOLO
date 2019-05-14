import os
import sys
import re
from PIL import Image

"""
This script is used to convert the format of the annotated data obtained from this dataset: http://goo.gl/Uj38Sf
"""

def separate_data_line(data_line):
    """Returns the separated image path and pothole data

    :returns: image_path, full_data
    """
    path_regex = '.*\.*\.*\.bmp'
    match = re.search(path_regex, data_line)
    image_path = match.group().replace('.bmp', '.jpg')
    data_start_index = match.span()[1]
    full_data = data_line[data_start_index:].strip()
    return image_path, full_data


def calculate_dimensions(left_x, top_y, pothole_width, pothole_height, image_width, image_height):
    """Returns a correctly formatted string in YOLOv2 format

    :returns: format_string
    """
    center_x = (left_x + (pothole_width/2)) / image_width
    center_y = (top_y + (pothole_height/2)) / image_height
    width_x = pothole_width / image_width
    height_y = pothole_height / image_height
    return ' {0} {1} {2} {3}'.format(center_x, center_y, width_x, height_y)


def process_data_line(data_dir, data_line, combined_text_file):
    """Formats the pre-existing data file and stores a formatted text file for each image"""
    image_path, full_data = separate_data_line(data_line)
    full_path = data_dir + '\\' + image_path
    text_file_path = full_path.replace('.jpg', '.txt')
    if not os.path.isfile(full_path):
        print("Could not find file: " + image_path)
        return
    # IMAGE PATH -> Convert to proper image path (data/Pothole/<img>)
    # TODO: variable image path
    image_name = image_path.split('\\')[-1]
    new_image_path = 'data/Pothole/' + image_name
    # IMAGE PATH
    combined_text_file.write(new_image_path + '\n')
    im = Image.open(full_path)
    image_width, image_height = im.size
    process_data = full_data.split(' ')
    return_string = '0'
    working_index = 1
    num_data = int(process_data[0])
    for x in range(num_data):
        left_x = process_data[working_index]
        top_y = process_data[working_index + 1]
        pothole_width = process_data[working_index + 2]
        pothole_height = process_data[working_index + 3]
        return_string += calculate_dimensions(float(left_x), float(top_y), float(pothole_width), float(pothole_height), float(image_width), float(image_height))
        working_index+=4
    with open(text_file_path, 'w') as f:
        f.write(return_string)
    f.close()


if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Invalid arguments.\nargs: <directory path> <text file to convert> <combined text file (test/train)>")
        sys.exit()

    directory_path = sys.argv[1]
    convert_text_file = sys.argv[2]
    combined_text_file = sys.argv[3]

    if not os.path.isdir(directory_path):
        print("Not a valid directory path.")
        sys.exit()
    elif not os.path.isfile(directory_path + '/' + convert_text_file):
        print("No text file found")
        sys.exit()

    print("Directory: " + directory_path)
    print("File: " + convert_text_file)
    print("File to write to: " + combined_text_file)

    while True:
        user_input = raw_input("Confirm? [Y/N]").strip().lower()
        if user_input == 'y':
            break
        elif user_input == 'n':
            sys.exit()

    with open(directory_path + '/' + convert_text_file, 'r') as f:
        data = f.readlines()
    f.close()

    with open('./' + combined_text_file, 'w') as new_file:
        new_file.close()
    c = open('./' + combined_text_file, 'a+')

    # TODO: make it more user-friendly (option to navigate and select directories/files)

    for line in data:
        process_data_line(directory_path, line, c)
    
    c.close()