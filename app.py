import streamlit as st
import pandas as pd
import os

# Configuração da página
st.set_page_config(
    page_title="Kite for Life - Desempenho",
    page_icon="📊",
    layout="centered"
)

def load_data(file_path):
    if os.path.exists(file_path):
        # Lê o CSV. Como o seu arquivo tem muitas linhas vazias iniciais,
        # vamos carregar tudo e depois limpar.
        df = pd.read_csv(file_path, header=None)
        return df
    return None

def main():
    st.title("🌊 Projeto: KITE FOR LIFE")
    st.subheader("Sistema de Gestão de Desempenho")

    file_path = 'deswmpenho.csv'
    
    if os.path.exists(file_path):
        df = load_data(file_path)
        
        # Interface Principal
        st.info("Planilha `deswmpenho.csv` carregada com sucesso.")

        # Tenta localizar o nome do projeto no CSV (baseado na estrutura enviada)
        # De acordo com seu arquivo, o nome está após várias linhas vazias
        st.markdown("---")
        
        tabs = st.tabs(["📋 Visualizar Dados", "📈 Gráficos", "➕ Novo Registro"])
        
        with tabs[0]:
            st.write("### Conteúdo da Planilha")
            # Mostra o DataFrame limpando linhas e colunas totalmente vazias
            clean_df = df.dropna(how='all').dropna(axis=1, how='all')
            st.dataframe(clean_df, use_container_width=True)

        with tabs[1]:
            st.write("### Análise de Desempenho")
            st.warning("Adicione dados numéricos à planilha para visualizar gráficos.")
            # Exemplo de gráfico caso houvesse dados
            # st.line_chart(clean_df[column_with_numbers])

        with tabs[2]:
            st.write("### Adicionar Novo Indicador")
            with st.form("form_registro"):
                data = st.date_input("Data da Atividade")
                descricao = st.text_input("Descrição da Atividade/Métrica")
                valor = st.number_input("Valor Alcançado", min_value=0.0)
                
                enviar = st.form_submit_button("Salvar na Planilha")
                if enviar:
                    st.success(f"Registro '{descricao}' preparado para salvamento!")
                    st.caption("Nota: Para salvar fisicamente no CSV, é necessário implementar a função de escrita.")

    else:
        st.error(f"Arquivo `{file_path}` não encontrado!")
        st.markdown(f"Certifique-se de que o arquivo `{file_path}` está na mesma pasta que este script.")

if __name__ == "__main__":
    main()