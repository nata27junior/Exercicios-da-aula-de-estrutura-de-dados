class Pilha():
   # Lista = []
    def __init__(self):
        self.Lista = []


    def topo(self):
        if self.Lista:
            return self.Lista[-1]
        raise PilhaVaziaErro()
    def vazia(self):
        return not bool (self.Lista)

    def empilhar(self, elemento):
        return self.Lista.append(elemento)

    def desempilhar(self):
        try:
            return self.Lista.pop()
        except IndexError:
            raise PilhaVaziaErro





class PilhaVaziaErro(Exception):
    pass





import unittest



class PilhaTestes(unittest.TestCase):
    def test_topo_lista_vazia(self):
        pilha = Pilha()
        self.assertTrue(pilha.vazia())
        self.assertRaises(PilhaVaziaErro, pilha.topo)

    def test_empilhar_um_elemento(self):
        pilha = Pilha()
        pilha.empilhar('A')
        self.assertFalse(pilha.vazia())
        self.assertEqual('A', pilha.topo())

    def test_empilhar_dois_elementos(self):
        pilha = Pilha()
        pilha.empilhar('A')
        pilha.empilhar('B')
        self.assertFalse(pilha.vazia())
        self.assertEqual('B', pilha.topo())

    def test_desempilhar_pilha_vazia(self):
        pilha = Pilha()
        self.assertRaises(PilhaVaziaErro, pilha.desempilhar)

    def test_desempilhar(self):
        pilha = Pilha()
        letras = 'ABCDE'
        for letra in letras:
            pilha.empilhar(letra)

        for letra_em_ordem_reversa in reversed(letras):
            letra_desempilhada = pilha.desempilhar()
            self.assertEqual(letra_em_ordem_reversa, letra_desempilhada)
