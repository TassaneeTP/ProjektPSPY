

import random 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os, sys


'''
clear = lambda: os.system('cls')
clear()

from words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
'''
'''
root = Tk()
root.geometry('905x700')
root.title('Hangman Game')
root.config(bg = '#FFEFDB')
'''
#print(logo)
'''
#Create blanks
display = []
for _ in range(word_length):
    display += "_"
'''
#Label(root, text= "Yes for easy, No for difficult", font= ('Helvetica 17 bold')).pack(pady=30)
answer = messagebox.askyesno('Easy(yes)/Difficult(no)','Which level do you want?')

if answer == True:
    databas = "words2.txt"
else:
    databas = "words.txt"

score = 0
end_of_game = True
while end_of_game:
        
        root = Tk()
        root.geometry('905x700')
        root.title('Hangman Game')
        root.config(bg = '#FFEFDB')
        count = 0
        win_count = 0

    #guess = input("Guess a letter: ").lower()

        
        file = open(databas,'r')
        l = file.readlines()
        index = random.randint(0,len(l))
        selected_word = l[index].strip('\n')
   

        x = 250
        for i in range(0,len(selected_word)):
            x += 60
            exec('d{}=Label(root,text="_",bg="#FFEFDB",font=("Helvetica",30))'.format(i))
            exec('d{}.place(x={},y={})'.format(i,x,450))
        
 
        al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for let in al:
            exec('{}=PhotoImage(file="{}.png")'.format(let,let))
        
    
        h123 = ['h1','h2','h3','h4','h5','h6','h7']
        for hangman in h123:
            exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))
   
    
        button = [['b1','a',0,595],['b2','b',70,595],['b3','c',140,595],['b4','d',210,595],['b5','e',280,595],['b6','f',350,595],['b7','g',420,595],['b8','h',490,595],['b9','i',560,595],['b10','j',630,595],['b11','k',700,595],['b12','l',770,595],['b13','m',840,595],['b14','n',0,645],['b15','o',70,645],['b16','p',140,645],['b17','q',210,645],['b18','r',280,645],['b19','s',350,645],['b20','t',420,645],['b21','u',490,645],['b22','v',560,645],['b23','w',630,645],['b24','x',700,645],['b25','y',770,645],['b26','z',840,645]]

        for q1 in button:
            exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#FFEFDB",activebackground="#FFEFDB",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
            exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
        
    
        han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
        for p1 in han:
            exec('{}=Label(root,bg="#FFEFDB",image={})'.format(p1[0],p1[1]))

    
        c1.place(x = 300,y =- 50)
    
    
        def close():
            global end_of_game
            answer = messagebox.askyesno('ALERT','You want to exit the game?')
            if answer == True:
                end_of_game = False
                root.destroy()
            
        e1 = PhotoImage(file = 'exit.png')
        ex = Button(root,bd = 0,command = close,bg="#FFEFDB",activebackground = "#FFEFDB",font = 10,image = e1)
        ex.place(x=770,y=10)
        s2 = 'SCORE:'+str(score)
        s1 = Label(root,text = s2,bg = "#FFEFDB",font = ("Helvetica",20))
        s1.place(x = 10,y = 10)

        def check(guess,button):
            global count,win_count,end_of_game,score 
            exec('{}.destroy()'.format(button))
            if guess in selected_word:
                for i in range(0,len(selected_word)):
                    if selected_word[i] == guess:
                        win_count += 1
                        exec('d{}.config(text="{}")'.format(i,guess.lower()))
                if win_count == len(selected_word):
                    score += 1
                    answer = messagebox.askyesno('Game over', 'You won!\nWant to play again?')
                    if answer == True:
                        end_of_game = True
                        root.destroy()
                    else:
                        end_of_game = False
                        root.destroy()
            else:
                count += 1
                exec('c{}.destroy()'.format(count))
                exec('c{}.place(x={},y={})'.format(count+1,300,-50))
                if count == 6:
                    answer = messagebox.askyesno('Game over', 'You lost!\nWant to play again?')
                    if answer == True:
                        end_of_game = True
                        score = 0
                        root.destroy()
                    else:
                        end_of_game = False
                        root.destroy()
        root.mainloop()
'''

root.mainloop()
'''
'''
Label(root, text= "Click the below button to Start the game", font= ('Helvetica 17 bold')).pack(pady=30)
B = ttk.Button(root, text = "Start", command = While).pack(pady=10)
root.mainloop()
'''
     #print(f"You've already guessed {guess}")
'''
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
'''