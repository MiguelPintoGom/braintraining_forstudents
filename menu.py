#############################
# projDBPY
# 24.11.2023
# Miguel Pinto Gomes
#############################

import tkinter as tk
import geo01
import info02
import info05
import database
# exercises array
a_exercise=["geo01", "info02", "info05"]
albl_image=[None, None, None] # label (with images) array
a_image=[None, None, None] # images array
a_title=[None, None, None] # array of title (ex: GEO01)

dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02, "info05": info05.open_window_info_05}

# call other windows (exercices)
def exercise(event,exer):
    dict_games[exer](window)


#call display_results
def display_result(event):
    # Récupérer les résultats
    all_results = database.get_all_results()

    # Créer une nouvelle fenêtre
    result_window = tk.Toplevel(window)
    result_window.title("Results")
    result_window.geometry("600x400")

    # Créer des étiquettes
    lbl_nickname = tk.Label(result_window, text="pseudo", font=("Arial", 12, "bold"))
    lbl_duration = tk.Label(result_window, text="duration", font=("Arial", 12, "bold"))
    lbl_dateAndHour = tk.Label(result_window, text="Date And Time", font=("Arial", 12, "bold"))
    lbl_nb_try = tk.Label(result_window, text="Number of Tries", font=("Arial", 12, "bold"))
    lbl_nb_ok = tk.Label(result_window, text="Number OK", font=("Arial", 12, "bold"))

    # Positionner les étiquettes
    lbl_nickname.grid(row=0, column=0, padx=10, pady=5)
    lbl_duration.grid(row=0, column=1, padx=10, pady=5)
    lbl_dateAndHour.grid(row=0, column=2, padx=10, pady=5)
    lbl_nb_try.grid(row=0, column=3, padx=10, pady=5)
    lbl_nb_ok.grid(row=0, column=4, padx=10, pady=5)

    # Afficher les résultats d
    for idx, result in enumerate(all_results, start=1):
        tk.Label(result_window, text=result['pseudo']).grid(row=idx, column=0, padx=10, pady=5)
        tk.Label(result_window, text=result['duration']).grid(row=idx, column=1, padx=10, pady=5)
        tk.Label(result_window, text=result['dateAndHour']).grid(row=idx, column=2, padx=10, pady=5)
        tk.Label(result_window, text=result['nb_try']).grid(row=idx, column=3, padx=10, pady=5)
        tk.Label(result_window, text=result['nb_ok']).grid(row=idx, column=4, padx=10, pady=5)


# Main window
window = tk.Tk()
window.title("Training, entrainement cérébral")
window.geometry("1100x900")

# color définition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
window.configure(bg=hex_color)
window.grid_columnconfigure((0,1,2), minsize=300, weight=1)

# Title création
lbl_title = tk.Label(window, text="TRAINING MENU", font=("Arial", 15))
lbl_title.grid(row=0, column=1,ipady=5, padx=40,pady=40)

# labels creation and positioning
for ex in range(len(a_exercise)):
    a_title[ex]=tk.Label(window, text=a_exercise[ex], font=("Arial", 15))
    a_title[ex].grid(row=1+2*(ex//3),column=ex % 3 , padx=40,pady=10) # 3 label per row

    a_image[ex] = tk.PhotoImage(file="img/" + a_exercise[ex] + ".gif") # image name
    albl_image[ex] = tk.Label(window, image=a_image[ex]) # put image on label
    albl_image[ex].grid(row=2 + 2*(ex // 3), column=ex % 3, padx=40, pady=10) # 3 label per row
    albl_image[ex].bind("<Button-1>", lambda event, ex = ex :exercise(event=None, exer=a_exercise[ex])) #link to others .py
    print(a_exercise[ex])

# Buttons, display results & quit
btn_display = tk.Button(window, text="Display results", font=("Arial", 15))
btn_display.grid(row=1+ 2*len(a_exercise)//3 , column=1)
btn_display.bind("<Button-1>",lambda e: display_result(e))

btn_finish = tk.Button(window, text="Quitter", font=("Arial", 15))
btn_finish.grid(row=2+ 2*len(a_exercise)//3 , column=1)
btn_finish.bind("<Button-1>", quit)

# main loop
window.mainloop()
