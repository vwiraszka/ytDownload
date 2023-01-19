import PySimpleGUI as sg
from pytube import YouTube
import threading
import time
from sys import argv

#Setting the app theme
sg.theme('DarkPurple4')

video_resolutions = []
def fetch_resolution(link):
    yt = YouTube(link)
    for stream in yt.streams.filter(subtype='webm', progressive=False).order_by('resolution'):
        video_resolutions.append(stream.resolution)

#link = "https://www.youtube.com/watch?v=iicfmXFALM8"




if __name__ == '__main__':
    layout = [[sg.Text('Please paste the link to the video you want to download:'), sg.InputText(key='-LINK-')],
              [sg.Button('Submit', enable_events=True)],
              [sg.Text('Choose quality: '), sg.Combo(values=['   '], key='-RES-', readonly=True, disabled=True, enable_events=True)],
              [sg.Button('Cancel')]]
    window = sg.Window('Window Title', layout)
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        elif event == "Submit":
            link = values['-LINK-']
            fetch_resolution(link)
            #sg.popup("jebac pis", video_resolutions)
            window['-RES-'].Update(values=video_resolutions, disabled=False)
            layout += [[sg.Text("")]]

    window.close()

