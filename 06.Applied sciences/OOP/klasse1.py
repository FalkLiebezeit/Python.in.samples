# Definition of the Koerper class with additional methods.
# Optimized and commented in English for clarity.

class Koerper:
    """
    A celestial body.

    Args:
        name (str): Name of the celestial body.
        mass (float): Mass of the celestial body in kilograms.
    """

    def __init__(self, name, mass):
        self.name = name  # Name of the celestial body
        self.mass = mass  # Mass in kilograms

    def earth_masses(self):
        """
        Calculate the mass in multiples of Earth's mass.

        Returns:
            float: Mass as a multiple of Earth's mass.
        """
        EARTH_MASS = 5.9722e24  # Earth's mass in kg
        return self.mass / EARTH_MASS

    def __str__(self):
        """
        Return a string representation of the body.

        Returns:
            str: Description of the celestial body.
        """
        return f'Body {self.name}: m = {self.mass:.3e} kg'

if __name__ == '__main__':
    # Example usage: create a planet and print its properties
    planet = Koerper('Jupiter', 1.89813e27)
    print(planet.name)
    print(planet.mass)
    print(planet)
    print(f'The planet {planet.name} has a mass of '
          f'{planet.earth_masses():.1f} Earth masses')