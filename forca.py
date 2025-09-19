#  Imports
import random
import os

#  Função para carregar palavras de um arquivo
def carregar_palavras(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []
    
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip().lower() for linha in arquivo if linha.strip()]
    return palavras

#  Escolhe uma palavra aleatória da lista
def escolher_palavra(lista):
    return random.choice(lista).lower()

#  Mostra o progresso da palavra com letras já usadas
def mostrar_palavra(palavra, letras_usadas):
    return ' '.join([letra if letra in letras_usadas else '_' for letra in palavra])

#  Função principal do jogo 
def jogar_forca(palavra):
    letras_usadas = set()
    tentativas = 7

    print("🎮 Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra(palavra, letras_usadas))
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Digite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já usou essa letra. Tente outra.")
            continue

        letras_usadas.add(letra)

        if letra not in palavra:
            tentativas -= 1
            print("Letra incorreta!")

        if all(l in letras_usadas for l in palavra):
            print(f"\n Parabéns! Você ganhou! A palavra era: {palavra}")
            return

    print(f"\n Você perdeu! A palavra era: {palavra}")

#  Executa o jogo
if __name__ == "__main__":
    palavras = carregar_palavras("palavras.txt")
    
    if not palavras:
        print("⚠️ Não foi possível iniciar o jogo. Nenhuma palavra carregada.")
    else:
        while True:
            palavra_escolhida = escolher_palavra(palavras)
            jogar_forca(palavra_escolhida)

            resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
            if resposta != 's':
                print("👋 Obrigado por jogar! Até a próxima!")
                input("Pressione Enter para sair...")
                break