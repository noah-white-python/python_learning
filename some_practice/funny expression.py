import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("#fffbe6")
s.title("Smirk Face!")
s.setworldcoordinates(-300, -150, 300, 350)
t.speed(0)
t.hideturtle()

def disk(x, y, r, col, border="#555"):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.pencolor(border)
    t.pensize(2)
    t.fillcolor(col)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def pen(x, y, col, size):
    t.penup(); t.goto(x, y)
    t.pendown(); t.pencolor(col); t.pensize(size)

# --- Face ---
disk(0, 0, 140, "#FFD93D", "#E6B800")

# --- Left eye (normal open) ---
disk(-50, 30, 28, "white")
disk(-44, 35, 15, "#222", "#222")
disk(-39, 40, 5, "white", "white")

# --- Right eye (squinted — just a curved line) ---
pen(78, 18, "#333", 5)
t.setheading(150)
t.circle(38, 120)

# --- Left eyebrow (normal) ---
pen(-76, 68, "#7a5000", 5)
t.goto(-50, 75); t.goto(-22, 68)

# --- Right eyebrow (raised high — smug!) ---
pen(20, 65, "#7a5000", 6)
t.goto(48, 80); t.goto(76, 68)

# --- Nose ---
disk(0, -20, 8, "#E6A800", "#cc8800")

# --- Smirk (asymmetric curl on right side) ---
pen(-40, -52, "#7a3000", 5)
t.goto(-15, -56)
t.goto(10, -50)
t.goto(30, -62)

# --- Rosy cheek (left side only, adds smugness) ---
t.penup(); t.goto(-100, -18)
t.pendown(); t.pencolor("#FF8FA3"); t.pensize(1)
t.fillcolor("#FF8FA3")
t.begin_fill()
for _ in range(2):
    t.forward(48); t.circle(12, 90)
    t.forward(24); t.circle(12, 90)
t.end_fill()

turtle.done()