import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
import time
import threading

class PDFWordDisplay:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Word Display")
        self.root.geometry("500x300")
        
        self.label = tk.Label(root, text="Open a PDF to start", font=("Helvetica", 24), wraplength=400)
        self.label.pack(pady=50)

        self.wpm_scale = tk.Scale(root, from_=60, to=600, orient="horizontal", label="Words per Minute (WPM)")
        self.wpm_scale.pack()
        self.wpm_scale.set(200)

        self.words_at_once = tk.Scale(root, from_=1, to=3, orient="horizontal", label="Words at Once")
        self.words_at_once.pack()
        self.words_at_once.set(1)

        self.open_button = tk.Button(root, text="Open PDF", command=self.open_pdf)
        self.open_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_display, state="disabled")
        self.stop_button.pack()

        self.words = []
        self.current_index = 0
        self.running = False

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.extract_words_from_pdf(file_path)
            self.start_display()

    def extract_words_from_pdf(self, file_path):
        self.words = []
        document = fitz.open(file_path)
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text = page.get_text()
            self.words.extend(text.split())
        document.close()

    def start_display(self):
        self.running = True
        self.current_index = 0
        self.stop_button.config(state="normal")
        threading.Thread(target=self.display_words).start()

    def stop_display(self):
        self.running = False
        self.stop_button.config(state="disabled")

    def display_words(self):
        while self.running and self.current_index < len(self.words):
            wpm = self.wpm_scale.get()
            delay = 60 / wpm
            words_at_once = self.words_at_once.get()
            words_to_display = " ".join(self.words[self.current_index:self.current_index + words_at_once])
            self.current_index += words_at_once
            
            self.label.config(text=words_to_display)
            time.sleep(delay)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFWordDisplay(root)
    root.mainloop()
