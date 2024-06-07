# Treinando-Desafios-de-C-digos-com-IAs-Generativas-


#1) Definir o mapeamento das características para os modelos Claude 3.
#2) Receber a entrada (a característica fornecida).
#3) Buscar a característica no dicionário.
#4) Retornar o nome do modelo correspondente ou uma mensagem de "Modelo não encontrado" caso a característica não exista no dicionário.

##Exemplo de Implementação em Python:


def identificar_modelo_caracteristica(caracteristica):
    # Dicionário com mapeamento de características para modelos
    caracteristicas_para_modelos = {
        "automatizar tarefas": "Claude 3 Opus",
        "equilíbrio ideal entre inteligência e velocidade": "Claude 3 Sonnet",
        "desempenho otimizado para NLP": "Claude 3 Haiku",
        "processamento de linguagem natural avançado": "Claude 3 Opus",
        "alta precisão em análise de dados": "Claude 3 Sonnet",
        "resposta rápida e eficiente": "Claude 3 Haiku"
    }
    
    # Verifica se a característica está no dicionário
    if caracteristica in caracteristicas_para_modelos:
        return caracteristicas_para_modelos[caracteristica]
    else:
        return "Modelo não encontrado."

# Testando a função
caracteristica = input("Digite a característica do modelo: ")
resultado = identificar_modelo_caracteristica(caracteristica)
print(resultado)


import sys

# Dicionário associando características aos modelos Claude 3
caracteristicas_modelos = {
    "automatizar tarefas": "Claude 3 Opus",
    "pesquisa e desenvolvimento": "Claude 3 Opus",
    "resposta rápida e capacidade de resposta quase instantânea": "Claude 3 Haiku",
    "motores de chatbots de lojas": "Claude 3 Haiku",
    "moderação de conteúdo": "Claude 3 Haiku",
    "processamento de tarefas mais básicas": "Claude 3 Haiku",
    "raciocínio cuidadoso": "Claude 3 Sonnet",
    "processamento de dados": "Claude 3 Sonnet",
    "aplicações de vendas": "Claude 3 Sonnet",
    "extração de texto de imagens": "Claude 3 Sonnet",
    "equilíbrio ideal entre inteligência e velocidade": "Claude 3 Sonnet",
}

# Função para encontrar o modelo correspondente à característica fornecida
def encontrar_modelo(caracteristica_fornecida, caracteristicas_modelos):
    for caracteristica, modelo in caracteristicas_modelos.items():
        if caracteristica.lower() in caracteristica_fornecida.lower():
            return modelo
    return "Modelo não encontrado."

# Entrada do usuário
caracteristica_fornecida = sys.stdin.readline().strip()

# Encontrar e imprimir o modelo correspondente
modelo_correspondente = encontrar_modelo(caracteristica_fornecida, caracteristicas_modelos)
print(modelo_correspondente)
