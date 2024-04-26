import numpy as np

def calculate(numeros):
    if len(numeros) != 9:
        raise ValueError("A lista deve conter nove números.")

    # Converter a lista em uma matriz numpy 3x3
    matriz = np.array(numeros).reshape(3, 3)

    # Calcular média, variância, desvio padrão, máximo, mínimo e soma ao longo dos eixos e para a matriz achatada
    media = [list(np.mean(matriz, axis=0)), list(np.mean(matriz, axis=1)), np.mean(matriz)]
    variancia = [list(np.var(matriz, axis=0)), list(np.var(matriz, axis=1)), np.var(matriz)]
    desvio_padrao = [list(np.std(matriz, axis=0)), list(np.std(matriz, axis=1)), np.std(matriz)]
    maximo = [list(np.max(matriz, axis=0)), list(np.max(matriz, axis=1)), np.max(matriz)]
    minimo = [list(np.min(matriz, axis=0)), list(np.min(matriz, axis=1)), np.min(matriz)]
    soma = [list(np.sum(matriz, axis=0)), list(np.sum(matriz, axis=1)), np.sum(matriz)]

    # Retornar o dicionário conforme especificado
    return {
        'mean': media,
        'variance': variancia,
        'standard deviation': desvio_padrao,
        'max': maximo,
        'min': minimo,
        'sum': soma
    }