import streamlit as st
from pymongo import MongoClient
import pandas as pd
import json

# Conexão com MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["eshop_db"]

st.title("E-Shop Brasil – Gestão de Dados com MongoDB")

menu = st.sidebar.selectbox("Menu", ["Inserir Dados", "Visualizar Dados", "Manipular Dados"])

if menu == "Inserir Dados":
    st.header("Inserir Registro")
    collection = st.selectbox("Coleção", ["clientes", "produtos", "pedidos"])
    data = st.text_area("Insira os dados em formato JSON")
    
    if st.button("Salvar"):
        try:
            record = json.loads(data)
            db[collection].insert_one(record)
            st.success("Registro inserido com sucesso!")
        except Exception as e:
            st.error(f"Erro: {e}")

elif menu == "Visualizar Dados":
    st.header("Visualizar Registros")
    collection = st.selectbox("Coleção", ["clientes", "produtos", "pedidos"])
    docs = list(db[collection].find({}, {"_id": 0}))
    if docs:
        df = pd.DataFrame(docs)
        st.dataframe(df)
    else:
        st.info("Nenhum dado encontrado.")

else:
    st.header("Manipular Dados")
    collection = st.selectbox("Coleção", ["clientes", "produtos", "pedidos"])
    filtro = st.text_input("Filtro (campo=valor)")
    novo_valor = st.text_input("Novo valor (campo=valor)")

    if st.button("Atualizar"):
        try:
            campo_f, valor_f = filtro.split("=")
            campo_n, valor_n = novo_valor.split("=")
            db[collection].update_one({campo_f.strip(): valor_f.strip()},
                                      {"$set": {campo_n.strip(): valor_n.strip()}})
            st.success("Registro atualizado com sucesso!")
        except Exception as e:
            st.error(f"Erro: {e}")

    if st.button("Excluir"):
        try:
            campo_f, valor_f = filtro.split("=")
            db[collection].delete_one({campo_f.strip(): valor_f.strip()})
            st.success("Registro excluído com sucesso!")
        except Exception as e:
            st.error(f"Erro: {e}")
