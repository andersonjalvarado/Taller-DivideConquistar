## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================
##Usado para probar el algoritmo de la maxima i-diferencia en el Taller de Divide y Venceras
'''
Usage: create a sequence of experiments like:

for i in `seq 0 100 30000`;do \
  echo -n $i && echo -n " " && \
  python test_complejidad.py $i; done > plots.txt
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

then use "plots.txt" to draw the execution times (in seconds).
Here is an example using gnuplot:

plot "plots.txt" with linespoints title "Maxima_I_Diferencia"
'''

import sys, random, time
from maxima_diferencia import *

## -------------------------------------------------------------------------
def ExecAlgorithm( f, A, n = 5 ):
  t = float( 0 )
  for i in range( n ):
    S = A.copy( )
    st = time.time( )
    f( S )
    t += float( time.time( ) - st )
  # end for
  return t / float( n )
# end def

## -------------------------------------------------------------------------
o = 1000000
n = int( sys.argv[ 1 ] ) #tamaño del arreglo
S = [ random.randint( -o, o ) for i in range( n ) ]

max_dif = ExecAlgorithm( maxima_i_diferencia, S )

print(f"{max_dif:.3e}")

## eof - real_experiments_maxDifference.py