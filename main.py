from pydub import AudioSegment
import math

old_audio = "Nixon.wav"

def main():
    # Load the original audio file
    original_audio = AudioSegment.from_mp3(old_audio)

    duration = len(original_audio)

    # Calculate the number of 5-minute chunks needed
    chunks = math.ceil(duration / 299999)

    for x in range(chunks):
        starttime = x * 299999
        endtime = min((x + 1) * 299999, len(original_audio))  

        chunk = original_audio[starttime:endtime]

        newfilename = f"newAudio{x + 1}.wav"
        chunk.export(newfilename, format="wav")

    print(f"Exported {chunks} files.")

if __name__ == "__main__":
    main()