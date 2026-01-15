import os

def analisar_texto(texto, palavra_de_busca):
    texto_limpo = texto.replace(".", "").replace(",", "").lower()
    lista_palavras = texto_limpo.split()
    qtd_palavras = len(lista_palavras)

    maior_palavra = " "
    for palavra in lista_palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    
    print(f"--- Relatório ---")
    print(f"Total de palavras: {qtd_palavras}")
    print(f"Maior palavra encontrada: {maior_palavra}")

    if palavra_de_busca in lista_palavras:
        print(f"Busca: a palavra {palavra_de_busca} está presente no texto.")
    else: 
        print(f"Busca: a palavra {palavra_de_busca} não foi encontrada.")


if __name__ == "__main__":
   nome_arquivo = input("Digite o nome do arquivo (ex: arquivo.txt): ")
   if os.path.exists(nome_arquivo):
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                meu_texto = arquivo.read().lower()
            
            busca = input("Qual palavra você deseja buscar? ").strip().lower()
            analisar_texto(meu_texto, busca)
            
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
   else:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado na pasta.")








