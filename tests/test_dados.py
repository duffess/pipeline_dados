import unittest
from scripts.processamento_dados import Dados

class TestDados(unittest.TestCase):

    def setUp(self):
        self.lista_mock = [
            {"Produto": "Camiseta", "Preço": "39.90"},
            {"Produto": "Tênis", "Preço": "129.90"}
        ]
        self.dados = Dados(self.lista_mock, 'list')

    def test_size_data(self):
        self.assertEqual(self.dados.qtd_linhas, 2)

    def test_get_columns(self):
        self.assertIn("Produto", self.dados.nome_colunas)

    def test_transforma_dados_tabela(self):
        tabela = self.dados._transformando_dados_tabela()
        self.assertEqual(len(tabela), 3)  # 1 header + 2 linhas de dados
        self.assertEqual(tabela[0], self.dados.nome_colunas)

if __name__ == "__main__":
    unittest.main()
