import json

class FMVP:
    def __init__(self, force, mass, velocity, position, timestamp):
        assert isinstance(force, list)
        assert len(force) == 3
        assert isinstance(velocity, list)
        assert len(velocity) == 3
        assert isinstance(position, list)
        assert len(position) == 3

        assert isinstance(mass, list) == False
        assert isinstance(timestamp, list) == False

        self.force = force
        self.mass = mass
        self.velocity = velocity
        self.position = position
        self.timestamp = timestamp

    def as_json(self):
        return json.dumps(self.__dict__)