import tkinter as tk


def hitung_total():
    harga = float(entry_harga.get())
    kuantitas = int(entry_kuantitas.get())
    total = harga * kuantitas
    label_total.config(text=f"Total: {total:.2f} Rupiah")


window = tk.Tk()
window.title("KASIR MASBROW")


label_harga = tk.Label(window, text="Harga:")
label_harga.pack()
entry_harga = tk.Entry(window)
entry_harga.pack()


label_kuantitas = tk.Label(window, text="Kuantitas:")
label_kuantitas.pack()
entry_kuantitas = tk.Entry(window)
entry_kuantitas.pack()


tombol_hitung = tk.Button(window, text="Hitung Total", command=hitung_total)
tombol_hitung.pack()


label_total = tk.Label(window, text="")
label_total.pack()


window.mainloop()