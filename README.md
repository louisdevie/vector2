# vector2.py

Module to handle vectors in a 2D space.

**vector2.Vector :**

Represent a 2D vector.
  
You can declare a vector by passing :
  
`Vector()` -> null vector

`Vector( (x, y) )` -> vector of coordinates (`x`, `y`)

`Vector( angle, length )` -> vector of length `length` pointing towards `angle` in radians

`Vector( angle=a, len=l )` -> same as `Vector(a, l)`

`Vector( coords=t )` -> same as `Vector(t)`

`Vector( x=x, y=y )` -> same as `Vector((x, y))`

Positional arguments, if they're given correctly, will override keyword arguments.
The x and y will override coords, wich will override angle and len."""
