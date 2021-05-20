import PySimpleGUI as gui
import speech_recognition as speech
import nltk
from nltk.corpus import wordnet as wn

def get_text_from_voice():
    with speech.Microphone(device_index=1) as microphone:
        recognizer.adjust_for_ambient_noise(microphone)
        voice = recognizer.record(microphone, duration=6)
        text = recognizer.recognize_google(voice, language='en-US')
        return text


def processing(text):
    list_of_words = [i.lower() for i in text.split()]
    for i in list_of_words:
        print()
        try:
            print(i + ":", "-".join((entries[i])[0]))
        except:
            print(i + ":", "Word not found!")
        try:
            synsets = wn.synsets(i)
            for j in synsets[:3]:
                print("Definition:", j.definition())
                print("Synonims:", [k.name() for k in j.lemmas()])
        except:
            print("Cannot find word in wordnet!")
        

def main():
    layout = [
        
        [gui.Button('', image_filename='./images/microphone.png', image_size=(100, 100), image_subsample=2, border_width=2, key='Push')],
        [gui.Text('Push to Start', size=(100, 1), justification='center', font=("Times New Roman", 16))],
        [gui.Text('Transcription - ARPABET', size=(200, 1), justification='left', font=("Times New Roman", 10))],
        [gui.Output(size=(200, 50))]
    ]

    window = gui.Window('Marii Pavlo, KN-310, Course Work, Natural Language', layout, location=(100, 50), size=(1200, 600),
                       font=("Times New Roman", 12), element_justification='c')
    while True:
        event, values = window.read(timeout=100)
        if event == 'Exit' or event == gui.WIN_CLOSED:
            break
        elif event == 'Push':
            print('Say: ', end="")
            try:
                text = get_text_from_voice()
                print(text)
                processing(text)
            except:
                print('Sorry, something went wrong, try again!')

if __name__ == '__main__':
    gui.theme('DarkBlue')
    entries = nltk.corpus.cmudict.dict()
    recognizer = speech.Recognizer()
    main()