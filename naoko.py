import requests
import json
import time
sid=0
file_name = "sample.mp3"

def generate_audio(text):
    url = f"https://api.tts.quest/v1/voicevox?text={text}&speaker={sid}"
    response = requests.get(url).json()
    while True:
        statusurl=response["audioStatusUrl"]
        status=requests.get(statusurl).json()
        if status["isAudioReady"]:
            break
        time.sleep(1)

    audio_url = response["mp3DownloadUrl"]
    return audio_url

def save_audio(audio_url, file_name):
    audio_content = requests.get(audio_url).content
    with open(file_name, "wb") as file:
        file.write(audio_content)

def main():
    f=open(input("Input file name to speak:"),"rt")
    text = f.read().replace(' ','').replace('\t','').replace('\n','')

    print(text)
    audio_url = generate_audio(text)
    print(audio_url)
    save_audio(audio_url, file_name)

if __name__ == "__main__":
    main()
    exit(0)

