import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Cosmic Cafe ☕🌸 – Emotional Edition")
root.geometry("750x520")
root.config(bg="#ffe6f0")


# 🧍‍♀️ Customer data
customer_positions = [(150, 250), (350, 250), (550, 250)]
faces = ["😊", "😡", "😢", "😐"]   # happy, angry, sad, confused
orders = ["Cosmic Latte", "Star Cupcake", "Moon Milkshake", "Galaxy Cookie"]

# canvas
canvas = tk.Canvas(root, width=750, height=400, bg="#ffe6f0", highlightthickness=0)
canvas.pack()

customer_objects = []
current_emotions = []


# 👽 Create customers
def create_customers():
    for i in range(3):
        x, y = customer_positions[i]
        face = canvas.create_text(x, y, text="😐", font=("Arial", 48))
        customer_objects.append(face)
        current_emotions.append("😐")
        canvas.create_text(x, y+60, text=f"Customer {i+1}", font=("Comic Sans MS", 12, "bold"))

create_customers()


# ❤️ Score
score = 0
score_label = tk.Label(root, text=f"Score: {score}", font=("Comic Sans MS", 16, "bold"), bg="#ffe6f0")
score_label.pack(pady=10)


# ✨ Change customer face
def set_emotion(customer_id, emotion):
    canvas.itemconfig(customer_objects[customer_id], text=emotion)
    current_emotions[customer_id] = emotion


# 🎮 Serve Logic
def serve_customer():
    global score
    
    customer_id = random.randint(0, 2)
    order = random.choice(orders)
    
    # Customer appears confused waiting
    set_emotion(customer_id, "😐")
    
    ask = messagebox.askyesno(
        f"Customer {customer_id+1}",
        f"This customer wants: {order}\nDid you serve it to them?"
    )

    if ask:
        # ✔ Correct service
        set_emotion(customer_id, "😊")
        score += 10
        
        # floating hearts!
        x, y = customer_positions[customer_id]
        heart = canvas.create_text(x, y - 80, text="💖", font=("Arial", 30))
        root.after(1000, lambda: canvas.delete(heart))
    
    else:
        # ❌ Wrong / No service
        bad_reaction = random.choice(["😡", "😢"])  # angry OR sad
        set_emotion(customer_id, bad_reaction)
        score -= 5
    
    score_label.config(text=f"Score: {score}")


# Buttons
btn_frame = tk.Frame(root, bg="#ffe6f0")
btn_frame.pack()

serve_btn = tk.Button(
    btn_frame, text="Serve Customer", command=serve_customer,
    bg="#ff69b4", fg="white", font=("Comic Sans MS", 14, "bold"), width=16
)
serve_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(
    btn_frame, text="Exit Cafe", command=root.destroy,
    bg="#ba55d3", fg="white", font=("Comic Sans MS", 14, "bold"), width=16
)
exit_btn.grid(row=0, column=1, padx=10)

root.mainloop()
