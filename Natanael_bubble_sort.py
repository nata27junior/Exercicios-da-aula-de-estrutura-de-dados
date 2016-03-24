import unittest


def bubble_sort(seq):
    # vai ser O(N**2) para tempo de execução e O(N) para memoria
    n=len(seq)
    i=0
    j=0
    flag=1
    if n==0:
            return  []
    elif n==1:
            return  seq
    elif n==2:
        seq[i,i+1]==seq[i+1,i]
        return  seq

    else:
        for i_corrente in range(n):
            for i_inicio in range(n-1):
                if seq[i_inicio]>seq[i_corrente]:
                   seq[i_inicio],seq[i_corrente]=seq[i_corrente],seq[i_inicio]




        return seq




class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
