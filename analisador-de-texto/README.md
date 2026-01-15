# Analisador de Texto  (Python)

Este projeto é um utilitário de linha de comando (CLI) desenvolvido para realizar análises estatísticas básicas e buscas em arquivos de texto. Foi criado como parte dos meus estudos em **Ciência da Computação** para consolidar conceitos de manipulação de arquivos, estruturas de dados e lógica de programação.

## Funcionalidades

* **Leitura Dinâmica:** O programa solicita o nome do arquivo `.txt` e valida sua existência.
* **Processamento de Dados:** * Contagem total de palavras.
    * Identificação da maior palavra presente no corpo do texto.
* **Sistema de Busca:** Verifica a ocorrência de palavras-chave de forma insensível a maiúsculas/minúsculas (*case-insensitive*).
* **Tratamento de Erros:** Implementação de blocos `try/except` para lidar com falhas de leitura ou arquivos inexistentes.

## Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3
* **Bibliotecas:** `os` (Manipulação do Sistema Operacional).
* **Conceitos de Engenharia de Software:**
    * **Modularização:** Uso de funções para separar responsabilidades.
    * **Context Managers:** Uso de `with open()` para gerenciamento seguro de memória.
    * **Normalização de Dados:** Uso de `.lower()` e `.strip()` para garantir buscas precisas.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/analisador-texto-python.git](https://github.com/SEU_USUARIO/analisador-texto-python.git)