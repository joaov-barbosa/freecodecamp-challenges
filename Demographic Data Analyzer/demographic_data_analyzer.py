import pandas as pd

# path = './adult.data'
# column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
#                 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
#                 'hours-per-week', 'native-country', 'salary']
# data = pd.read_csv(path, header=None, names=column_names)



#Quantas pessoas de cada raça estão representadas neste conjunto de dados? Esta deve ser uma série Pandas com nomes de raças como rótulos de índice. ( racecoluna)
def percentual_pessoas_formados_mais50k(data):
#Contar o número de pessoas com bacharelado
 formados_mais50k = ((data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (data['salary'] == '>50K')).sum()
#Calcular a porcentagem de pessoas com bacharelado
 porcentagem_formados_mais50k = (formados_mais50k / len(data)) * 100
 return porcentagem_formados_mais50k

def contar_racas(data):
 race_counts = data['race'].value_counts()
 return race_counts

#Qual é a idade média dos homens?
def media_idade_homens(data):
#Filtrar o DataFrame para incluir apenas os homens
 male_data = data[data['sex'] == 'Male']
#Calcular a idade média dos homens
 average_age_men = male_data['age'].mean()
 return average_age_men

#Qual é a porcentagem de pessoas que possuem bacharelado?
def percentual_pessoas_bacharel(data):
#Contar o número de pessoas com bacharelado
 bach_count = (data['education'] == 'Bachelors').sum()
#Calcular a porcentagem de pessoas com bacharelado
 percentage_bachelors = (bach_count / len(data)) * 100
 return percentage_bachelors

#Que porcentagem de pessoas sem educação avançada ganha mais de 50 mil?
def sem_educacao_avancada_mais50k(data):
 sem_educacao_avancada_mais50k = data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (data['salary'] == '>50K')]
# Calcular o número total de pessoas que atendem a esses critérios
 total_sem_educacao_avancada_mais50k = len(sem_educacao_avancada_mais50k)
 return total_sem_educacao_avancada_mais50k

#Qual é o número mínimo de horas que uma pessoa trabalha por semana?
def numero_minimo_trabalhado_horas(data):
 min_hours_per_week = data['hours-per-week'].min()
 return min_hours_per_week

#Que porcentagem das pessoas que trabalham o número mínimo de horas por semana tem um salário superior a 50 mil?
def percentual_minimo_horas_mais50k(data):
 min_horas_semana = data['hours-per-week'].min()
 min_horas_trabalhandores = data[data['hours-per-week'] == min_horas_semana]
 min_mais50k = min_horas_trabalhandores[min_horas_trabalhandores['salary'] == '>50K']
 percentage_min_mais50k = (len(min_mais50k) / len(data)) * 100
 return percentage_min_mais50k

#Qual país tem a maior porcentagem de pessoas que ganham mais de 50 mil e qual é essa porcentagem?
def  pais_com_maior_porcentagem_pessoas_mais50k(data):
 contagem_renda_alta = data[data['salary'] == '>50K']['native-country'].value_counts()
 contagem_total = data['native-country'].value_counts()
 porcentagem_renda_alta_por_pais = (contagem_renda_alta / contagem_total) * 100
 pais_maior_porcentagem = porcentagem_renda_alta_por_pais.idxmax()
 maior_porcentagem = porcentagem_renda_alta_por_pais.max()
 resposta= f"O país com a maior porcentagem de pessoas com renda alta é {pais_maior_porcentagem} com {maior_porcentagem:.2f}%."
 return resposta

#Identifique a ocupação mais popular para quem ganha mais de 50 mil na Índia.
def ocupacao_mais_popular_india_mais50k(data):
 filtro = (data['salary'] == '>50K') & (data['native-country'] == 'India')
 pessoas_renda_alta_india = data[filtro]
 ocupacao_mais_popular = pessoas_renda_alta_india['occupation'].value_counts().idxmax()
 return ocupacao_mais_popular