import unittest


def insertion_sort(seq):
    '''  tempo de O(N**2) mas quando esta ordenado é O(N)  e  memória O(N) '''
    for i_corrente in range(1,len(seq)):
        aux = seq[i_corrente]
        i_inicio = i_corrente-1
        while i_inicio>=0 and aux<seq[i_inicio]:
            seq[i_inicio+1] = seq[i_inicio]
            i_inicio=i_inicio-1
        seq[i_inicio+1] = aux

    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
