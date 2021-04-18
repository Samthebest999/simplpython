class simplpython:
    def display(*text: str):
        print(text)

    def files_io(filename, mode, *text: str):
        if mode == "r":
            global file_text
            file_text = open(filename, "r").read()
        if mode == "w":
            open(filename, "w").write(text)
        if mode == "rb":
            global file_text
            file_text = open(filename, "rb").read()
        if mode == "rt":
            global file_text
            file_text = open(filename, "rt").read()
        if mode == "a":
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
