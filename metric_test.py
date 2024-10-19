"""
Module metricTest.py

Metric example - Module which is used as a testbed for static checkers.
This is a mix of different functions and classes doing different things.
"""
import random


def fn(x, y):
    """A function which performs a sum"""
    return x + y


def find_optimal_route_to_my_office_from_home(
    start_time,
    expected_time,
    favorite_route='SBS1K',
    favorite_option='bus'
):
    """Find the optimal route based on time difference."""
    d = (expected_time - start_time).total_seconds() / 60.0

    if d <= 30:
        return 'car'

    if 30 < d < 45:
        return ('car', 'metro')

    if d > 45:
        if d < 60:
            # First volvo, then connecting bus
            return ('bus:335E', 'bus:connector')
        elif d > 80:
            # Might as well go by normal bus
            return random.choice((
                'bus:330',
                'bus:331',
                ':'.join((favorite_option, favorite_route))
            ))
        elif d > 90:
            # Relax and choose favorite route
            return ':'.join((favorite_option, favorite_route))

    return None  # Default case if no conditions are met


class C:
    """A class which does almost nothing"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f(self):
        """Empty method"""
        pass

    def g(self, x, y):
        """Compare x values and return a sum"""
        if self.x > x:
            return self.x + self.y
        elif x > self.x:
            return x + self.y
        return None  # Default case if neither condition is met


class D(C):
    """D class"""

    def __init__(self, x):
        super().__init__(x, None)  # Call parent constructor with y=None

    def f(self, x, y):
        """Compare x and y and return their sum or difference"""
        if x > y:
            return x - y
        return x + y

    def g(self, y):
        """Compare self.x and y and return their sum or difference"""
        if self.x > y:
            return self.x + y
        return y - self.x
