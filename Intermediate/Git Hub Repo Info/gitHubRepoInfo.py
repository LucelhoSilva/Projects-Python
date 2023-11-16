import requests


def obter_repositorios_github(nome_usuario):
    url = f'https://api.github.com/users/{nome_usuario}/repos'

    resposta = requests.get(url)

    if resposta.status_code == 200:

        repositorios = resposta.json()

        print(f"\nRepositórios de {nome_usuario}:")
        for repo in repositorios:
            print(repo['name'])

        print(f"Total de repositórios: {len(repositorios)}\n")
    else:

        print(
            f"Erro ao obter repositórios. Código de status: {resposta.status_code}")


nome_usuario = input("\nDigite o nome do usuário do GitHub: ")

obter_repositorios_github(nome_usuario)
