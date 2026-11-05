import requests

def get_dolar_hoje():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        cotacao = response.json()["USDBRL"]
        return float(cotacao["bid"]), float(cotacao["ask"])
    except Exception as e:
        print(f"Erro ao buscar cotação na API: {e}")
        return None

def converter(valor_reais, cotacao):
    return valor_reais / cotacao

def main():
    print("--- CONVERSOR DE MOEDAS ---")
    resultado = get_dolar_hoje()
    if resultado is None:
        print("Sistema offline. Tente novamente mais tarde.")
        return

    compra, venda = resultado
    print(f"Dólar hoje: compra R$ {compra:.2f} | venda R$ {venda:.2f}\n")

    try:
        valor_reais = float(input("Digite o valor em R$ para converter: "))
        if valor_reais < 0:
            print("Valor inválido.")
            return
        dolares = converter(valor_reais, venda)
        print(f"Com R$ {valor_reais:.2f} você compra US$ {dolares:.2f}")
    except ValueError:
        print("Erro: digite apenas números (ex: 50 ou 50.50).")

if __name__ == "__main__":
    main()
