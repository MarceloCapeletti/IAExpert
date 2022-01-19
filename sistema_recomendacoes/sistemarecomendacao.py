# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 13:38:02 2021

@author: leloc
"""

from basededados import avaliacoesUsuario
from math import sqrt

def euclidiana(usuario1, usuario2):
    si = {}
    for item in avaliacoesUsuario[usuario1]:
        if item in avaliacoesUsuario[usuario2]: si[item] = 1
    if len(si) == 0: return 0
    
    soma = sum([pow(avaliacoesUsuario[usuario1][item] - avaliacoesUsuario[usuario2][item],2) for item in avaliacoesUsuario[usuario1] if item in avaliacoesUsuario[usuario2]])
    
    return 1 / (1+sqrt(soma))

def getSimilares(usuario):
    similaridade = [(euclidiana(usuario,outro),outro)
                    for outro in avaliacoesUsuario if outro != usuario]
    similaridade.sort()
    similaridade.reverse()
    return similaridade
    
def getRecomendacoes(usuario):
    totais = {}
    somaSimilaridade={}
    
    for outro in avaliacoesUsuario:
        if outro == usuario: continue
        
        similaridade = euclidiana(usuario,outro)
        
        if similaridade <=0: continue
        
        for item in avaliacoesUsuario[outro]:
            if item not in avaliacoesUsuario[usuario]:
                totais.setdefault(item,0)
                totais[item] += avaliacoesUsuario[outro][item] * similaridade
                somaSimilaridade.setdefault(item,0)
                somaSimilaridade[item] += similaridade
    ranking=[(total / somaSimilaridade[item],item) for item,total in totais.items()]
    ranking.sort()
    ranking.reverse()
    return ranking
    
print(getRecomendacoes('Leonardo'))
