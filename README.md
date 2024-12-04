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

Ingestão de dados CSV na camada Bronze.
![image](https://github.com/user-attachments/assets/b83641cb-a78b-489a-88dd-8aca8a42ca6d)

Transformação e limpeza de dados para a camada Silver.
![image](https://github.com/user-attachments/assets/298d606e-e1ab-477c-a44d-c3f5de142cf4)

Agregação de dados na camada Gold.
![image](https://github.com/user-attachments/assets/4f0cb91a-0c2e-43a8-af7d-9ab8679faa8c)

Foi criado um arquivo CSV fictício contendo dados de pedidos de cerveja.
beer_sales.csv

Camada Medalhão 

Pipeline Completo: Dados fluem desde a ingestão (Bronze) até a agregação e visualização (Gold).
Monitoramento: Dashboard funcional no Grafana, exibindo insights agregados sobre vendas de cerveja.
Ambiente Otimizado: Configurado com recursos limitados e pronto para escalabilidade.

Camada Gold
![image](https://github.com/user-attachments/assets/46f587b5-f4ff-4d23-bd31-2ea7274d7488)

camada Silver
![image](https://github.com/user-attachments/assets/8f1a78e7-f922-4ee1-9475-029dcd306a6a)

Camada Bronze
![image](https://github.com/user-attachments/assets/5225fa6a-044e-4914-948c-0677b411b587)

Grafana
![image](https://github.com/user-attachments/assets/4b7647b4-ca5d-4d76-ac6b-cf0a64d9621f)

Conclusão: O desafio foi superado com sucesso, demonstrando a viabilidade de configurar um pipeline completo para um ambiente de produção.

Print do esquema de dados 

Camada Gold
![image](https://github.com/user-attachments/assets/eba4590e-a56b-4b57-a1b2-0b1d709dbacd)

Camada Silver
![image](https://github.com/user-attachments/assets/96606dfd-2186-4c6b-b496-201ef6319c14)







