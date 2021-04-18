class simplpython:
    def display(*text: str):
        print(text)

    def files_io(filename, mode, *text: str):
        if "r" == mode:
            global file_text
            file_text = open(filename, "r").read()
        if "w" == mode:
            open(filename, "w").write(text)
        if "rb" == mode:
            global file_text
            file_text = open(filename, "rb").read()
        if "rt" == mode:
            global file_text
            file_text = open(filename, "rt").read()
        if "a" == mode:
            open(filename, "a").write(text)

    def TTS(speak: str, language: str, slow: bool):
        from gtts import gTTS
        from playsound import playsound
        import os
        gts = gTTS(text=speak, lang=language, slow=slow_true_or_false)
        gts.save("TTS_TEMP.mp3")
        playsound("TTS_TEMP.mp3")
        if os.path.exists("TTS_TEMP.mp3"):
            os.remove("TTS_TEMP.mp3")
