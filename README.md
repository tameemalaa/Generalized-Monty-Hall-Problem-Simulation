# Generalized Monty Hall Problem Simulation
 Generalized 'Monty Hall' problem simulation with graphing  and theortical value calculator for the switch strategy win percent

# Theoretical Monty Hall Problem 
The General formula for the problability of getting a car after switching is given by the formula : 

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-C(D-1)}{D(D-1-O)}" title="\Largex=\frac{-C(D-1)}{D(D-1-O)}" /> \
•	Number of Doors(D) \
•	Number of Cars(C) \
•	Number of Doors to be opened by the host(O) \

Additional Reading: [Higher Variations of the Monty Hall Problem ](https://www.researchgate.net/publication/230656854_Higher_Variations_of_the_Monty_Hall_Problem_30_40_and_Empirical_Definition_of_the_Phenomenon_of_Mathematics_in_Boole%27s_Footsteps_as_Something_the_Brain_Does)

# Installing requirements.txt:
```bash
pip install -r requirements.txt
```

# Program Description: 
The user defines the parameters for the problem:

•	Number of Doors(D) \
•	Number of Cars(C) \
•	Number of Doors to be opened by the host(O) \
•	Number of Trials (N)

The classic parameters for the problem are (3 doors, one car and one door to be revealed).  \
The simulation then runs for (n) number of times, and each time picks a door then the host reveals a number of doors that don’t contain the prize. Then, the simulation tries out 3 strategies and records the results \
 •	 Stay at the chosen door \
 •	 Switch to an unopened door \
 •	 Random: make a random choice between all unopened doors 
 
The win percentage for each strategy vs number of trials is plotted in real time

# Sample Run: 
Times to play ? 10000 \
Choose total number of doors : 3 \
Total number of cars : 1 \
Number of Doors to be opened : 1 

## Output

![image](https://user-images.githubusercontent.com/66860955/126853136-16bbeb8a-5858-4e98-9d7d-9756c46dba0d.png)

### The simulation results in 10000 trials: 

| Strategy      | Win percentage|       
| ------------- | ------------- |                
| Stay          | 34.04         |
| Switch        | 65.96         |
| Random        | 49.78         |

| Theoritcal Switch win percentage | Simluation Switch win percentage |
|--------------------------------- | -------------------------------- |
|          66.66666666666666       |                65.96             |

# License
[MIT](https://choosealicense.com/licenses/mit/)
