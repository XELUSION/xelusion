import turtle as t

# Membuat jendela untuk menggambar
window = t.Screen()
window.title("Gambar Tangan Menggunakan Turtle")

# Membuat objek turtle
pen = t.Turtle()
pen.speed(1)  # Mengatur kecepatan turtle

# Menggambar tangan
pen.fillcolor("#ffe4b5")  # Mengatur warna kulit tangan
pen.begin_fill()

# Menggambar jari-jari tangan
pen.goto(0, 0)
pen.circle(50, 180)  # Setengah lingkaran (tangan)

# Menggambar garis telunjuk
pen.left(45)
pen.forward(100)

# Menggambar ujung telunjuk
pen.left(45)
pen.forward(30)

# Menggambar garis tengah
pen.backward(30)
pen.right(45)
pen.forward(40)

# Menggambar garis kelingking
pen.right(45)
pen.forward(30)

# Kembali ke tengah tangan
pen.right(45)
pen.backward(40)

# Menggambar ibu jari
pen.right(90)
pen.forward(50)

# Menggambar punggung tangan
pen.right(90)
pen.forward(150)
pen.left(90)

# Menggambar pangkal ibu jari
pen.forward(50)

pen.end_fill()

# Menggambar kuku jari telunjuk
pen.fillcolor("white")
pen.penup()
pen.goto(20, 60)
pen.pendown()
pen.begin_fill()
pen.goto(25, 70)
pen.goto(35, 70)
pen.goto(35, 60)
pen.goto(20, 60)
pen.end_fill()

# Menutup jendela saat di-klik
window.exitonclick()