/*
write program to the following CSP that works on SWI-Prolog
Vars = E , A , R , D
D(E) = D(A)  = D(R) = D(D) = [0 .. 9]
Constraints:
        D > 0
        E > 0
        1000*D + 100*E + 10*E + R = 300*E + 30*A + 3*R

*/

% 1. Define the domain of the variables
domain([E,A,R,D],0,9).

% 2. Define the constraints
% 2.1. D > 0
D #> 0.

% 2.2. E > 0
E #> 0.

% 2.3. 1000*D + 100*E + 10*E + R = 300*E + 30*A + 3*R
1000*D + 100*E + 10*E + R #= 300*E + 30*A + 3*R.

% 3. Labeling
labeling([E,A,R,D]).

/*
?- Rev.
E = 2,
A = 3,
R = 5,
D = 7
*/
