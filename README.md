# transformado-parquet

Um script Python robusto e eficiente para consolidar múltiplos arquivos Excel (`.xlsx`) em um único arquivo Parquet otimizado.

Este projeto foi desenvolvido para automatizar e acelerar o processo de transformação de dados, convertendo um formato comum, porém pesado (Excel), para um formato de colunar de alta performance (Parquet), ideal para análise de dados e processamento em grandes volumes.

## 🚀 Recursos

- **Consolidação Automática**: Lê e combina automaticamente todos os arquivos `.xlsx` de um diretório de entrada.
- **Alta Performance**: Gera um arquivo único no formato **Parquet**, que é altamente comprimido e otimizado para consultas.
- **Tratamento de Dados**: Lida com diferentes estruturas de planilhas e normaliza os dados durante a consolidação.
- **Flexível**: Permite configurar o diretório de entrada, o nome do arquivo de saída e outras opções de processamento.

## 📋 Pré-requisitos

Para executar este script, você precisará ter o Python 3.7 ou superior instalado. As seguintes bibliotecas também são necessárias:

- `pandas`
- `pyarrow`
- `openpyxl`

## ⚙️ Instalação

1.  Clone este repositório:

    ```bash
    git clone https://github.com/SEU_USUARIO/transformado-parquet.git
    cd transformado-parquet
    ```

2.  Crie e ative um ambiente virtual (opcional):

    ```bash
    python -m venv venv
    source venv/bin/activate # No Windows use: venv\Scripts\activate
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

    Se você não tiver um arquivo `requirements.txt`, pode instalar as bibliotecas manualmente:

    ```bash
    pip install pandas pyarrow openpyxl
    ```

## 📖 Como Usar

### 1. Preparar os Arquivos de Entrada

Coloque todos os arquivos `.xlsx` que você deseja consolidar em um único diretório.

### 2. Configurar o Script

Abra o arquivo `transformado_parquet.py` e ajuste as configurações no início do script, se necessário:

- `input_directory`: O caminho para a pasta contendo os arquivos Excel.
- `output_file`: O nome do arquivo Parquet de saída (padrão: `dados_consolidados.parquet`).

```python
# Exemplo de configuração
input_directory = './data/input/'
output_file = 'dados_finais.parquet'
