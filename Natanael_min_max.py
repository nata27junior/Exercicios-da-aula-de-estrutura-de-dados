# A função min_max deverá rodar em O(n) e o código não pode usar nenhuma
# lib do Python (sort, min, max e etc)
# Não pode usar qualquer laço (while, for), a função deve ser recursiva
# Ou delegar a solução para uma função puramente recursiva
import unittest

seq = []
maior = 0
menor = 0
teste = 0

def menor(seq):
    if teste < seq[- 1]:
        return teste
    else:
        return seq[-1]

def maior(seq):

    if teste > seq[-1]:
        return teste
    else:
        return seq[-1]

def min_max(seq):

    if len(seq) == 0:
        return (None, None)
    elif len(seq) <=1:
        return (seq[0],seq[0])
    elif len(seq)>1:
        return (menor(seq), maior(seq))

    '''
    :param seq: uma sequencia
    :return: (min, max)
    Retorna tupla cujo primeiro valor mínimo (min) é o valor
    mínimo da sequencia seq.
    O segundo é o valor máximo (max) da sequencia
    '''



class MinMaxTestes(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertTupleEqual((None, None), min_max([]))

    def test_lista_len_1(self):
        self.assertTupleEqual((1, 1), min_max([1]))

    def test_lista_consecutivos(self):
        self.assertTupleEqual((0, 500), min_max(list(range(501))))


if __name__ == '__main__':
    unittest.main()

