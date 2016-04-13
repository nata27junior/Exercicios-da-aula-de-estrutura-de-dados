def busca_binaria(seq, procurado):
    """
     O(N) para tempo de execução e O(1) para espaço em memória
    Deve retornar o índice onde o elemento deveriar ser inserido em lista ordenada
    :param procurado: elemento a ser procurado
    :param seq: sequencia a ser pesquisada

    :return: int
    """
    n=len(seq)
    i_menor = 0
    metade = n // 2 #divisao interia
    i_maior = n

    if n == 0:
        return 0

    while i_menor < i_maior:
        if procurado <= seq[metade]:
            i_maior = metade
            metade = (i_menor + i_maior) // 2
        else:
            i_menor = metade + 1
            metade = (i_menor + i_maior) // 2

    return i_menor


import unittest


class BuscaBinariaTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertEqual(0, busca_binaria([], 1))
        self.assertEqual(0, busca_binaria([], 2))
        self.assertEqual(0, busca_binaria([], 3))

    def teste_lista_unitaria(self):
        self.assertEqual(0, busca_binaria([1], 0))
        self.assertEqual(0, busca_binaria([1], 1))
        self.assertEqual(1, busca_binaria([1], 2))
        self.assertEqual(1, busca_binaria([1], 3))
        self.assertEqual(1, busca_binaria([1], 4))

    def teste_lista_nao_unitaria(self):
        lista = list(range(10))
        self.assertEqual(0, busca_binaria(lista, -2))
        self.assertEqual(0, busca_binaria(lista, -1))
        for i in lista:
            self.assertEqual(i, busca_binaria(lista, i))
        self.assertEqual(10, busca_binaria(lista, 10))
        self.assertEqual(10, busca_binaria(lista, 11))
        self.assertEqual(10, busca_binaria(lista, 12))

    def teste_lista_elementos_repetidos(self):
        lista = [1, 1, 1, 2, 2, 2]
        self.assertEqual(0, busca_binaria(lista, 1))
        self.assertEqual(3, busca_binaria(lista, 2))
