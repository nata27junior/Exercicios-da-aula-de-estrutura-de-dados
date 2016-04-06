import unittest

#seq = [1, 1, 2]
# tempo: O(n**2)  memoria: O(log(n))

def _quick_recursivo(seq, inicio, final):
    if inicio >= final:
        return seq
    n=len(seq)
    indice_pivot = final
    pivot = seq[indice_pivot]
    i_menor = inicio
    i_maior = final - 1



    #posicionando pivot
    for i in range(n):

        if i_menor <= i_maior and seq[i_menor] <= pivot:
            i_menor += 1

        elif i_menor <= i_maior and seq[i_maior] >= pivot:
            i_maior -= 1

        elif i_menor < i_maior:
           seq[i_maior], seq[i_menor] = seq[i_menor], seq[i_maior]


    seq[i_menor], seq[final] = seq[final], seq[i_menor]
    # Resolver para sublista da esquerda
    _quick_recursivo(seq, inicio, i_menor - 1)

    # Resolver para sublista da direita
    _quick_recursivo(seq, i_menor + 1, final)

    return seq


def quick_sort(seq):
    return _quick_recursivo(seq, 0, len(seq) - 1)


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
