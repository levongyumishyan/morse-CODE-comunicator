
# tkinter and PIl are NOT available in linux for some reason (out of the box of course)
import tkinter as tk
from pygame import mixer
from PIL import ImageTk, Image


#All the variabels before frame

prompt = "If you want to do a short press press 1 and if you want to do a long press press 2"

mixer.init(100000)

def on_key(event):

    if event.char == event.keysym:

        if event.char == '1':

            d1.play()

        if event.char == '2':

            d2.play()
try:
    d1 = mixer.Sound("morse_code2.wav")

    d2 = mixer.Sound("morse_code2(long[).wav")
except:
    print('Sound Error')

#Main frame

root = tk.Tk()
root.geometry('550x450')
root.title("Morse Code Communicator")
img = ImageTk.PhotoImage(Image.open("morse_alpha.png"))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="y", expand="yes")
label1 = tk.Label(root, text=prompt, width =len(prompt) , height=4, bg='black', fg='white')
label1.pack()
label1.bind_all('<Key>', on_key)
root.mainloop()


