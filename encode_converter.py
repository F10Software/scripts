import os
import sys
import chardet
import codecs
import pathlib

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

def convert_encoding(input_path, output_path, from_encoding, to_encoding='utf-8'):
    with codecs.open(input_path, 'r', from_encoding) as file:
        content = file.read()
    with codecs.open(output_path, 'w', to_encoding) as file:
        file.write(content)

def main():
    if len(sys.argv) != 4:
        print("Usage: python convert_encoding.py <source_folder> <destination_folder> <encode_name>")
        sys.exit(1)

    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]
    encod_target = sys.argv[3]

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if pathlib.Path(file).suffix in ('.pas', '.dfm'):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_folder, file)
                encod_source = detect_encoding(source_file)
                print(f"Converting the {source_file} file, encoded as {encod_source} to {encod_target} encoding")
                convert_encoding(source_file, destination_file, encod_source, encod_target)

main()