import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image 
import PIL.ImageTk

def disphoto(path):
    #画像を読み込む
    newImage = PIL.Image.open(path).resize((32,32)).convert("L").resize((300,300))
    #画像をTkinterで表示できるように変換する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData
    #画像を表示す

def openfile():
    path = fd.askopenfilename()
    
    if path:
        disphoto(path)

root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(text="画像を選択", command=openfile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()

    

