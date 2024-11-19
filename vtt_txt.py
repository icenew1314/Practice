import os

def convert_vtt_to_txt(vtt_file_path, txt_file_path):
    with open(vtt_file_path, 'r', encoding='utf-8') as vtt_file:
        lines = vtt_file.readlines()

    # Filter out the timestamps and metadata, keep only the text lines
    text_lines = []
    for line in lines:
        if '-->' not in line and line.strip() != '' and not line.startswith('WEBVTT'):
            text_lines.append(line.strip())

    # Write the filtered lines to a txt file
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write('\n'.join(text_lines))

def batch_convert_vtt_to_txt(folder_path):
    # Iterate over all files in the given folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.vtt'):
            vtt_file_path = os.path.join(folder_path, filename)
            txt_file_path = os.path.join(folder_path, filename.replace('.vtt', '.txt'))
            convert_vtt_to_txt(vtt_file_path, txt_file_path)
            print(f'Converted: {filename} -> {filename.replace(".vtt", ".txt")}')

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing VTT files: ")
    if os.path.isdir(folder_path):
        batch_convert_vtt_to_txt(folder_path)
    else:
        print("Invalid folder path")
