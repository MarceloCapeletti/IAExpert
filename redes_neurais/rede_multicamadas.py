
import numpy as np

def sigmoid(soma):
	return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
	return sig * (1 - sig)

#a = sigmoid(0.5)
#b = sigmoidDerivada(a)

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([[0],[1],[1],[0]])

#teste = np.concatenate((entradas,entradas),axis=1)


#pesos0 = np.array([[-0.425,-0.740,-0.961],
		#		   [0.358,-0.577,-0.469]])


#pesos1 = np.array([[-0.018],[-0.893],[0.148]])

pesos0 = 2*np.random.random((2,3)) -1
pesos1 = 2*np.random.random((3,1)) -1
	
epocas = 10000

taxaAprendizagem = 0.1
momento = 1
for j in range(epocas):
	camadaEntrada = entradas
	somaSinapse0 = np.dot(camadaEntrada,pesos0) #aqui só multiplicação das entradas e dos pesos (nao soma)
	camadaOculta = sigmoid(somaSinapse0)
	
	saidaSoma = np.dot(camadaOculta,pesos1)
	camadaSaida = sigmoid(saidaSoma)
	
	erroCamadaSaida = saidas - camadaSaida
	mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
	print("Erro: " + str(mediaAbsoluta))
	
	derivadaSaida = sigmoidDerivada(camadaSaida)
	deltaSaida = erroCamadaSaida*derivadaSaida
	#detasaida = derivada(saida) * erroSaida
	pesos1Transposta = pesos1.T
	deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
	deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)

	#ajuste dos pesos da camada oculta para camada de saida
	camadaOcultaTransposta = camadaOculta.T
	pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
	pesos1 = pesos1 * momento + (pesosNovo1*taxaAprendizagem)
	
	#ajuste dos pesos da camada de entrada para camada oculta
	camadaEntradaTransposta = entradas.T
	pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
	pesos0 = (pesos0 * momento) +(pesosNovo0 * taxaAprendizagem)