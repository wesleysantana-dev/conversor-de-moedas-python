import requests

def get_dolar_hoje():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data['USDBRL']['bid'])
        
    except Exception as e:
        print(f"Erro ao buscar cotação na API: {e}")
        return None

def main():
    print("--- CONVERSOR DE MOEDAS ---")
    
    dolar = get_dolar_hoje()
    
    if not dolar:
        print("Sistema offline. Tente novamente mais tarde.")
        return

    print(f"Cotação atual: US$ 1.00 = R$ {dolar:.2f}\n")
    
    try:
        valor_reais = float(input("Digite o valor em R$ para converter: "))
        
        if valor_reais < 0:
            print("Valor inválido.")
            return
            
        conversao = valor_reais / dolar
        print(f"\nCom R$ {valor_reais:.2f} você compra US$ {conversao:.2f}")
        
    except ValueError:
        print("Erro: Digite apenas números válidos (ex: 50 ou 50.50).")

if __name__ == "__main__":
    main()
