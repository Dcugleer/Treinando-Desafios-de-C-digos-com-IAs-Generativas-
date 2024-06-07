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
