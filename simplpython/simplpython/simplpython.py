class simplpython:
    def display(*text: str):
        print(text)

    def files_io(self, filename, mode, *text: str):
        if mode == "r":
            file_text = open(filename, "r").read()
            return file_text
        if mode == "w":
            for content in text:
                open(filename, "w").write(content)
        if mode == "rb":
            file_text = open(filename, "rb").read()
            return file_text
        if mode == "rt":
            file_text = open(filename, "rt").read()
            return file_text
        if mode == "a":
            for content in text:
                open(filename, "a").write(content)

    def TTS(self, speak: str, language: str, slow: bool):
        from gtts import gTTS
        from playsound import playsound
        import os
        gts = gTTS(text=speak, lang=language, slow=slow)
        gts.save("TTS_TEMP.mp3")
        playsound("TTS_TEMP.mp3")
        if os.path.exists("TTS_TEMP.mp3"):
            os.remove("TTS_TEMP.mp3")
