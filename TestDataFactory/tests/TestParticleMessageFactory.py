import os
import sys
import unittest

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from ParticleMessageFactory import ParticleMessageFactory
from FMVP import FMVP


class TestParticleMessageFactory(unittest.TestCase):
    def test_get_single_fmvp_message(self):
        f = ParticleMessageFactory()
        current_particles = f.get_particles()
        self.assertEqual(len(current_particles), 0)

        p = f.create_new_random_particle()
        self.assertIsInstance(p, FMVP)

        # print(p.as_json())

        current_particles = f.get_particles()
        self.assertEqual(len(current_particles), 1)

    def test_increment_particle_positions(self):
        f = ParticleMessageFactory()
        f.create_new_random_particle()
        f.increment_particle_positions()

        particles = f.get_particles()
        self.assertEqual(2, len(particles[1]))

        f.create_new_random_particle()
        f.increment_particle_positions()

        particles = f.get_particles()
        self.assertEqual(3, len(particles[1]))
        self.assertEqual(2, len(particles[2]))
