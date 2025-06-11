import os
if __name__ == '__main__':

    while True:
        x = input("Enter what you want to say :")
        if x.lower()=="exit":
            break
        command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(command)