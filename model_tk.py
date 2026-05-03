import numpy as np
from tkinter import *
from sklearn.linear_model import LinearRegression

# 🔹 Dataset (train করার জন্য)
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1,1)
scores = np.array([35, 40, 50, 55, 65, 70, 75, 85])

# 🔹 Model train
model = LinearRegression()
model.fit(hours, scores)

# 🔹 GUI function
def predict_score():
    try:
        h = float(entry.get())
        result = model.predict([[h]])
        output_label.config(text=f"Predicted Score: {result[0]:.2f}")
    except:
        output_label.config(text="Invalid input!")

# 🔹 Window setup
root = Tk()
root.title("Student Score Predictor")# Window name
root.geometry("300x200")# Window size

# 🔹 UI Elements
Label(root, text="Enter Study Hours:").pack(pady=10)

entry = Entry(root)
entry.pack(pady=5)


Button(root, text="Predict", command=predict_score).pack(pady=10)

output_label = Label(root, text="")
output_label.pack()

# 🔹 Run app
root.mainloop()