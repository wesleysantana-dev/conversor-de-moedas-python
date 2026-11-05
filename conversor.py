import requests


class ConversorMoedas:
    URL = "https://economia.awesomeapi.com.br/last/USD-BRL"

    def __init__(self):
        self.venda = None

    def buscar_cotacao(self):
        try:
            response = requests.get(self.URL)
            response.raise_for_status()
            cotacao = response.json()["USDBRL"]
            self.venda = float(cotacao["ask"])
            return True
        except Exception as e:
            print(f"Erro ao buscar cotação na API: {e}")
            return False

    def converter(self, valor_reais):
        return valor_reais / self.venda


def main():
    print("--- CONVERSOR DE MOEDAS ---")
    conversor = ConversorMoedas()

    if not conversor.buscar_cotacao():
        print("Sistema offline. Tente novamente mais tarde.")
        return

    print(f"Dólar hoje (venda): R$ {conversor.venda:.2f}\n")

    try:
        valor_reais = float(input("Digite o valor em R$ para converter: "))
        if valor_reais < 0:
            print("Valor inválido.")
            return
        dolares = conversor.converter(valor_reais)
        print(f"Com R$ {valor_reais:.2f} você compra US$ {dolares:.2f}")
    except ValueError:
        print("Erro: digite apenas números (ex: 50 ou 50.50).")


if __name__ == "__main__":
    main()
