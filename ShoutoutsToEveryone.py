#Shoutouts to Everyone= Write a program to pronounce list of name using win32 API.If you are given a list l as: l=["carla","potter","Tom"]
#Your program should pronounce:- Shoutout to carla
#                                Shoutout to Potter
#                                Shoutout to Tom
#pywin32 is a Python extension that lets Python talk directly to Windows. Not “Windows-like”.Not “cross-platform”, but Real Windows internals.It’s a wrapper over Win32 APIs and COM.

import win32com.client #That line alone lets Python control:Microsoft Excel,Windows voice engine,Windows shell.

speaker = win32com.client.Dispatch("SAPI.SpVoice") #Dispatch tells “Give me a running instance of this COM object, or create one if it doesn’t exist.” 

names = ["carla", "potter", "Tom","Antara","Avnish","Mohan","Aparna","Meena"]

for name in names:
    text = f"Shoutout to {name}"
    print(text)
    speaker.Speak(text)
