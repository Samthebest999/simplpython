class simplpython:
    def display(text: str):
        print(text)

    def files_io(filename, mode, text: str):
        if "r" in mode:
            global file_text
            file_text = open(filename, "r").read()
        if "w" in mode:
            open(filename, "w").write(text)

    def TTS(speak: str, language: str, slow_true_or_false: bool):
        from gtts import gTTS
        from playsound import playsound
        import os
        gts = gTTS(text=speak, lang=language, slow=slow_true_or_false)
        gts.save("TTS_TEMP.mp3")
        playsound("TTS_TEMP.mp3")
        if os.path.exists("TTS_TEMP.mp3"):
            os.remove("TTS_TEMP.mp3")
