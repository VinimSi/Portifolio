from TV import *
#classe de Tv
tv = Tv("Sony","Sony-1234")

#classe de controle
controle = Controle(tv)
controle.sintonizaCanal("Globo") #inserindo canal na var tv.lista_de_canais, so que parece q ele n salva os canais
controle.trocaCanal("Globo") #colocando o canal atual

#saida
print(f"TV: {tv.modelo} \nFabricante: {tv.fabricante} \nCanal atual {tv.canal_atual} \nCanais disponiveis: {tv.lista_de_canais}")