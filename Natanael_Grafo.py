class Arco():
    def __init__(self, origem, destino, valor):
        self.valor = valor
        self.vertices = (origem, destino)

    def __hash__(self):
        return hash(self.vertices + (self.valor,))

    def __eq__(self, arco):
        return (self.valor,) + self.vertices == (arco.valor,) + arco.vertices

    def __repr__(self):
        return 'Arco({!r}, {!r}, {!r})'.format(self.vertices[0], self.vertices[1], self.valor)
    def oposto(self,s):
        if s==self.vertices[0]:
            return self.vertices[1]
        else:
            return self.vertices[0]
class Grafo():

    def __init__(self):
        self.vertice = ()
        self.arco = ()
        self.adjacente = {}

    def vertices(self):
        return self.vertice

    def adicionar_vertice(self, cidade):
        self.vertice += cidade,

    def arcos(self, cidade):
        arco_encontrado = ()
        for arco_teste in self.arco:
            if cidade in arco_teste.vertices:
                arco_encontrado += arco_teste,
        return arco_encontrado

    def adicionar_arco(self, arco):
        self.arco += arco,
        vertice_1 = arco.vertices[0]
        vertice_2 = arco.vertices[1]
        for cidade in self.vertice:
            if cidade in arco.vertices:
                if cidade not in self.adjacente:
                    if cidade != vertice_1:
                        self.adjacente[cidade] = (vertice_1,arco)
                    else:
                        self.adjacente[cidade] = (vertice_2,arco)
                else:
                    if cidade != vertice_1:
                        self.adjacente[cidade] += (vertice_1,arco)
                    else:
                        self.adjacente[cidade] += (vertice_2,arco)


    def adjacencias(self, cidade):
        if self.adjacente:
            adjacencias = ()
            for x in range(0,len(self.adjacente[cidade]),2):
                adjacencias += self.adjacente[cidade][x],
            return adjacencias
        return self.adjacente

    def caminho(self, cidade1, cidade2):
        if cidade1 == cidade2:
            return [cidade1]
        elif self.arco == ():
            return []
        elif cidade2 in self.adjacente[cidade1][0]:
            return [cidade1, cidade2]
        else:
            cidade_atual = cidade1
            lista_cidades = []
            lista_cidades.append(cidade_atual)
            while True:
                for cidade in self.adjacente:
                    if cidade == cidade_atual:
                        for origem in self.adjacente[cidade]:
                            if isinstance(origem, Arco) and (origem.vertices[0] not in lista_cidades or origem.vertices[1] not in lista_cidades):
                                if origem.vertices[0] != cidade:
                                    cidade_atual = origem.vertices[0]
                                    break
                                else:
                                    cidade_atual = origem.vertices[1]
                                    break
                        lista_cidades.append(cidade_atual)
                    if cidade_atual == cidade2:
                        return lista_cidades


    def calcular_melhores_caminhos_partindo_de(self,vertice):
        caminho = {vertice: [vertice]}
        visitados = [vertice]
        atual = {vertice: 0}


        while (len(visitados) < len(self.vertice)):
            for vert in self.arcos(vertice):
                if vert.oposto(vertice) not in visitados:
                    if vert.oposto(vertice) not in atual.keys():
                        atual[vert.oposto(vertice)] = atual[vertice] + vert.valor
                    else:
                        if atual[vert.oposto(vertice)] > atual[vertice] + vert.valor:
                            atual[vert.oposto(vertice)] = atual[vertice] + vert.valor

            for x, y in atual.items():
                if x not in visitados:
                    menor = y
                    ponto = x
                    break
            for x, y in atual.items():
                if x not in visitados:
                    if y < menor:
                        menor = y
                        ponto = x

            if ponto not in visitados:
                visitados.append(ponto)
            vertice = ponto
            for x in self.arcos(vertice):
                if x.oposto(ponto) in visitados:
                    menor = atual[x.oposto(vertice)] + x.valor
                    break

            for x in self.arcos(vertice):
                if x.oposto(vertice) in visitados:

                    if atual[x.oposto(vertice)] + x.valor <= menor:
                        menor = atual[x.oposto(vertice)] + x.valor
                        ponto = x.oposto(vertice)
                        val = x.valor

            caminho[vertice] = caminho[ponto] + [val, vertice]
        caminhos = {}
        for x, y in atual.items():
            caminhos[x] = tuple()
            caminhos[x] = caminhos[x] + (y, caminho[x])
        return caminho


import unittest


class ArcoTestes(unittest.TestCase):
    def teste_init(self):
        arco = Arco('origem', 'destino', 1)
        self.assertTupleEqual(('origem', 'destino'), arco.vertices)
        self.assertEqual(1, arco.valor)

    def teste_oposto(self):
        arco = Arco('origem', 'destino', 1)
        self.assertEqual('origem', arco.oposto('destino'))
        self.assertEqual('destino', arco.oposto('origem'))


# Dados a serem usados nos testes

# Dados de vérticos
bertioga = 'Bertioga'
caragua = 'Caragua'
jacarei = 'Jacareí'
mogi = 'Mogi da Cruzes'
santos = 'Santos'
sjc = 'São José dos Campos'
sao_paulo = 'São Paulo'
taubate = 'Taubaté'

