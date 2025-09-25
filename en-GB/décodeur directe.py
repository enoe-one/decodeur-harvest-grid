import tkinter as tk
from tkinter import filedialog, messagebox, BooleanVar
import zlib
import base64
import os

def decode_save(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    try:
        compressed = base64.b64decode(data)
        json_bytes = zlib.decompress(compressed)
        txt = json_bytes.decode("utf-8")
        with open(output_file, "w") as out:
            out.write(txt)
        messagebox.showinfo("Succès", f"Decoded file : {output_file}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Unable to decode : {e}")

def encode_save(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    try:
        compressed = zlib.compress(data.encode("utf-8"))
        b64 = base64.b64encode(compressed).decode("utf-8")
        with open(output_file, "w") as out:
            out.write(b64)
        messagebox.showinfo("Succès", f"Encoded file : {output_file}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Unable to encode : {e}")

def select_file():
    file_path = filedialog.askopenfilename(title="Select a file")
    if not file_path:
        return
    sense_inverse = inverse_var.get()
    file_dir, file_name = os.path.split(file_path)
    if sense_inverse:

        output_file = os.path.join(file_dir, file_name + ".save")
        encode_save(file_path, output_file)
    else:
        output_file = os.path.join(file_dir, file_name + ".txt")
        decode_save(file_path, output_file)

root = tk.Tk()
root.title("Harvest Grid Save Tool")

tk.Label(root, text="Harvest Grid Backup Decoder/Encoder").pack(pady=8)
inverse_var = BooleanVar()
tk.Checkbutton(root, text="Sens inverse (JSON → backup)", variable=inverse_var).pack()
tk.Button(root, text="Select a file", command=select_file).pack(pady=12)
tk.Label(root, text="• To decode: select a .save file\n• To encode: tick the box and select a .txt or .json file").pack(pady=8)

root.mainloop()