import os 
import sys
import tkinter as tk
import customtkinter as ctk

#TO IMPORT FILES FROM PC
def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  except Exception:
    base_path = os.path.abspath(".")
  return os.path.join(base_path, relative_path)

#GAME VARIABLES
playerO = "O"
playerX = "X"
winner = True
current_player = playerO
turn = 0
game_over = False
board = [["0","0","0"],
         ["0","0","0"],
         ["0","0","0"]]

def check_winner() :
    global current_player,turn,game_over,winner

    turn += 1

    for row in range(3) :
        if board[row][0].cget("text") == board[row][1].cget("text") == board[row][2].cget("text") and board[row][0].cget("text") != "" :
            label.configure(text=f"Winner : {board[row][0].cget("text")}",
                            fg_color="#FB8500",
                            text_color="#000000")
            for column in range(3) :
                board[row][column].configure(fg_color="#FB8500",
                                             hover_color="#D97400",
                                             text_color="#000000")
            game_over = True
            winner = True
            return

    for column in range(3) :
        if board[0][column].cget("text") == board[1][column].cget("text") == board[2][column].cget("text") and board[0][column].cget("text") != "" :
            label.configure(text=f"Winner : {board[0][column].cget("text")}",
                            fg_color="#FB8500",
                            text_color="#000000")
            for row in range(3) :
                board[row][column].configure(fg_color="#FB8500",
                                             hover_color="#D97400",
                                             text_color="#000000")
            game_over = True
            winner = True
            return

    for i in range(3) :
        if board[0][0].cget("text") == board[1][1].cget("text") == board[2][2].cget("text") and board[i][i].cget("text") != "" :
            label.configure(text=f"Winner : {board[0][0].cget("text")}",
                            fg_color="#FB8500",
                            text_color="#000000")
            board[i][i].configure(fg_color="#FB8500",
                                  hover_color="#D97400",
                                  text_color="#000000")
            winner = True
            game_over = True

    if board[0][2].cget("text") == board[1][1].cget("text") == board[2][0].cget("text") and board[0][2].cget("text") != "" :
        label.configure(text=f"Winner : {board[0][2].cget("text")}",
                        fg_color="#FB8500",
                        text_color="#000000")
        board[0][2].configure(fg_color="#FB8500",
                              hover_color="#D97400",
                              text_color="#000000")
        board[1][1].configure(fg_color="#FB8500",
                              hover_color="#D97400",
                              text_color="#000000")
        board[2][0].configure(fg_color="#FB8500",
                              hover_color="#D97400",
                              text_color="#000000")
        winner = True
        game_over = True
        return

    if turn == 9 and not winner:
        label.configure(text="Tie!",
                        fg_color="#FB8500",
                        text_color="#000000")
        game_over = True

def set_button(row,column) :
    global current_player,game_over
    if board[row][column].cget("text") != "" or game_over :
        return
    
    board[row][column].configure(text=current_player)

    if current_player == playerO :
        current_player = playerX
    else :
        current_player = playerO

    label.configure(text=f"Turn : {current_player}")

    check_winner()

def new_game() :
    global game_over,turn,winner
    turn = 0
    game_over = False
    winner = False
    label.configure(text=f"Turn : {current_player}",
                    fg_color="#003554",
                    text_color="#ccdffc")
    for row in range(3) :
        for column in range(3) :
            board[row][column].configure(text="",
                                         fg_color="#3ABDFF",
                                         hover_color="#0392D9",
                                         text_color="#000000",)

#SETTING WINDOW
window = ctk.CTk(fg_color="#051923")
window.title("TIC TAC TOE")
window.geometry("500x500")
window.iconbitmap(resource_path("tic-tac-toe.ico"))
icon = tk.PhotoImage(file=resource_path("tic-tac-toe.png"))
window.iconphoto(False, icon)
window.resizable(False,False)

#CENTERING WINDOW
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#FRAME
frame = ctk.CTkFrame(window,fg_color="#051923")
frame.pack()

#LABEL
label = ctk.CTkLabel(frame,fg_color="#003554",
                     text=f"Turn : {current_player}",
                     text_color="#ccdffc",
                     font=("Consolas", 36, "bold"),
                     width=50,
                     height=50,
                     corner_radius=10)
label.grid(row = 0, column=0, columnspan=3, padx=5, pady=10)

#GAME BUTTONS
for row in range(3) :
    for column in range(3) :
        board[row][column] = ctk.CTkButton(frame,
                                width=170,
                                height=150,
                                command = lambda row=row, column=column : set_button(row,column), 
                                text="",
                                fg_color="#3ABDFF",
                                hover_color="#0392D9",
                                text_color="#000000",
                                font=("Segoe UI", 40, "bold"),
                                corner_radius=20)
        
        board[row][column].grid(row =row+1, column=column, padx=5, pady=5, sticky="nsew")

#RESET BUTTON
restart = ctk.CTkButton(frame,
                        text="Restart",
                        width=50,
                        height=50,
                        command = new_game,
                        fg_color="#FB8500",
                        hover_color="#D97400",
                        text_color="#000000",
                        font=("Segoe UI", 36, "bold"),
                        corner_radius=10)
restart.grid(row = 4, column=0, columnspan=3, padx=5, pady=10)

window.mainloop()