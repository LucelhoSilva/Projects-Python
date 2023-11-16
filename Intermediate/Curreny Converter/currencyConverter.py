import requests


def obter_dados_moedas():
    url = "https://api.hgbrasil.com/finance"
    parametros = {"format": "json"}

    resposta = requests.get(url, params=parametros)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        print(f"Erro ao obter dados da API. Código de status: {resposta.status_code}")
        return None


def converter_moeda(valor_em_reais, taxa_conversao):
    return valor_em_reais * taxa_conversao


def main():
    dados_moedas = obter_dados_moedas()

    if dados_moedas:
        valor_em_reais = float(input("Digite o valor em reais (R$): "))
        print("-------------------------------------------------------")
        print(f"Valor informado em Reais (R$): {valor_em_reais:.2f}")
        print("-------------------------------------------------------\n")

        taxa_euro = dados_moedas["results"]["currencies"]["EUR"]["buy"]
        valor_em_euro = converter_moeda(valor_em_reais, taxa_euro)
        print(f"Valor em Euro (EUR): {valor_em_euro:.2f}")

        taxa_dolar = dados_moedas["results"]["currencies"]["USD"]["buy"]
        valor_em_dolar = converter_moeda(valor_em_reais, taxa_dolar)
        print(f"Valor em Dólares (USD): {valor_em_dolar:.2f}")

        taxa_pesoargentino = dados_moedas["results"]["currencies"]["ARS"]["buy"]
        valor_em_pesoargentino = converter_moeda(
            valor_em_reais, taxa_pesoargentino)
        print(f"Valor em Pesos Argentinos (ARS): {valor_em_pesoargentino:.2f}")

        tava_libraesterlina = dados_moedas["results"]["currencies"]["GBP"]["buy"]
        valor_em_libraesterlina = converter_moeda(
            valor_em_reais, tava_libraesterlina)
        print(f"Valor em Libras Esterlinas (GBP): {valor_em_libraesterlina:.2f}")


if __name__ == "__main__":
    main()
