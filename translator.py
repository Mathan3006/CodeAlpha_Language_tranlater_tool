from tkinter import *
from googletrans import Translator, LANGUAGES # type: ignore

# Initialize the translator
translator = Translator()

# Create the GUI window
root = Tk()
root.title("CodeAlpha - Language Translator")
root.geometry("500x400")
root.config(bg="#f0f0f0")

# Language list
languages = list(LANGUAGES.values())

# Function to perform translation
def translate_text():
    src_lang = source_lang.get()
    dest_lang = target_lang.get()
    text_to_translate = input_text.get("1.0", END)

    # Get language codes
    src_code = list(LANGUAGES.keys())[languages.index(src_lang)]
    dest_code = list(LANGUAGES.keys())[languages.index(dest_lang)]

    try:
        translated = translator.translate(text_to_translate, src=src_code, dest=dest_code)
        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)
    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, "Error: " + str(e))

# Title
Label(root, text="Language Translator", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Language dropdowns
frame = Frame(root, bg="#f0f0f0")
frame.pack(pady=5)

source_lang = StringVar()
source_lang.set("english")
OptionMenu(frame, source_lang, *languages).grid(row=0, column=0, padx=10)

target_lang = StringVar()
target_lang.set("tamil")
OptionMenu(frame, target_lang, *languages).grid(row=0, column=1, padx=10)

# Input text
Label(root, text="Enter text to translate:", bg="#f0f0f0").pack(pady=5)
input_text = Text(root, height=5, width=60)
input_text.pack(pady=5)

# Translate button
Button(root, text="Translate", command=translate_text, bg="green", fg="white").pack(pady=10)

# Output text
Label(root, text="Translated text:", bg="#f0f0f0").pack(pady=5)
output_text = Text(root, height=5, width=60)
output_text.pack(pady=5)

# Start the GUI loop
root.mainloop()
