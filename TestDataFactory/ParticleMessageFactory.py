import sys
from random import randint
from FMVP import FMVP


class ParticleMessageFactory:
    def __init__(self):
        self.active_particles = {}

    def get_particles(self):
        return self.active_particles

    def create_new_random_particle(self):
        MIN = 0
        MAX = 9
        force = [randint(MIN, MAX), randint(MIN, MAX), randint(MIN, MAX)]
        mass = randint(MIN, MAX) + 1  # try to keep this positive
        velocity = [randint(MIN, MAX), randint(MIN, MAX), randint(MIN, MAX)]
        position = [randint(MIN, MAX), randint(MIN, MAX), randint(MIN, MAX)]
        timestamp = 0
        p = FMVP(force=force, mass=mass, velocity=velocity, position=position, timestamp=timestamp)

        max_current_particle = 0
        if len(self.active_particles.keys()) > 0:
            max_current_particle = max(self.active_particles.keys())

        next_particle_index = max_current_particle + 1
        self.active_particles[next_particle_index] = [p]

        return p

    def increment_particle_positions(self):
        for i, particle_list in self.active_particles.items():
            p = particle_list[-1]
            new_position = [p.position[0] + p.velocity[0],
                            p.position[1] + p.velocity[1],
                            p.position[2] + p.velocity[2]]
            new_velocity = [p.velocity[0] + randint(-3, 3),
                            p.velocity[1] + randint(-3, 3),
                            p.velocity[2] + randint(-1, 1)]
            p_new = FMVP(force=p.force, mass=p.mass,
                         velocity=new_velocity,
                         position=new_position,
                         timestamp=p.timestamp+1)
            particle_list.append(p_new)

