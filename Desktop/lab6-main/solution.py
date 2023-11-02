import math
from render import InitRender, Render

G = 6.67408e-11

# Define the bodies
central_body = (1e12, (400.0, 400.0), (0.0, 0.0))  # Central body with large mass, positioned at the origin, stationary
planet1 = (1e4, (360.0, 400.1), (0.0001, 1.5))   # Planet 1 starting at (1000, 0) with a velocity vector giving it a circular orbit
planet2 = (1e3, (400.1, 280.0), (-0.5, 0.0001))  # Planet 2 starting at (0, -500) with a velocity vector giving it a circular orbit

# Define the system
system = [central_body, planet1, planet2]

def calculate_distance(body1, body2):
    """Returns the distance between two bodies"""
    pass

def calculate_force(body1, body2):
    """Returns the force exerted on body1 by body2, in 2 dimensions as a tuple"""
    pass

def calculate_net_force_on(body, system):
    """Returns the net force exerted on a body by all other bodies in the system, in 2 dimensions as a tuple"""
    pass

def calculate_acceleration(body, system):
    """Returns the acceleration of a body due to the net force exerted on it by all other bodies in the system, in 2 dimensions as a tuple"""
    pass

def update_velocity(system, dt):
    """Updates the velocities of all bodies in the system, given a time step dt"""
    pass
   

def update(system, dt):
    """Update the positions of all bodies in the system, given a time step dt"""
    pass

def simulate(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps"""
    pass

def simulate_with_visualization(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps, and visualizes the motion"""
    pass

if __name__ == '__main__':
    pass

import numpy as np
from render import *

G = 6.67430e-11

def calculate_distance(body1, body2):
    x1,y1 = body1[1]
    x2,y2 = body2[1]
    distance = np.sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance

def calculate_force(body1,body2):
    distance = calculate_distance(body1, body2)
    m1 = body1[0]
    m2 = body2[0]
    global G
    force = G*m1*m2/(distance**2)
    x1,y1 = body1[1]
    x2,y2 = body2[1]
    x = x2 - x1
    y = y2 - y1
    x = x/np.sqrt(x**2 + y**2)
    y = y/np.sqrt(x**2 + y**2)
    return (force*x, force*y)

def calculate_net_force_on(body, system):
    force = np.array([0.,0.])
    for b in system:
        if b == body:
            continue
        b12_force = calculate_force(body,b)
        
        force[0]=  force[0] + b12_force[0]
        force[1]=  force[1] + b12_force[1]
       
    return force

def calculate_acceleration(body, system):
    force = calculate_net_force_on(body, system)
    m = body[0]
    a = force/m
    return a
    
def update_velocity(system, dt):
    new_system = []
    for i in range(len(system)):
        body = system[i]
        a = calculate_acceleration(body, system)
        new_body = (body[0], body[1], (system[i][2][0] + a[0]*dt,system[i][2][1] + a[1]*dt))
       
        new_system.append(new_body)
    return new_system
    
def update(system, dt):
    new_system = []
    system = update_velocity(system, dt)
    for i in range(len(system)):
        new_body = (system[i][0], (system[i][1][0] + system[i][2][0]*dt,                                   system[i][1][1] + system[i][2][1]*dt),system[i][2])

        new_system.append(new_body)
    return new_system
    
def simulate(system, dt, num_steps):
    for i in range(num_steps):
        system = update(system, dt)
    return system

def simulate_with_visualization(system, dt, num_steps):
    InitRender()
   
    Render(system)
    for i in range(num_steps):
        system = update(system, dt)
        Render(system)
    
if __name__ == "main":
    system = [(1e7, (1e2,2e2), (0,1e3)), (1e18, (2e2,4e2), (0,-1e3)),(1e7, (3e2,5e2), (-1e3,0))]
    num_steps = 100
    dt = 0.01
    simulate_with_visualization(system, dt, num_steps)








