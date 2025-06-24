June 2 2025 class - 3

1. Equation : 
   mathematical equation that shows two things are equal.
   . x + 2 = 5

2. Linear equation : Straight, no change . 
   (Constant rate of change)
   The graph is a straight line for this.
   . ax + b = 0

3. Exponential equation : 
   Continous changes. (mathematical equation has a variable in the exponent and grows).
   . y = a^x

4. Multiple Linear equation : 
   set of linear equations more than one variable.(that mean we will have 2 or more equations)
    . In linear equation we just have to find one variable x.
    . but here we should find based on the problem like x, y,z this is     called multiple linear equation. 

5. Optimization : 
    Finding the best solution under the given conditions. 
    .if we have so many 1000 records and 1 million features,  
    .we just optimise that means we minimise the features to get the records.

# MATRICES:-
 Matrix : 
   Set of numbers arranged in rows and columns.
   . matrix dimensions are rows and columns.
   . Matrix is an rectangular array.
   . row is horizontal. column is vertical.

TYPES OF MATRICES:-
1. Rectangular Matrix :
   With m rows and n columns( that means different rows and different columns).
   m*n matrix.

2. Square Matrix :
   with same number of rows and columns.
   n*n matrix.

3. Diagonal Matrix :
   having values on the diagonal side and 0 on the rest.

4. Row matrix :
   having only one row.

5. column matrix :
   having only one column. 

6. Scalar matrices :
   having equal diagonal values and 0 on the rest.

7. Identity matrix :
   having 1 as the diagonal values and 0 on the rest.
   . symbol is I.

8. zero matrix : 
   null matrix having zeros.

9. Equal matrices :
   if each element is same from the corresponding matrix.

10. Negative matrix : 
    if having + sign, we change it to - and if having - sign we change it to +.

11. transpose matrix :
    Swapping rows and columns. 

12. Symmetric matrix :
    A matrix that is equal to its transpose.

13. Asymmetric matrix : 
    A matrix that is not equal to its transpose.

14. Idempotent matrix : 
    A matrix when multiplied by itself gives the same matrix back.
    A*A = A
    
    <img src = "https://github.com/Maanvitha6/GENAI-CLASS-1/blob/main/Assets/matrices-1.jpeg">
    <img src = "https://github.com/Maanvitha6/GENAI-CLASS-1/blob/main/Assets/matrices-2.jpeg">

15. Determinant of a matrix :
    The determinant is a scalar value that can be calculated from a square matrix (same number of rows and columns).
    Properties:
    . Only defined for square matrices (e.g., 2×2, 3×3).

    . If determinant = 0, the matrix is singular (not invertible).

    . If determinant ≠ 0, the matrix is invertible.

    <img src = "https://github.com/Maanvitha6/GENAI-CLASS-1/blob/main/Assets/determinant%20matrix.png">

16. Inverse of a matrix :
    
    inverse of 2*2 matrix :
    
    <img src = "https://github.com/Maanvitha6/GENAI-CLASS-1/blob/main/Assets/inverse%20matrix.png">

    inverse of 3*3 matrix :

    <img src = ">


16. Scalar :-
    A scalar is a single number or quantity that represents magnitude only, without direction.
    
    
# Vectors:- 
1. vector:
   vector is a direction.
   .A vector is a quantity that has both:
    Magnitude (how much).
    Direction (where).

    Example: 
    Imagine you're walking:
    5 steps forward → that’s a vector (distance + direction).
    If you just say 5, that’s just a number (called a scalar).

. Equations for vectors are :-
  
  <img src = "https://github.com/Maanvitha6/GENAI-CLASS-1/blob/main/Assets/vector%201.png">
  <img src = "https://github.com/Maanvitha6/GENAI-CLASS-1/blob/main/Assets/vector%202.png">

2. Vector space :
   Collection of two vectors 
   . that can add together.
   . multiply by numbers (scalars) and still stay inside the space.

   Example:
   . Movements of a car on a flat road = 2D vector space.
        -> Every movement = a vector.
        ->You can add movements and scale them.
        ->The set of all possible movements forms a vector space.
      
3. eigen vector :
   An eigenvector is a special kind of vector that does not change direction when a matrix (like a transformation) is applied to it.

   <img src = "https://github.com/Maanvitha6/GENAI-CLASS-1/blob/main/Assets/eigen%20vector.png">

4. eigen value :
   A number that tells how much the eigenvector gets stretched.

5. Distance between 2 vectors :
   The distance between two vectors means how far apart they are.

6. Angle between 2 vectors :
   
   <img src = "https://github.com/Maanvitha6/GENAI-CLASS-1/blob/main/Assets/distance%20angle%20vectors.jpeg" >

   # TYPES OF ANGLES : 
   1. Acute angle
   2. right angle
   3. obtuse angle
   4. zero angle
   5. straight angle

      * Acute (0°–90°)	- Going mostly in same direction  - Two people walking in slightly different paths.
      * Right (90°) - 	Perpendicular directions -	One going north, one going east.
      * Obtuse (90°–180°) - 	Going in wide different directions - One forward, one backward-diagonal.
      * Zero (0°)	- Same exact direction - 	Two cars on same road, same direction.
      * Straight (180°) - 	Completely opposite directions -	One north, one south.

   --> Real-time example based on these vector concepts :




1.  Linear Independence :
. No vector in the set can be made by adding or multiplying the other vector in the set.
  Example :
  Let’s take vectors:
  A = (1, 0), B = (0, 1)
  You can’t make A using B or B using A.
  So they are linearly independent.

2. Basis :
. A basis is a set of linearly independent vectors that can be used to make any vector in that space using addition and scalar  multiplication. 

3. Rank :
   . It’s the number of linearly independent rows or columns in a matrix.

   Example : 
   --> If we are delivering food, just imagine we should use only 2 routes.
        1. Route A (go north).
        2. Route B(go east).

   * We cant make route A with Route B and also we cant make Route B with Route A.
   so, these are LINEARLY INDEPENDENT.

   * Now imagine you want to reach any location in the city by combining your routes.

     If you use:
     Route A (north).
     Route B (east).
     You can go anywhere in the city by combining these (e.g., north + east, or 3 steps east and 2 steps north).
     So, Route A and B together form a BASIS.

   * The rank tells us how many directions or unique routes we actually have.

     we have 2 directions: north and east → Rank = 2
     If you only had 1 direction (say only north), you could only move in a line → Rank = 1.
