# 🌦️ ETL de Dados Meteorológicos — Open-Meteo

Projeto de portfólio de **Engenharia de Dados** que implementa um pipeline ETL em Python consumindo uma API meteorológica pública real.

A aplicação consulta a API **Open-Meteo**, transforma os dados retornados e gera arquivos estruturados para análise.

## 🎯 Objetivo

Demonstrar um fluxo completo de ETL:

```text
                    ┌─────────────────┐
                    │  Open-Meteo API │
                    └────────┬────────┘
                             │
                          Extract
                             │
                             ▼
                    ┌─────────────────┐
                    │  data/raw       │
                    │  JSON original  │
                    └────────┬────────┘
                             │
                        Transform
                             │
                             ▼
                    ┌─────────────────┐
                    │ data/processed  │
                    │ CSV tratado     │
                    └────────┬────────┘
                             │
                           Load
                             │
                             ▼
                    ┌─────────────────┐
                    │ analytics.csv   │
                    └─────────────────┘
```

## 🔌 API utilizada

O projeto utiliza a **Open-Meteo API**, uma API pública de previsão meteorológica.

Documentação oficial:

https://open-meteo.com/

Endpoint utilizado:

```text
https://api.open-meteo.com/v1/forecast
```

A consulta usa latitude, longitude e variáveis meteorológicas para obter dados horários.

## 🧰 Tecnologias

- Python 3.10+
- Requests
- Pandas
- API REST
- JSON
- CSV
- ETL
- Logging
- Variáveis de ambiente

## 📁 Estrutura

```text
etl-api-clima/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

## ⚙️ Como executar

### 1. Clone o projeto

```bash
git clone https://github.com/SEU-USUARIO/etl-api-clima.git
cd etl-api-clima
```

### 2. Crie um ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o ambiente

Copie:

```text
.env.example
```

para:

```text
.env
```

Você pode alterar latitude e longitude para qualquer local.

Exemplo:

```env
LATITUDE=-28.2925
LONGITUDE=-53.5027
TIMEZONE=America/Sao_Paulo
```

### 5. Execute o pipeline

```bash
python run.py
```

O pipeline irá:

1. Consumir a API.
2. Salvar a resposta original em `data/raw/`.
3. Transformar os dados.
4. Salvar o resultado em `data/processed/weather.csv`.
5. Exibir um resumo no terminal.

## 📊 Exemplo de saída

```text
==================================================
ETL - DADOS METEOROLÓGICOS
==================================================

[EXTRACT] Consultando Open-Meteo...
[EXTRACT] Dados recebidos com sucesso.
[EXTRACT] Arquivo bruto salvo em data/raw/...

[TRANSFORM] Normalizando dados...
[TRANSFORM] 168 registros preparados.

[LOAD] Salvando CSV...
[LOAD] Arquivo salvo em data/processed/weather.csv

==================================================
Pipeline concluído com sucesso!
==================================================
```

## 🔄 Etapas do ETL

### Extract

O módulo `extract.py` faz uma requisição HTTP para a API e salva o JSON original.

Isso é importante em pipelines reais porque permite:

- auditoria;
- reprocessamento;
- investigação de problemas;
- rastreabilidade da origem.

### Transform

O módulo `transform.py` transforma a estrutura aninhada da API em uma tabela.

Campos principais:

| Campo | Descrição |
|---|---|
| timestamp | Data e hora da medição |
| temperature_c | Temperatura em °C |
| humidity_percent | Umidade relativa |
| precipitation_mm | Precipitação em mm |
| wind_speed_kmh | Velocidade do vento |
| weather_code | Código meteorológico |

Também são realizadas validações simples:

- conversão de tipos;
- tratamento de valores ausentes;
- ordenação temporal;
- remoção de registros duplicados.

### Load

O módulo `load.py` grava os dados tratados em CSV.

O resultado fica em:

```text
data/processed/weather.csv
```

## 📈 Possíveis análises

A saída pode ser utilizada posteriormente para:

- dashboard de clima;
- análise de temperatura;
- análise de precipitação;
- comparação entre cidades;
- previsão de demanda;
- estudos de séries temporais.

## 🚀 Próximas evoluções

Este projeto foi pensado para ser expandido.

Possíveis melhorias:

- Docker;
- PostgreSQL;
- Airflow;
- Apache Spark;
- armazenamento em S3;
- particionamento por data;
- testes automatizados;
- CI/CD com GitHub Actions;
- dashboard com Power BI ou Streamlit.

## 👨‍💻 Objetivo de portfólio

Este projeto demonstra conhecimentos de:

```text
API REST
   ↓
Python
   ↓
ETL
   ↓
Data Quality
   ↓
Data Transformation
   ↓
Data Storage
   ↓
Analytics
```

---

## 📄 Licença

MIT
