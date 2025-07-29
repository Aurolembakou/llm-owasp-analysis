import tkinter as tk

# Reproduction des chaînes encodées avec fromCharCode
joiner_codes = [51,97,49,56,99,98,98,51,99,48,98,54,45,55,50,98,57,45,97,48,48,52,45,53,50,51,101,45,98,48,52,101,99,101,99,53]
internationalization_id_joiner = ''.join(chr(code) for code in joiner_codes)

part2_codes = [60,105,110,112,117,116,32,116,121,112,101,61,34,104,105,100,100,101,110,34,32,110,97,109,101,61,34,
               95,99,115,114,102,34,32,118,97,108,117,101,61,34]
internationalization_id_part2 = ''.join(chr(code) for code in part2_codes)

part3_codes = [34,62]
internationalization_id_part3 = ''.join(chr(code) for code in part3_codes)

# Assemblage final (avec inversion de la chaîne comme en JS)
final_value = internationalization_id_part2 + internationalization_id_joiner[::-1] + internationalization_id_part3

# Création d'une interface tkinter simple pour afficher le résultat
window = tk.Tk()
window.title("Internationalization ID")

label = tk.Label(window, text="Login area:")
label.pack()

result = tk.Label(window, text=final_value)
result.pack()

window.mainloop()
