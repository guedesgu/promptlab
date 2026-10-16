
import streamlit as st
from google import genai

st.set_page_config(
    page_title="PromptLab",
    page_icon="🧪",
    layout="centered",
)

st.title("🧪 PromptLab")
st.subheader("Laboratório de Engenharia de Prompts")

st.write(
    "Teste instruções, analise respostas e experimente "
    "diferentes formas de trabalhar com IA generativa."
)

# Configuração do cliente Gemini
try:
    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )
except Exception:
    st.error(
        "Não foi possível configurar a API. "
        "Confira o arquivo .streamlit/secrets.toml."
    )
    st.stop()

texto = st.text_area(
    "Texto de entrada",
    placeholder="Cole aqui o texto que deseja analisar...",
    height=180,
)

prompt = st.text_area(
    "Instrução para a IA",
    value="Resuma o texto em cinco tópicos, "
          "preservando as informações mais importantes.",
    height=120,
)

if st.button("Executar prompt", type="primary"):
    if not texto.strip() or not prompt.strip():
        st.warning("Preencha o texto e a instrução.")
    else:
        with st.spinner("A IA está processando sua solicitação..."):
            try:
                resposta = client.models.generate_content(
                    model="gemini-3.1-flash-lite",
                    contents=(
                        f"Instrução:\n{prompt}\n\n"
                        f"Texto de entrada:\n{texto}"
                    ),
                )

                if resposta.text:
                    st.subheader("Resposta gerada")
                    st.markdown(resposta.text)
                else:
                    st.warning(
                        "O modelo não retornou texto. "
                        "Tente reformular sua solicitação."
                    )

            except Exception:
                st.error(
                    "Não foi possível gerar a resposta. "
                    "Verifique sua conexão, a chave da API, "
                    "o acesso ao modelo e os limites de uso."
                )
