## =========================================================================
## @author Anderson Alvarado
## =========================================================================
from maxima_diferencia import *

f_write = open("result_cases.txt", "w")
f_write.write("Valor Deseado\tValor Obtenido\n")
with open("test_cases.in", "r") as f_in, open("test_cases.out", "r") as f_out:
    for line1, line2 in zip(f_in.readlines(), f_out.readlines()):
        line1 = line1.strip()
        line2 = line2.strip()
        if line1 != "10000":
            S = [float(x) for x in line1.split(" ")]
            expected_value = line2.split(" ")
            obtained_value = maxima_i_diferencia(S)
            f_write.write(str(expected_value[1])+"\t"+str(obtained_value)+"\n")

f_write.close()