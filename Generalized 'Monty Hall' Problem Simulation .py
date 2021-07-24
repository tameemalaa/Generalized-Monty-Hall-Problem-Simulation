from math import floor
from random import choice 
import matplotlib.pyplot as plt
from prettytable import PrettyTable
class door :
    def __init__(self):
        self.status=True
        self.hascar=False

def play(num_doors = 3, num_cars=1 , num_opened= 1):
    doors = [door() for i in range (num_doors)]
    i = 0
    while i < num_cars:
        change = choice(doors) 
        if not(change.hascar) :
            setattr(change , 'hascar', True)
            i += 1 
    pick = choice(doors)
    i = 0 
    while i < num_opened :
        change = choice(doors)
        if change.status and not(change.hascar) and pick is not change :
            setattr(change, 'status', False)
            i += 1
    while True :
        switch = choice(doors)
        if switch.status and switch is not pick :
            break 
    while True :
        ran = choice(doors)
        if ran.status:
            break
    return [pick.hascar ,switch.hascar, ran.hascar ]

def main() :
    print (" Please note:  Any invaild input will set to the default value!!!")
    while True :
        trials = int(input("How many times to play? (Defualt= 10000) ") or "10000")
        num_doors = int(input("Choose the total number of doors? (Defualt= 3) ") or "3")
        num_cars = int(input("Choose the number of cars? (Defualt= 1) ") or "1")
        num_opened = int(input("Choose the number of doors for monty to open? (Defualt= 1) ") or "1")
        wins_pick, wins_switch,wins_random = 0,0,0
        if num_doors > (num_opened+1) and num_cars < num_doors -num_opened and num_doors>= 3 and num_cars >=1 and num_opened>=1 and trials >=1 :
            break
        else : 
            print(""" The game conditions does not fit, please follow the following rules:
            1- Number of doors opened should be less than the total number of doors by 2 , one for the first pick and at least one for the second stage.
            2- the number of cars should be less than the number of total doors - the number of doors will be opened.
            3- the minmun number of each game condition is its default value.
            4- the minmum number of trials is 1. """)
    switch_theo = (num_cars*(num_doors-1)) / (num_doors*(num_doors - 1 - num_opened))*100
    pick_perc , switch_perc , random_perc , x = [0], [0], [0], [0]
    for i in range (1 , trials+1 ): 
        lst = play(num_doors,num_cars,num_opened)
        wins_pick += lst[0]
        wins_switch += lst[1]
        wins_random += lst[2]
        if i % (floor(trials/1000))==0 or i == trials or trials<1000 :
            x.append(i)
            pick_perc.append((wins_pick/i)*100)
            switch_perc.append((wins_switch/i)*100)
            random_perc.append((wins_random/i)*100)
        if i % 1000 == 0 or i == 1 or i == trials :
            plt.cla()                
            plt.ion
            plt.title("Monty Hall Simulation", fontsize=20)
            plt.xlabel("Trials")
            plt.ylabel("Win Percentage %")  
            plt.axis([0, trials, 0, 100])
            plt.plot(x,pick_perc,color='Red',label='Stay' )
            plt.plot(x,switch_perc,color='Blue',label='Switch')
            plt.plot(x,random_perc, color='Green',label='Random')
            plt.legend(loc='upper right', title='Strategy')
            plt.grid()
            plt.pause(0.00000000000000000000000000000000000000000000000000000000000000000000000001)
    print(f"The simulation results in {trials} trials: ")
    t1 = PrettyTable()
    t1.add_column("Strategy",["Stay ","Switch ","Random "])
    t1.add_column("Win Percentage % ",[pick_perc[-1],switch_perc[-1],random_perc[-1]])
    t2 = PrettyTable()
    t2.add_column("Theoretical Switch Win Percentage % ",[switch_theo])
    t2.add_column("Simulation Switch Win Percentage % ",[switch_perc[-1]])
    print(t1)
    print(t2)
    plt.show()

while True :
    main ()
    while True :
        i=  input("Type 1 to run another simulation or  2 to terminate: ")
        if i == "1" :
            breaker = False
            break
        elif i == "2":
                breaker= True
                break
        else :
            print(" Please, enter 1 or 2 ")
    if breaker:
        break
