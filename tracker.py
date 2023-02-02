import requests
import time
import tkinter as tk
import winsound

API_KEY = "token"
DOMAIN = "doamin.com"

while True:
    response = requests.get(f"https://api.ip2whois.com/v2?key={API_KEY}&domain={DOMAIN}")
    data = response.json()

    if data["status"] == "error":
        root = tk.Tk()
        root.title("Dominio liberado")
        root.geometry("300x100")
        # center window
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        label = tk.Label(root, text="El dominio ha expirado y ha sido liberado.")
        label.pack()
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        root.mainloop()
        break
    else:
        print("El dominio aún está activo.")

    time.sleep(3600)