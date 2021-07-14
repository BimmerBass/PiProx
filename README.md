# PyProx
A python script to approximate the value of pi using a well known Monte-Carlo method.

# Method
The script works by generating a set of n random points on the unit square (A square in a 2D coordinate system with side lengths 2), then it counts how many of them fall inside the unit circle (a circle with origin (0, 0) and radius 1). It turns out that the ratio between the number of points inside the unit circle and the total number of points will tend towards π / 4 for n -> ∞, and we will therefore find an approximation of the value of pi (π).

The above means that the algorithm is entirely based on random (uniform) distributions of points.

## Motivation of the method
If we assume that the radius of the circle is unknown, we can express its area as ![equation](http://www.sciweavers.org/tex2img.php?eq=A_c%20%3D%20%5Cpi%20%5Ccdot%20r%5E2&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0). Additionally, we know that the side length of the square is twice that of the circle's radius, and we therefore know that ![equation](http://www.sciweavers.org/tex2img.php?eq=A_s%20%3D%20%282%5Ccdot%20r%29%5E2%20%3D%204%5Ccdot%20r%5E2&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0). Combining these, we get that ![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7BA_c%7D%7BA_s%7D%20%3D%20%5Cfrac%7B%5Cpi%20%5Ccdot%20r%5E2%7D%7B4%5Ccdot%20r%5E2%7D%20%3D%20%5Cfrac%7B%5Cpi%7D%7B4%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0).

Now, if we populate the square (that has the circle inside of it) with random points, it follows intuitively that the ratio of points inside the circle and total points, will tend towards the ratio of the circle's area and the square's area. This is because infinitely many points will populate the square and circle entirely and therefore they can be seen as a sort of expression for their respective areas.

The above is not a complete, mathematical proof, but rather a kind of proof-of-concept.
