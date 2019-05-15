class SpaceAge(object):
    EARTH_YEAR = 31557600
    orbits = {'mercury' : 0.2408467, 'venus' : 0.61519726, 'earth' : 1,
              'mars' : 1.8808158, 'jupiter' : 11.862615, 'saturn' : 29.447498,
              'uranus' : 84.0169846, 'neptune' : 164.79132 }
              
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_age = self.seconds / self.EARTH_YEAR
        for planet in self.orbits:
            setattr(self, 'on_' + planet, self.calc(planet))

    def calc(self, planet):
        return lambda: round(self.earth_age / self.orbits[planet], 2)
