import argparse
import secrets
import string
import sys


def gerar_senha(tamanho):
    char = string.ascii_letters + string.digits + string.punctuation
    words = r"|\/?~^{}[]´`';:.,<>()"
    table = str.maketrans("", "", words)
    char = char.translate(table)
    return "".join(secrets.choice(char) for _ in range(tamanho))


def main():
    parser = argparse.ArgumentParser(description="Gerador de senhas")
    parser.add_argument(
        "-p",
        "--passwd",
        type=int,
        default=8,
        help="Tamanho de caracteres incluindo simbolos, letra maiuscula e minuscula, e numeros voce deseja",
    )

    args = parser.parse_args()
    if args.passwd > 30:
        print("Senha muito grande, favor diminuir tamanho")
    else:
        senha = gerar_senha(args.passwd)
        print(
            f"Senha gerada: {senha}, gostaria de exportar para um arquivo de texto?\n"
        )
        saida = input("Y[es]/N[o]\n")
        if saida != "Y":
            print("Desligando...")
        else:
            print("Imprimindo...")
            with open("senhas.txt", "w") as f:
                sys.stdout = f
                print(senha)


if __name__ == "__main__":
    main()
