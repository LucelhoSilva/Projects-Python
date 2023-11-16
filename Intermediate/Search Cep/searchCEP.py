import requests


class ViaCepAPI:
    def __init__(self):
        self.base_url = "https://viacep.com.br/ws/"

    def get_address_by_cep(self, cep):
        url = f"{self.base_url}{cep}/json"
        response = requests.get(url)
        data = response.json()
        return data if isinstance(data, dict) and 'erro' not in data else None

    def get_address_by_logradouro(self, uf, cidade, logradouro):
        url = f"{self.base_url}{uf}/{cidade}/{logradouro}/json"
        response = requests.get(url)
        data = response.json()
        return data if isinstance(data, list) else [data]


def main():
    via_cep_api = ViaCepAPI()

    cep_ou_logradouro = input("\nDigite o CEP ou nome do logradouro: ")

    if cep_ou_logradouro.isnumeric():
        # Se o input é um número, assume que é um CEP
        dados = via_cep_api.get_address_by_cep(cep_ou_logradouro)
    else:
        # Se não for um número, assume que é um nome de logradouro
        uf = input("Digite a UF: ")
        cidade = input("Digite a cidade: ")
        dados = via_cep_api.get_address_by_logradouro(
            uf, cidade, cep_ou_logradouro)

    if dados:
        if isinstance(dados, list):
            for item in dados:
                endereco = item.get('logradouro', '')
                bairro = item.get('bairro', '')
                cidade = item.get('localidade', '')
                uf = item.get('uf', '')
                cep = item.get('cep', '')

                resultado_formatado = f"\n{endereco} - {bairro}, {cidade} - {uf}, {cep}\n"
                print(resultado_formatado)
        else:
            endereco = dados.get('logradouro', '')
            bairro = dados.get('bairro', '')
            cidade = dados.get('localidade', '')
            uf = dados.get('uf', '')
            cep = dados.get('cep', '')

            resultado_formatado = f"{endereco} - {bairro}, {cidade} - {uf}, {cep}\n"
            print(resultado_formatado)
    else:
        print("CEP ou logradouro não encontrado.")


if __name__ == "__main__":
    main()
