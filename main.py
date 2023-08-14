import tkinter as tk


def calculate_bmi():
 try:
  # Girdileri al
  height_cm = float(my_text.get("1.0", "end-1c")) / 100
  weight_kg = float(my_text1.get("1.0", "end-1c"))

  # BMI hesapla
  bmi = weight_kg / (height_cm ** 2)

  # Sonucu ekrana yaz
  result_text.config(state="normal")
  result_text.delete("1.0", "end")
  result_text.insert("1.0", f"Vücut Kitle Endeksiniz: {bmi:.2f}\n")

  # Sonuca göre kategoriyi belirle
  if bmi < 18.5:
   category = "Zayıfsın"
  elif 18.5 <= bmi < 25:
   category = "Normal kilo"
  elif 25 <= bmi < 30:
   category = "Şişmansın"
  else:
   category = "Obezsin"

  result_text.insert("end", f"Kategori: {category}")
 except ValueError:
  result_text.config(state="normal")
  result_text.delete("1.0", "end")
  result_text.insert("1.0", "Hatalı giriş! Lütfen sayısal değerler girin.")
 finally:
  result_text.config(state="disabled")


window = tk.Tk()
window.title("BMI Hesaplama")
window.config(bg="white")
window.geometry("600x500")

label = tk.Label(text="Lütfen Boyunuzu Giriniz (cm):", font=('Arial', 10, "bold"))
label.place(x=100, y=100)

label1 = tk.Label(text="Lütfen Kilonuzu Giriniz (kg):", font=('Arial', 10, "bold"))
label1.place(x=100, y=150)

my_text = tk.Text(height=1, width=10)
my_text.place(x=300, y=100)

my_text1 = tk.Text(height=1, width=10)
my_text1.place(x=300, y=150)

my_button = tk.Button(text="Hesapla", command=calculate_bmi)
my_button.place(x=200, y=200)

result_text = tk.Text(height=2, width=30, state="disabled")
result_text.place(x=200, y=250)

window.mainloop()