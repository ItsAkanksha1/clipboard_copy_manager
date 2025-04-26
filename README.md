# 📋 Clipboard Copy Manager

A lightweight Python-based clipboard history tracker with a GUI and local storage. Monitors clipboard content, stores unique entries, and lets you reuse or manage your copy history easily.

## 🚀 Features

- 🔄 Real-time clipboard monitoring
- 🧠 Smart history: stores only unique entries
- 💾 Local SQLite database for persistent storage
- 🖱️ User-friendly GUI built with Tkinter
- 📋 One-click re-copy to clipboard
- ❌ Clear entire clipboard history with confirmation

## 🛠️ Tech Stack

- Python 3.x
- Tkinter (GUI)
- `pyperclip` (Clipboard access)
- SQLite3 (Database)

## 📂 Project Structure

```
clipboard_copy_manager/
├── clipboard_manager.py      # Main script
├── clipboard_history.db      # SQLite DB (auto-created on first run)
└── README.md
```

## ✅ Requirements

Install required dependencies:

```bash
pip install pyperclip
```

> Tkinter comes pre-installed with Python. If not, install via your package manager.

## 🧪 How to Run

```bash
python clipboard_manager.py
```

The app will:
- Start a background thread to monitor your clipboard.
- Log new, unique copies to a local SQLite database.
- Display all entries in a listbox for reuse.

## 🧼 Optional: Clear History

- Use the **Clear All** button in the GUI.
- Confirm before deleting everything.

## 🔐 Security

- All clipboard data is stored **locally only**.
- Uses SQLite with `INSERT OR IGNORE` to avoid duplicates.

## 🙌 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Request features
- Submit pull requests

## 📄 License

MIT License © 2025 [Akanksha](https://github.com/ItsAkanksha1)
