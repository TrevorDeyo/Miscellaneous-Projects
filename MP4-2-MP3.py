# this code sucks

import os
import subprocess

def convert_mp4_to_mp3(directory):
    # Get the list of files in the directory
    files = os.listdir(directory)
    total_files = len(files)

    # Initialize progress variables
    converted_count = 0
    failed_count = 0

    # Process each file
    for filename in files:
        # Check if the file has an MP4 extension
        if filename.endswith('.mp4'):
            # Remove the last occurrence of the square brackets along with the content inside them
            new_filename = filename.rsplit('[', 1)[0]

            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

            # Convert MP4 to MP3 using ffmpeg command-line tool
            mp3_filename = new_filename.rsplit('.', 1)[0] + '.mp3'
            input_file = os.path.join(directory, new_filename)
            output_file = os.path.join(directory, mp3_filename)

            try:
                command = f'ffmpeg -i "{input_file}" -codec:a libmp3lame -qscale:a 2 "{output_file}"'
                subprocess.check_output(command, shell=True)

                # Remove the original MP4 file
                os.remove(input_file)

                print(f'Converted "{filename}" to "{mp3_filename}"')
                converted_count += 1
            except subprocess.CalledProcessError as e:
                print(f'Error converting "{filename}": {e}')
                failed_count += 1

    print('Conversion completed.')
    print(f'Total files: {total_files}')
    print(f'Converted files: {converted_count}')
    print(f'Failed conversions: {failed_count}')

# Specify the directory where the files are located
directory = r'C:\Users\tdeyo\Desktop\Code\MiscProjects\mp4s'

# Convert MP4 to MP3
convert_mp4_to_mp3(directory)
