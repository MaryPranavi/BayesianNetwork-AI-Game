# BayesianNetwork AI-Game

## Task 1

Consider the following Bayesian Network
![Screenshot 2025-02-28 122223](https://github.com/user-attachments/assets/2704f562-1ac7-4bd6-a7cf-825f8b8b9ff9)

The Variables used here are as followes
B : True if there is a Baseball Game on TV, False if not
G: True if George watches TV, False if not
C: True if George is out of Cat Food, False if not
F: True if George feeds his cat, False if not.

Let us say you are given some Training Data which represents what happens over a period of time (For example: This file contains what happens every evening over one specific year). Your Task is to learn the conditonal probabilty tables for the bayesian network from the training data. The training data will be formatted as follows:
The first number is 0 if there is no baseball game on TV (B is false), and 1 if there is a baseball game on TV (B is true).
The second number is 0 if George does not watch TV (G is false), and 1 if George watches TV (G is true).
The third number is 0 if George is not out of cat food (C is false), and 1 if George is out of cat food (C is true).
The fourth number is 0 if George does not feed the cat (F is false), and 1 if George feeds the cat (F is true).

Your program should be called bnet and the command line invocation should follow the following format:
bnet.py <training_data>
<training_data> text file with training data.

You can display the calculated probabilty values in standard output.

## Task 2

Add functionality to the code for Task 1 to also be able to calculate any value in the JPD for this domain using the conditional probabilty distributions calculated in Task 1.

Your program's command line invocation will be changed to:

bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>
<training_data> text file with training data.
Bt if B is true, Bf if B is false
Gt if G is true, Gf if G is false
Ct if C is true, Cf if C is false
Ft if F is true, Ff if F is false
Sample Invocation: bnet.py training_data.txt Bt Gf Ct Ff  Train the Bayesian Network and use it to calculate P(B=t, G=f, C=t, F=f)

You can display the calculated probabilty values in standard output.

## Task 3 

Add functionality to the code for Task 2 to also be able to calculate the probabilty for any event given evidence (if available) using inference by enumeration.

Your program's command line invocation will be changed to:

bnet.py <training_data> <query variable values> [given <evidence variable values>]
<training_data> text file with training data.
Values of Query Variable [Format is same as in Task 2]
Values of Evidence Variable (if any) [Format is same as in Task 2]

Sample Invocations:
bnet.py training_data.txt Bt Gf given Ff  Train the Bayesian Network and use it to calculate P(B=t, G=f | F=f)
bnet.py training_data.txt Bt Ff  Train the Bayesian Network and use it to calculate P(B=t, F=f)
You can display the calculated probabilty values in standard output.