vertices_cidades = (bertioga,
                    caragua,
                    jacarei,
                    mogi,
                    santos,
                    sjc,
                    sao_paulo,
                    taubate)
# Dados de arcos
arco_tauba_sjc = Arco(taubate, sjc, 43900)
arco_scj_jaca = Arco(sjc, jacarei, 13200)
arco_scj_caragua = Arco(sjc, caragua, 86900)
arco_caragua_bertioga = Arco(caragua, bertioga, 114000)
arco_bertioga_mogi = Arco(bertioga, mogi, 48700)
arco_mogi_jaca = Arco(mogi, jacarei, 54300)
arco_mogi_sp = Arco(mogi, sao_paulo, 61900)
arco_jaca_sp = Arco(jacarei, sao_paulo, 81800)
arco_santos_sp = Arco(santos, sao_paulo, 72800)
arco_santos_bertioga = Arco(santos, bertioga, 74400)

arcos_distancias = (arco_tauba_sjc,
                    arco_scj_jaca,
                    arco_scj_caragua,
                    arco_caragua_bertioga,
                    arco_bertioga_mogi,
                    arco_mogi_jaca,
                    arco_mogi_sp,
                    arco_jaca_sp,
                    arco_santos_sp,
                    arco_santos_bertioga)


class GrafoTestes(unittest.TestCase):
    def teste_adicionar_vertice(self):
        grafo = Grafo()
        self.assert_mesmo_elementos(tuple(), grafo.vertices())
        grafo.adicionar_vertice(santos)
        self.assert_mesmo_elementos((santos,), grafo.vertices())
        grafo.adicionar_vertice(jacarei)
        self.assert_mesmo_elementos((santos, jacarei), grafo.vertices())
        grafo.adicionar_vertice(mogi)
        self.assert_mesmo_elementos((santos, jacarei, mogi), grafo.vertices())
        grafo.adicionar_vertice(caragua)
        self.assert_mesmo_elementos((santos, jacarei, mogi, caragua), grafo.vertices())

    def teste_adicionar_arco(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        self.assert_mesmo_elementos(tuple(), grafo.arcos(sjc))
        self.assert_mesmo_elementos(tuple(), grafo.adjacencias(sjc))
        grafo.adicionar_vertice(jacarei)
        self.assert_mesmo_elementos(tuple(), grafo.arcos(jacarei))
        self.assert_mesmo_elementos(tuple(), grafo.adjacencias(sjc))
        self.assert_mesmo_elementos(tuple(), grafo.adjacencias(jacarei))
        grafo.adicionar_arco(arco_scj_jaca)
        self.assert_mesmo_elementos((arco_scj_jaca,), grafo.arcos(jacarei))
        self.assert_mesmo_elementos((arco_scj_jaca,), grafo.arcos(sjc))
        self.assert_mesmo_elementos((jacarei,), grafo.adjacencias(sjc))
        self.assert_mesmo_elementos((sjc,), grafo.adjacencias(jacarei))
        grafo.adicionar_vertice(taubate)
        grafo.adicionar_arco(arco_tauba_sjc)
        self.assert_mesmo_elementos((arco_scj_jaca, arco_tauba_sjc), grafo.arcos(sjc))
        self.assert_mesmo_elementos((arco_tauba_sjc,), grafo.arcos(taubate))

        self.assert_mesmo_elementos((sjc,), grafo.adjacencias(jacarei))
        self.assert_mesmo_elementos((sjc,), grafo.adjacencias(taubate))
        self.assert_mesmo_elementos((taubate, jacarei), grafo.adjacencias(sjc))

    def teste_caminho_para_proprio_vertice(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        self.assertListEqual([sjc], grafo.caminho(sjc, sjc))

    def teste_caminho_vertices_desconexos(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        self.assertListEqual([], grafo.caminho(sjc, jacarei))

    def teste_caminho_dois_vertices_conexos(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        grafo.adicionar_arco(arco_scj_jaca)
        self.assertListEqual([sjc, jacarei], grafo.caminho(sjc, jacarei))

    def teste_caminho_tres_vertices_conexos(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        grafo.adicionar_vertice(taubate)
        grafo.adicionar_arco(arco_scj_jaca)
        grafo.adicionar_arco(arco_tauba_sjc)

        self.assertListEqual([taubate, sjc, jacarei], grafo.caminho(taubate, jacarei))
        self.assertListEqual([taubate, sjc], grafo.caminho(taubate, sjc))

    def teste_caminho_4_vertices_conexos_nao_lineares(self):
        grafo = Grafo()
        grafo.adicionar_vertice(sjc)
        grafo.adicionar_vertice(jacarei)
        grafo.adicionar_vertice(mogi)
        grafo.adicionar_vertice(sao_paulo)
        grafo.adicionar_arco(arco_scj_jaca)
        grafo.adicionar_arco(arco_jaca_sp)
        grafo.adicionar_arco(arco_mogi_jaca)
        grafo.adicionar_arco(arco_mogi_sp)

        caminho = grafo.caminho(sjc, sao_paulo)
        self.assertTrue([sjc, jacarei, sao_paulo] == caminho or [sjc, jacarei, mogi, sao_paulo] == caminho)

    def assert_mesmo_elementos(self, iteravel, outro_iteravel):
        "Método auxiliar para asserção de elementos"
        self.assertSetEqual(set(iteravel), set(outro_iteravel))
