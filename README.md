## ETL AIRFLOW com Grafana

PostgreSQL - Configurado e funcionando como banco de dados para armazenar os dados nas camadas Bronze, Silver e Gold.
Airflow - Implementado para orquestrar o pipeline de dados, incluindo ingestão, transformação e agregação.
Grafana - Instalado e configurado, pronto para monitoramento e visualização dos dados.

Objetivo do Desafio
Configurar um pipeline de dados funcional com as seguintes ferramentas:

PostgreSQL para armazenamento de dados nas camadas Bronze, Silver e Gold.
Apache Airflow para orquestração e automação do pipeline.
Grafana para monitoramento e visualização de métricas e dados.

###

Passos Realizados

Instalação e configuração PostgreSQL
Criação de usuários, banco de dados brewery_data e tabelas para as camadas Bronze, Silver e Gold.

Implementação do Airflow

Criação de 3 DAGs:

![image](https://github.com/user-attachments/assets/b83641cb-a78b-489a-88dd-8aca8a42ca6d)
Ingestão de dados CSV na camada Bronze.

Transformação e limpeza de dados para a camada Silver.
![image](https://github.com/user-attachments/assets/298d606e-e1ab-477c-a44d-c3f5de142cf4)

Agregação de dados na camada Gold.
![image](https://github.com/user-attachments/assets/4f0cb91a-0c2e-43a8-af7d-9ab8679faa8c)

Foi criado um arquivo CSV fictício contendo dados de pedidos de cerveja.
beer_sales.csv

Configuração do Grafana

