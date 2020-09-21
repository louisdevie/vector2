## vector2.py

*========== EN ==========*

Module to handle vectors in a 2D space.

**vector2.Vector :**

Represent a 2D vector. It can be interpreted as a tuple of length 2 like (x, y).
  
You can declare a vector by passing :
  
`Vector()` -> null vector

`Vector( (x, y) )` -> vector of coordinates (`x`, `y`)

`Vector( angle, length )` -> vector of length `length` pointing towards `angle` in radians

`Vector( angle=a, len=l )` -> same as `Vector(a, l)`

`Vector( coords=t )` -> same as `Vector(t)`

`Vector( x=x, y=y )` -> same as `Vector((x, y))`

Positional arguments, if they're given correctly, will override keyword arguments.

The `x` and `y` will override `coords`, wich will override `angle` and `len`.

You can add/substact two vectors together, or multiply/divide them by a scalar.

`vector.length()` -> return the distance from the origin to the extremity of the vector.

You can compare a vector to another or to a number *(the length of the vector(s) will be used)*.

`vector.xint()` -> return the integer part of the x-coordinate.

`vector.yint()` -> same, but with the y-coordinate.

`vector.as_tuple()` -> convert to a tuple.

`vector.as_int_tuple()` -> shortcut for `(vector.xint(), vector.yint())`.

`vector.is_equal_to(other)` -> with the `==` or the `!=` operators, two vectors will be compared by their length. use `is_equal_to` to test if they're *exactly* the same.

*========== FR ==========*

Module pour gérer des vecteurs sur un plan.

**vector2.Vector :**

Représente un vecteur bidimensionnel. Il peut être directement interprété comme un tuple comme (x, y).
  
Vous pouvez déclarer un vecteur en faisant :
  
`Vector()` -> vecteur nul

`Vector( (x, y) )` -> vecteur de coordonnées (`x`, `y`)

`Vector( angle, length )` -> vecteur de longueur `length` dirigé vers `angle` en radians

`Vector( angle=a, len=l )` -> égal à `Vector(a, l)`

`Vector( coords=t )` -> égal à `Vector(t)`

`Vector( x=x, y=y )` -> égal à `Vector((x, y))`

Les arguments positionnels, si ils sont passés correctement, vont écraser les arguments à mot-clés.

Les arguments `x` et `y` vont écraser `coords`, qui va écraser `angle` et `len`.

Vous pouvez ajouter/soustaire deux vecteurs ensemble, ou les multiplier/diviser par un scalaire.

`vector.length()` -> retourne la distance de l'origine du vecteur à son extrémité.

Vous pouvez comparer un vecteur à un autre ou à un nombre (la longueur de(s) vecteur(s) sera utilisée).

`vector.xint()` -> retourne la partie entière de l'abscisse du vecteur.

`vector.yint()` -> pareil, mais avec l'ordonnée.

`vector.as_tuple()` -> convertit en tuple.

`vector.as_int_tuple()` -> raccourci pour `(vector.xint(), vector.yint())`.

`vector.is_equal_to(other)` -> avec les opérateurs `==` et `!=`, deux vecteur serot comparés par leur longueur. utilisez `is_equal_to` pour tester si il sont *identiques*.
