def display(what_to_display):
    print(what_to_display)


def files_io(filename, mode, text_to_use):
    if "r" in mode:
        global file_contents
        file_contents = open(filename, "r").read()
    if "w" in mode:
        open(filename, "w").write(text_to_use)

def TTS(what_to_say, language, slow_true_or_false):
    from gtts import gTTS
    from playsound import playsound
    import os
    gts = gTTS(text=what_to_say, lang=language, slow=slow_true_or_false)
    gts.save("TTS_TEMP.mp3")
    playsound("TTS_TEMP.mp3")
    if os.path.exists("TTS_TEMP.mp3"):
        os.remove("TTS_TEMP.mp3")
