# Waifu Speech
Waifu Speech is a program for changing voices into female anime voices.

### How does Waifu Speech work
<img src="/assets/images/structure.png" />
If you look at the diagram there are 4 processes in this program. Because Voicevox only supports Japanese, it needs to change the text of the audio that we previously processed into Japanese

### How do I run this program
To run this very simple program, you need Python version 3.7++ because this program uses Python, so make sure you have Python installed on your computer.

#### Install modules
- Windows, Linux, Mac
``` konsole
pip install -r requirements.txt
```
*  I'm not sure it will work on all platforms but you can give it a try. I tried it on linux

If already installed
``` konsole
python3 main.py
```
or
``` konsole
python main.py
```
(I'm using the first method because im using python 3.xx)

### Troubleshooting
- Linux

If there are problems when converting audio, try installing flac 

Activate debug mode if the error persists to view the error log. Don't forget to send the error log to the issue to be fixed

### License
[see: LICENSE](/LICENSE)

### Modify (customized.)
- Linux
  
  got Waifu-Speech takes input from Japanese text file and renamed to 'eriko.py', by fygar256.
