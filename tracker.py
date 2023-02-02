import requests
import time
import tkinter as tk
import winsound

API_KEY = "token"
DOMAIN = "domain.com"

while True:
    response = requests.get(f"https://api.ip2whois.com/v2?key={API_KEY}&domain={DOMAIN}")
    data = response.json()

    if data["status"] == "error":
        root = tk.Tk()
        root.title("Domain Tracker")
        root.geometry("300x100")
        # center window
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        label = tk.Label(root, text="The domain is available!")
        label.pack()
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        root.mainloop()
        break
    else:
        print("The domain is still registered.")

    time.sleep(3600)