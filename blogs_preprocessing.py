import os
import re

# Function to remove invalid characters from XML content
def remove_invalid_xml_characters(xml_content):
    # Eliminate the content between <date> and </date> tags
    xml_content = re.sub('<date>.*</date>', '', xml_content)
    # Eliminate all the tags
    xml_content = re.sub('<.*?>', '', xml_content)
    return xml_content

# Function to modify XML files
def modify_xml_files():
    try:
        for filename in os.listdir('blogs'):
            # Read the file contents
            file = open('blogs/' + filename, 'r', encoding='utf-8', errors='ignore')
            file_content = file.read()
            file.close()
            # Remove invalid characters from the file contents
            cleaned_content = remove_invalid_xml_characters(file_content)
            # Write the cleaned content back to the file
            file = open('blogs/' + filename, 'w')
            file.write(cleaned_content)
            file.close()
    except Exception as e:
        print(e)
        print('Error while processing file: ' + filename)

# Call the modify_xml_files function
modify_xml_files()
