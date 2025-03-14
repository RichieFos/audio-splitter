from pydub import AudioSegment
import math
import re

def get_file_extension(filename):
    match = re.search(r'\.\w+$', filename)
    if match:
        extension = match.group(0).removeprefix(".")
        return extension
    else:
        return None

def main():
    old_audio = "Nixon.wav"
    file_extension = get_file_extension(old_audio)
    original_audio = AudioSegment.from_mp3(old_audio)

    duration = len(original_audio)

    # Calculate the number of 4-minute 59 second chunks needed
    chunks = math.ceil(duration / 299999)

    for x in range(chunks):
        starttime = x * 299999
        endtime = min((x + 1) * 299999, len(original_audio))  

        chunk = original_audio[starttime:endtime]

        newfilename = f"newAudio{x + 1}.{file_extension}"
        chunk.export(newfilename, format=file_extension)

    print(f"Exported {chunks} files.")

if __name__ == "__main__":
    main()