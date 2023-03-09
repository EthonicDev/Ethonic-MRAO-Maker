import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

file_path = ""

def select_file(entry):
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def combine_textures():
    metallic_path = metallic_entry.get()
    roughness_path = roughness_entry.get()
    ambient_path = ambient_entry.get()
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "mrao.png")

    try:
        metallic = Image.open(metallic_path).convert("L")
        roughness = Image.open(roughness_path).convert("L")
        ambient = Image.open(ambient_path).convert("L")
        mrao = Image.merge("RGB", (ambient, roughness, metallic))

        mrao.save(output_path, format="PNG")

        messagebox.showinfo("Info", "Your Textures Have Been Combined")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.config(bg="#1c1c1c")
root.title("Ethonic's MRAO Texture Combiner")
root.iconbitmap("icon.ico")

metallic_label = tk.Label(root, relief=tk.FLAT, text="Metallic Texture:", bg="#333", fg="white")
metallic_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)

metallic_entry = tk.Entry(root, relief=tk.FLAT, bg="#2d2d2d", fg="white", width=50)
metallic_entry.grid(row=0, column=1, padx=5, pady=5)

metallic_button = tk.Button(root, relief=tk.RAISED, text="Select", bg="#444", fg="white", command=lambda: select_file(metallic_entry))
metallic_button.grid(row=0, column=2, padx=5, pady=5)

roughness_label = tk.Label(root, relief=tk.FLAT, text="Roughness Texture:", bg="#333", fg="white")
roughness_label.grid(row=1, column=0, sticky="W", padx=5, pady=5)

roughness_entry = tk.Entry(root, relief=tk.FLAT, bg="#2d2d2d", fg="white", width=50)
roughness_entry.grid(row=1, column=1, padx=5, pady=5)

roughness_button = tk.Button(root, relief=tk.RAISED, text="Select", bg="#444", fg="white", command=lambda: select_file(roughness_entry))
roughness_button.grid(row=1, column=2, padx=5, pady=5)

ambient_label = tk.Label(root, relief=tk.FLAT, text="Ambient Occlusion Texture:", bg="#333", fg="white")
ambient_label.grid(row=2, column=0, sticky="W", padx=5, pady=5)

ambient_entry = tk.Entry(root, relief=tk.FLAT, bg="#2d2d2d", fg="white", width=50)
ambient_entry.grid(row=2, column=1, padx=5, pady=5)

ambient_button = tk.Button(root, relief=tk.RAISED, text="Select", bg="#444", fg="white", command=lambda: select_file(ambient_entry))
ambient_button.grid(row=2, column=2, padx=5, pady=5)

output_label = tk.Label(root, relief=tk.FLAT, text="Output:", bg="#333", fg="white")
output_label.grid(row=3, column=0, sticky="W", padx=5, pady=5)

#output_entry = tk.Entry(root, relief=tk.FLAT, bg="#2d2d2d", fg="white", width=50)
#output_entry.grid(row=3, column=1, padx=5, pady=5)
text_label = tk.Label(root, relief=tk.FLAT, text="outputs as mrao.png in same directory", height=1, width=40, bg="#333", fg="white", wraplength=450)
text_label.grid(row=3, column=1, padx=5, pady=5)

#output_button = tk.Button(root, relief=tk.FLAT, text="Select", bg="#333", fg="white", command=lambda: filedialog.asksaveasfilename(defaultextension=".png"))
#output_button.grid(row=3, column=2, padx=5, pady=5)

combine_button = tk.Button(root, relief=tk.RAISED, borderwidth=2, highlightthickness=2, text="Combine Textures", bg="#444", fg="white", command=combine_textures)
combine_button.grid(row=4, columnspan=3, padx=5, pady=5)

text_label = tk.Label(root, relief=tk.FLAT, text="This program that I made because I can't find any free programs that easily do this. I had a bunch of errors with output so It currently just outputs the file as mrao.png in the same directory as this.", width=45, height=5, bg="#333", fg="white", wraplength=300)
text_label.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()