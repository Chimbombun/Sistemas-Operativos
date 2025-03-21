Este programa intenta simular el algoritmo de peor ajuste (worst fit) en la asignación de memoria continua.
Busca el bloque de memoria más grande donde quepa un proceso, y lo coloca allí.

Se me presentaron unos cuantos errores que no pude solucionar

.F...EF....
======================================================================
ERROR: test_req_choose_middle_index (test_basic_worst_fit.TestBasicWorstFit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/madiazv1/Documents/Sistemas-Operativos/copa-folder/test_basic_worst_fit.py", line 48, in test_req_choose_middle_index
    self.assertEqual(search[3], 1)
TypeError: 'NoneType' object is not subscriptable

======================================================================
FAIL: test_req_choose_last_index (test_basic_worst_fit.TestBasicWorstFit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/madiazv1/Documents/Sistemas-Operativos/copa-folder/test_basic_worst_fit.py", line 33, in test_req_choose_last_index
    self.assertEqual(search[3], 0)
AssertionError: 2 != 0

======================================================================
FAIL: test_req_choose_middle_len (test_basic_worst_fit.TestBasicWorstFit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/madiazv1/Documents/Sistemas-Operativos/copa-folder/test_basic_worst_fit.py", line 56, in test_req_choose_middle_len
    self.assertEqual(len(search[0]), len_work_memory)
AssertionError: 2 != 3

----------------------------------------------------------------------
Ran 11 tests in 0.004s

FAILED (failures=2, errors=1)

test_req_choose_middle_index
Este test quiere que el proceso se asigne al índice 1 (el segundo bloque).
El código retorna None, lo que significa que no encontró ningún bloque donde quepa el proceso.

test_req_choose_last_index
Este test quiere que el proceso se ubique en el bloque 0, pero el código lo puso en el índice 2.

test_req_choose_middle_len
Este test espera que la cantidad de bloques siga siendo 3 después de asignar el proceso.
Pero el código redujo la lista a 2, es decir, eliminó un bloque
