__all__ = ['Vector']

__doc__ = """Module to handle vectors in a 2D space."""

import math

class Vector (object):
	"""Represent a 2D vector.
You can declare a vector by passing :
    Vector() -> null vector
    Vector( (x, y) ) -> vector of coordinates (x, y)
    Vector( angle, length ) -> vector of length (length) pointing towards (angle) in radians
    Vector( angle=a, len=l ) -> same as Vector(a, l)
    Vector( coords=t ) -> same as Vector(t)
    Vector( x=x, y=y ) -> same as Vector((x, y))

Positional arguments, if they're given correctly, will override keyword arguments.
The x and y will override coords, wich will override angle and len."""

	def __init__(self, *args, **kwargs):

		if len(args) == 1:
			if type(args[0]) is tuple:
				self.x, self.y = args[0]
				return

		elif len(args) == 2:
			if type(args[0]) in (int, float) and type(args[1]) in (int, float):
				self.x = math.cos(args[0]) * args[1]
				self.y = math.sin(args[0]) * args[1]
				return

		else:
			self.x = math.cos(kwargs.get('angle', 0)) * kwargs.get('len', 0)
			self.y = math.sin(kwargs.get('angle', 0)) * kwargs.get('len', 0)
			self.x, self.y = kwargs.get('coords', (self.x, self.y))
			self.x = kwargs.get('x', self.x)
			self.y = kwargs.get('y', self.y)

	def __repr__(self):
		return 'Vector2D (%r, %r)'%(self.x, self.y)


	def __pos__(self):
		return Vector(x=self.x, y=self.y)

	def __neg__(self):
		return Vector(x=-self.x, y=-self.y)

	def __nonzero__(self):
		if self.x and self.y:
			return True
		return False


	def __iadd__(self, vector):
		if type(vector) is Vector:
			self.x += vector.x
			self.y += vector.y

		else:
			raise TypeError('you can only add a vector to another vector')

	def __isub__(self, vector):
		if type(vector) is Vector:
			self.x -= vector.x
			self.y -= vector.y

		else:
			raise TypeError('you can only substract a vector to another vector')

	def __imul__(self, scalar):
		if type(scalar) in (int, float):
			self.x *= scalar
			self.y *= scalar

		else:
			raise TypeError('you can only multiply a vector by a scalar (int or float)')

	def __idiv__(self, scalar):
		if type(scalar) in (int, float):
			self.x /= scalar
			self.y /= scalar

		else:
			raise TypeError('you can only divide a vector by a scalar (int or float)')


	def __add__(self, vector):
		if type(vector) is Vector:
			return Vector(x=self.x+vector.x, y=self.y+vector.y)

		else:
			raise TypeError('you can only add a vector to another vector')

	def __sub__(self, vector):
		if type(vector) is Vector:
			return Vector(x=self.x-vector.x, y=self.y-vector.y)

		else:
			raise TypeError('you can only substract a vector to another vector')

	def __mul__(self, scalar):
		if type(scalar) in (int, tuple):
			return Vector(x=self.x*vector.x, y=self.y-vector.y)

		else:
			raise TypeError('you can only multiply a vector by a scalar (int or float)')

	def __div__(self, scalar):
		if type(scalar) in (int, tuple):
			return Vector(x=self.x/vector.x, y=self.y/vector.y)

		else:
			raise TypeError('you can only divide a vector by a scalar (int or float)')


	def __lt__(self, other):
		if type(other) is Vector:
			return self.length() < other.length()

		elif type(other) in (int, float):
			return self.length < other

		else:
			raise TypeError('you can only compare a vector to another vector or a number')

	def __gt__(self, other):
		if type(other) is Vector:
			return self.length() > other.length()

		elif type(other) in (int, float):
			return self.length > other

		else:
			raise TypeError('you can only compare a vector to another vector or a number')

	def __le__(self, other):
		if type(other) is Vector:
			return self.length() <= other.length()

		elif type(other) in (int, float):
			return self.length <= other

		else:
			raise TypeError('you can only compare a vector to another vector or a number')

	def __ge__(self, other):
		if type(other) is Vector:
			return self.length() >= other.length()

		elif type(other) in (int, float):
			return self.length >= other

		else:
			raise TypeError('you can only compare a vector to another vector or a number')

	def __eq__(self, other):
		if type(other) is Vector:
			return self.length() == other.length()

		elif type(other) in (int, float):
			return self.length == other

		else:
			raise TypeError('you can only compare a vector to another vector or a number')

	def __ne__(self, other):
		if type(other) is Vector:
			return self.length() != other.length()

		elif type(other) in (int, float):
			return self.length != other

		else:
			raise TypeError('you can only compare a vector to another vector or a number')


	def length(self):
		"""return the length of the vector"""
		return math.sqrt(self.x**2 + self.y**2)

	def as_tuple(self):
		"""equivalent to (vector.x, vector.y)"""
		return (self.x, self.y)

	def as_int_tuple(self):
		"""equivalent to (vector.xint(), vector.yint())"""
		return (int(self.x), int(self.y))

	def xint(self):
		"""return the x coordinate as an integer"""
		return int(self.x)

	def yint(self):
		"""return the y coordinate as an integer"""
		return int(self.y)
	
	def is_equal_to(self, vector):
		if type(vector) is Vector:
			return self.x==vector.x and self.y==vector.y

		else:
			raise TypeError('you can only test if a vector is the same as another vector')
