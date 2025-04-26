import threading, time, sqlite3
import pyperclip
import tkinter as tk
from tkinter import messagebox

DB = 'clipboard_history.db'
POLL_INTERVAL = 0.5  # seconds

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clips
                 (id INTEGER PRIMARY KEY, content TEXT UNIQUE, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def add_clip(text):
    conn = sqlite3.connect(DB)
    try:
        conn.execute("INSERT OR IGNORE INTO clips (content) VALUES (?)", (text,))
        conn.commit()
    finally:
        conn.close()

def get_history():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT content FROM clips ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return [r[0] for r in rows]

def watch_clipboard(app):
    last = ''
    while True:
        try:
            content = pyperclip.paste()
            if content and content != last:
                last = content
                add_clip(content)
                app.refresh_list()
        except Exception:
            pass
        time.sleep(POLL_INTERVAL)

class ClipboardApp:
    def __init__(self, root):
        self.root = root
        root.title("Clipboard Manager")
        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(padx=10, pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Copy", command=self.copy_selected).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Clear All", command=self.clear_history).grid(row=0, column=1, padx=5)

        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for item in get_history():
            self.listbox.insert(tk.END, item)

    def copy_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Info", "Select an entry first")
            return
        text = self.listbox.get(sel)
        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Copied to clipboard!")

    def clear_history(self):
        if messagebox.askyesno("Confirm", "Delete all history?"):
            conn = sqlite3.connect(DB)
            conn.execute("DELETE FROM clips")
            conn.commit()
            conn.close()
            self.refresh_list()

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = ClipboardApp(root)

    # start watcher thread
    t = threading.Thread(target=watch_clipboard, args=(app,), daemon=True)
    t.start()

    root.mainloop()
