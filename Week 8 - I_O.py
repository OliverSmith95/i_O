# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:49:16 2018

@author: gy18os
"""

import random #inputting the random function
import operator
import csv
import matplotlib.pyplot #inputting code to allow for matplot for code
environment = [] #creation of environment empty list
import Agent_Framework_2 #inform the agent framework - seperate bracket of agents, external to other aspects of code. 


 
f = open ("in.txt")
reader = csv.reader(f)
for row in reader:
    rowlist = [] #creation of lists derived from csv file
    environment.append(rowlist)
    for value in row:
            #print (value)
            #indented below to combat float error. ensure indention is correct
            rowlist.append(int(value))
f.close()
#inporting mapping environment 
matplotlib.pyplot.imshow(environment) # introduced environments to plot
matplotlib.pyplot.show() 
  

        

'''
envrionment = [] #create a new list in which to rows from rowlist

   f = open('in.ixt") 
reader = csv.reader(f)
for row in reader:				# A list of rows
       rowlist = []			# A list of value
       environment.append(rowlist)
       for value in row:
       rowlist.append(environment)    
       print(value) 				# Floats
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
print ("loaded environment")
print ("plot environment")
'''

#agent framework 2 is the file i want to input, .agent is the data. 
a = Agent_Framework_2.Agent(environment) # feeding the environment our agents 
print (a._y, a._x) #print co-ordinates for file
a.move() #mvoing set of co-ordinates 
print(a._y, a._x) 

def distance_between(agents_row_a, agents_row_b):
     return (((agents_row_a._x - agents_row_b._x)**2) + 
     ((agents_row_a._y - agents_row_b._y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []
distances = []

 # Make the agents.
for i in range(num_of_agents):
    agents.append(Agent_Framework_2.Agent(environment)) # introduced environments

 # Move the agents.
for j in range(num_of_iterations):
     for i in range(num_of_agents):
         agents[i].move()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
     #changed agent labels to match agent frame work.
     matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
 
matplotlib.pyplot.show()

for agents_row_a in agents:
     for agents_row_b in agents:
         distance = distance_between(agents_row_a, agents_row_b) 
         
#eating the remaining data - If we then call eat for each agent after we move it in model.py
for j in range(num_of_iterations):
     for i in range(num_of_agents):
         agents[i].move()
         agents[i].eat()
         
         
#plot both datasets together - requirement of eating remaining data first then introduce code below. 
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

         