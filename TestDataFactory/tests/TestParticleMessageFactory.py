import unittest
from ..ParticleMessageFactory import ParticleMessageFactory
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
