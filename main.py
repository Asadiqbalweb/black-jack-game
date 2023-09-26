import tkinter as tk
from blackJackGame import BlackjackGame

if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGame(root)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    game.start()
    root.mainloop()