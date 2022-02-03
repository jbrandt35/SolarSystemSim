import numpy as np

#Class for Objects in N-body Simulator
class Body:
    def __init__(self,name,mass,iposition,ivelocity):
        self.name = name
        self.mass = mass
        self.position = iposition
        self.velocity = ivelocity
        self.position_history = np.array([iposition])
        self.velocity_history = np.array([ivelocity])
        self.kinetic_energy = (1/2) * self.mass * np.linalg.norm(ivelocity)**2

    def __repr__(self):
        return str({"name":self.name, "mass":self.mass, "position":self.position, "velocity":self.velocity})

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    def get_mass(self):
        return self.mass

    def update_position(self,new_position):
        self.position = new_position
        np.append(self.position_history, new_position)

    def update_velocity(self,new_velocity):
        self.velocity = new_velocity
        np.append(self.velocity_history, new_velocity)
        self.kinetic_energy = (1/2) * self.mass * np.linalg.norm(new_velocity)**2
    