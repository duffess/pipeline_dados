import json
import csv

class Dados:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self._leitura_dados()
        self.nome_colunas = self._get_columns()
        self.qtd_linhas = self._size_data()

    def _leitura_json(self):
        with open(self.path, 'r') as file:
            return json.load(file)

    def _leitura_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def _leitura_dados(self):
        if self.tipo_dados == 'csv':
            return self._leitura_csv()
        elif self.tipo_dados == 'json':
            return self._leitura_json()
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memória'
            return dados
        else:
            raise ValueError(f"Tipo de dados não suportado: {self.tipo_dados}")

    def _get_columns(self):
        return list(self.dados[-1].keys())

    def _size_data(self):
        return len(self.dados)

    def rename_columns(self, key_mapping):
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)

        self.dados = new_dados
        self.nome_colunas = self._get_columns()

    @staticmethod
    def join(dadosA, dadosB):
        combined_list = dadosA.dados + dadosB.dados
        return Dados(combined_list, 'list')

    def _transformando_dados_tabela(self):
        tabela = [self.nome_colunas]
        for row in self.dados:
            linha = [row.get(coluna, 'Indisponível') for coluna in self.nome_colunas]
            tabela.append(linha)
        return tabela

    def salvando_dados(self, path):
        dados_tabela = self._transformando_dados_tabela()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_tabela)
