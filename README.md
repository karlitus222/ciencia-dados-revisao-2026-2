# Ciência de Dados — Atividade 05: Revisão

**Carlos Gabriel Raposo Landim · Engenharia de Software · 2026/2**

Cinco exercícios de limpeza e preparação de dados na etapa de Preparação dos Dados do CRISP-DM. Os notebooks estão executados, com código, tabelas, gráficos, decisões justificadas, respostas de reflexão e desafios.

| Exercício | Notebook | Tema |
|---|---|---|
| 1 | [Melbourne](01_melbourne.ipynb) | Ausências, remoção, mediana/moda e KNNImputer |
| 2 | [KPMG](02_kpmg.ipynb) | Duplicatas, chaves, indicadores e RapidFuzz |
| 3 | [Adult](03_adult.ipynb) | Padronização, marcadores desconhecidos e escalonamento |
| 4 | [Diamonds](04_diamonds.ipynb) | Outliers, Z-score, IQR, remoção, capping e log |
| 5 | [SHEIN](05_shein.ipynb) | Pipeline reutilizável para duas categorias de produtos |

O GitHub exibe os notebooks com as saídas. As versões HTML também podem ser baixadas e abertas no navegador. Os CSVs de comparação e a base SHEIN tratada ficam em [resultados](resultados/).

## Reproduzir

Use Python 3.12. No diretório deste repositório:

```bash
python -m pip install -r requirements.txt
python baixar_dados.py
python -m pip install jupyterlab
python -m jupyter lab
```

Abra os notebooks e execute as células em ordem, mantendo a raiz do repositório como diretório de trabalho. O script baixa as bases de suas fontes públicas para `dados/`; os arquivos originais não são versionados aqui. Se o Kaggle exigir autenticação ou mudar o download, faça o download manual no link correspondente e extraia para a mesma pasta.

| Pasta | Fonte e arquivo esperado |
|---|---|
| `dados/melbourne/` | [Melbourne Housing Snapshot](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot), `melb_data.csv` |
| `dados/kpmg/` | [Customer Transaction Dataset](https://www.kaggle.com/datasets/archit9406/customer-transaction-dataset), `KPMG_VI_New_raw_data_update_final.xlsx` |
| `dados/adult/` | [Adult — UCI](https://archive.ics.uci.edu/dataset/2/adult), `adult.data` e `adult.names` |
| `dados/diamonds/` | [seaborn-data](https://github.com/mwaskom/seaborn-data), `diamonds.csv` |
| `dados/shein/` | [Dirty E-Commerce Data — SHEIN](https://www.kaggle.com/datasets/oleksiimartusiuk/e-commerce-data-shein), `us-shein-electronics-4395.csv` e `us-shein-appliances-3987.csv` |

## Resultados principais

- Melbourne: 13.580 imóveis; casos completos reduzem a base a 6.196 linhas. BuildingArea tem 47,50% de ausências. KNN e imputação estatística são comparados, incluindo limitações e custo medido.
- KPMG: 20.000 transações e nenhuma duplicata exata na versão utilizada. A análise preserva os registros e explica por que semelhança textual não basta para fundir marcas.
- Adult: marcadores textuais revelam 1.836 ausências em workclass, 1.843 em occupation e 583 em native-country. O IQR nulo de capital-gain limita o escalonamento robusto.
- Diamonds: 20 registros têm dimensões não positivas. As estratégias de tratamento são comparadas sem presumir que preço elevado seja erro.
- SHEIN: 8.380 anúncios passam a 8.137 após retirar 243 cópias completas. A união das colunas complementares recupera todos os títulos. Desconto não informado permanece desconhecido.

As análises são descritivas e se referem às versões obtidas das bases. Em uma avaliação preditiva, imputadores e escalonadores devem ser ajustados somente nos dados de treino. As bases mantêm as condições de uso definidas por seus respectivos distribuidores.
