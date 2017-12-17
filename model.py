# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:49:19 2017
GEOG5995M Programming for Social Science: Core Skills
@author: Eugeni Vidal
"""
import matplotlib
import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import agentclasses
import csv

#Define model parameters
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#Make the environment
environment = []

f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

agents = []

#For animating
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

def update(frame_number):
    fig.clear()   

# Make the agents.
    for i in range(num_of_agents):
        agents.append(agentclasses.Agent(environment, agents))

    random.shuffle(agents)
# Move the agents.
    for j in range(num_of_iterations):
 
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
#Plotting
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a <num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()


   


