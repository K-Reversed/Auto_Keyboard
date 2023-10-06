import keyboard, time, sys, tkinter as tk
class Found(Exception): pass
def press():
    window.withdraw()
    time.sleep(5)
    text = entry.get().replace(' ', '').split(',')
    print(text)
    
    try:
        while True:
            for i in text:
                if keyboard.is_pressed('F7'):
                    raise Found
                keyboard.press(i[:1])
                print(i[:1], type(i))
                time.sleep(2)
        
    except Found:
        window.deiconify()

        

window = tk.Tk()
window.geometry('200x100')
window.resizable(False,False)
window.wm_attributes('-fullscreen', False)

label = tk.Label(text='Hello, World!')
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(text='click to start', command=press)
button.pack()

window.mainloop()