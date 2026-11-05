from unittest.mock import MagicMock, patch

from conversor import ConversorMoedas


class TestConversorMoedas:
    def setup_method(self):
        # Roda antes de cada teste: cria um conversor novo
        self.conversor = ConversorMoedas()

    def test_converter_reais_em_dolares(self):
        self.conversor.venda = 5.5
        assert round(self.conversor.converter(1200), 2) == 218.18

    def test_converter_zero_reais_da_zero_dolares(self):
        self.conversor.venda = 5.5
        assert self.conversor.converter(0) == 0

    def test_buscar_cotacao_com_api_simulada(self):
        resposta_falsa = MagicMock()
        resposta_falsa.raise_for_status.return_value = None
        resposta_falsa.json.return_value = {
            "USDBRL": {"bid": "5.4908", "ask": "5.4920"}
        }
        with patch("conversor.requests.get", return_value=resposta_falsa):
            assert self.conversor.buscar_cotacao() is True
        assert self.conversor.venda == 5.4920

    def test_buscar_cotacao_quando_a_api_falha(self):
        with patch("conversor.requests.get", side_effect=Exception("sem conexão")):
            assert self.conversor.buscar_cotacao() is False
        assert self.conversor.venda is None