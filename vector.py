import operator
import math


class Vector(object):
    """
    Vector operations based on Udacity Linear Algebra refresher course.
    """
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def add(self, v):
        return Vector(map(operator.add, self.coordinates, v.coordinates))


    def subtract(self, v):
        return Vector(map(operator.sub, self.coordinates, v.coordinates))

    def scale(self, scalar):
        return Vector([x*scalar for x in self.coordinates])


    def magnitude(self):
        return math.sqrt(sum([x*x for x in self.coordinates]))

    def normalize(self):
        norm = 1.0/self.magnitude()
        return Vector([x*norm for x in self.coordinates])


if __name__ == "__main__":
    my_vector = Vector((1,2,3))
    print my_vector
    my_vector2 = Vector((1,2,3))
    my_vector3 = Vector((-1,2,3))
    print my_vector == my_vector2
    print my_vector == my_vector3
    print 'my_vector + my_vector2' ,my_vector.add(my_vector2)
    print 'my_vector - my_vector3' ,my_vector.subtract(my_vector3)
    print 'my_vector2 scaled by 3' ,my_vector2.scale(3)

    print my_vector.magnitude()
    print my_vector.normalize(), my_vector.normalize().magnitude()
