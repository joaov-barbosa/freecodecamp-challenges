import pandas as pd
import demographic_data_analyzer as dda

# Leitura do arquivo DataFrame no arquivo main
path = './adult.data'
column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                'hours-per-week', 'native-country', 'salary']
data = pd.read_csv(path, header=None, names=column_names)

# Chamadas para cada método do arquivo demographic_data_analyzer.py
print("Porcentagem de pessoas com educação avançada ganhando mais de 50 mil:", dda.percentual_pessoas_formados_mais50k(data))
print("Número de pessoas de cada raça:", dda.contar_racas(data))
print("Média de idade dos homens:", dda.media_idade_homens(data))
print("Porcentagem de pessoas com bacharelado:", dda.percentual_pessoas_bacharel(data))
print("Número de pessoas sem educação avançada ganhando mais de 50 mil:", dda.sem_educacao_avancada_mais50k(data))
print("Número mínimo de horas trabalhadas por semana:", dda.numero_minimo_trabalhado_horas(data))
print("Porcentagem de pessoas que trabalham o número mínimo de horas por semana e ganham mais de 50 mil:", dda.percentual_minimo_horas_mais50k(data))
print(dda.pais_com_maior_porcentagem_pessoas_mais50k(data))
print("Ocupação mais popular para quem ganha mais de 50 mil na Índia:", dda.ocupacao_mais_popular_india_mais50k(data))