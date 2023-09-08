import turtle

# Membuat layar untuk menggambar
wn = turtle.Screen()
wn.title("Gambar Bangun Datar")
wn.bgcolor("white")

# Membuat objek turtle
t = turtle.Turtle()

# Menggambar persegi panjang
t.penup()
t.goto(-50, -50)
t.pendown()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
t.penup()

# Menggambar segitiga
t.goto(-75, -50)
t.pendown()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.penup()

# Menggambar trapezium
t.goto(-90, -50)
t.pendown()
t.forward(120)
t.left(135)
t.forward(60)
t.left(45)
t.forward(60)
t.left(135)
t.forward(120)
t.penup()

# Menggambar jajar genjang
t.goto(-100, -50)
t.pendown()
t.forward(120)
t.left(135)
t.forward(60)
t.left(45)
t.forward(60)
t.left(135)
t.forward(120)
t.penup()

# Menggambar belah ketupat
t.goto(0, 50)
t.pendown()
t.left(45)
t.forward(70)
t.left(45)
t.forward(70)
t.left(135)
t.forward(70)
t.left(45)
t.forward(70)
t.penup()

# Menutup jendela ketika di-klik
wn.exitonclick()