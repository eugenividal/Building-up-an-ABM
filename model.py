# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:49:19 2017
GEOG5995M Programming for Social Science: Core Skills
@author: Eugeni
"""
import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import agentclasses
import csv

# Parameters of the model.
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

# Set up environment list (before the agents list).
environment = []
# Read enviroment data.
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

# Set up agents list.
agents = []

# Animating.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentclasses.Agent(environment, agents))

carry_on = True

# Function to set up animation.
def update(frame_number): 
    
    fig.clear()   
    global carry_on

# Move the agents (and other behaviours).  
    for j in range (num_of_iterations):
        random.shuffle(agents) # Shuffle the list of agests each iteration before they do their stuff. 
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)

# Plot the agents within the environment.          
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        matplotlib.pyplot.imshow(environment)

# Generator function stops supplying stuff when the condition is met (Animation).     
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a <num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

# Animation plot.
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()
  
"""
THE END 
"""

