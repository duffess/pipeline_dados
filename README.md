
# Pipeline de Dados - Projeto ETL

## Descrição

Este projeto consiste em um pipeline de dados para extração, transformação e carregamento (ETL) de informações de duas fontes diferentes (JSON e CSV). O objetivo é combinar e padronizar os dados para posterior análise ou uso.

O pipeline foi desenvolvido em Python, utilizando manipulação de arquivos JSON e CSV, e organização orientada a objetos para facilitar manutenção e extensibilidade.

## Tecnologias

- Python 3.10.12
- CSV / JSON
- Orientação a Objetos
- Jupyter Notebook
- Ambiente virtual

## Estrutura do Projeto

```
├── data_raw/                  # Dados originais (JSON e CSV)
├── data_processed/            # Dados processados e combinados
├── notebooks/                 # Notebooks de exploração e testes
├── scripts/                   # Scripts Python principais (ETL)
│   ├── processamento_dados.py
│   └── fusao_mercados_agosto.py
├── tests/                     # Testes unitários
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação do projeto
```

## Como Rodar

1. Crie e ative um ambiente virtual:

### Linux / WSL / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o script principal:

```bash
python scripts/fusao_mercados_agosto.py
```

---

## Como Contribuir

Contribuições são bem-vindas! Abra issues ou envie pull requests para melhorias.

---

## Autor

Guilherme Duffes

---

## Licença

MIT License
