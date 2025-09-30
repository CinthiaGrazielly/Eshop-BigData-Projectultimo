# Projeto: Aplicação Prática de Tecnologias de Banco de Dados e Big Data na E-Shop Brasil

## 1. Introdução
A **E-Shop Brasil**, um dos maiores e-commerces do país, enfrenta desafios em **gestão de dados**, **personalização da experiência do cliente** e **otimização logística**.  
Este projeto propõe o uso de **SQL, NoSQL (MongoDB)** e **Big Data** para superar esses desafios.

## 2. Objetivos
- Garantir **segurança e privacidade** de dados (LGPD).
- Personalizar recomendações e navegação.
- Otimizar **estoques e logística**.
- Escalar a solução a longo prazo.

## 3. Arquitetura da Solução
- **Docker** para isolar o ambiente.
- **MongoDB** como banco NoSQL para dados semiestruturados.
- **Streamlit** para interface web.
- **Big Data (conceitual)**: Spark/Hadoop no futuro.

## 4. Funcionalidades
- Inserção de dados no MongoDB.
- Edição e exclusão de registros.
- Consulta e visualização em tabela/gráficos.
- Concatenar dados de diferentes coleções.
- Exemplo de recomendações simuladas.

## 5. Passos de Execução
1. Clonar o repositório:
   ```bash
   git clone https://github.com/seu-usuario/Eshop-BigData-Project.git
   cd Eshop-BigData-Project
   ```

2. Subir MongoDB com Docker:
   ```bash
   docker-compose up -d
   ```

3. Instalar dependências e executar aplicação:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

4. Acessar em [http://localhost:8501](http://localhost:8501)

## 6. Estrutura do Repositório
```
├── README.md
├── docker-compose.yml
├── requirements.txt
├── app.py
├── data/
└── exemplos/
```

## 7. Próximos Passos
- Integração com Data Lake.
- Machine Learning para recomendações.
- Integração omnichannel com ERP.

## 8. Conclusão
Demonstração prática do uso de **NoSQL, Big Data e Docker** para otimizar operações da E-Shop Brasil.
