import streamlit as st

st.set_page_config(
    page_title="Relatório – Projeto PSC",
    layout="centered"
)

st.title("Relatório – Projeto de Provimento de Serviços Computacionais")
st.markdown("**Marcela Monteiro Gondim**")
st.markdown("---")

# -------------------------------------------------
st.header("1. Planejamento da arquitetura")

st.subheader("Modelo de serviço adotado")
st.write("PaaS – Platform as a Service.")

st.subheader("Justificativa")
st.write("""
O modelo PaaS foi escolhido porque permite a execução de aplicações em contêiner
sem a necessidade de gerenciamento direto da infraestrutura física ou do sistema
operacional. A equipe fica responsável pela aplicação e pela configuração do
ambiente, enquanto o provedor de nuvem gerencia servidores, rede e escalabilidade.
""")

# -------------------------------------------------
st.header("2. Preparação do ambiente com Docker")

st.write("""
Foi criado um Dockerfile com base em uma imagem oficial do Python.
A configuração de rede foi simulada por meio da exposição da porta da aplicação.
Também foi considerada a utilização de volume persistente para armazenamento
de dados da aplicação.
""")

# -------------------------------------------------
st.header("3. Simulação de deploy")

st.write("""
A aplicação foi empacotada em uma imagem Docker e validada localmente por meio da
execução do contêiner utilizando a porta 5000. Para a simulação de deploy, a imagem
foi publicada em um repositório de imagens em nuvem após autenticação e envio da
imagem (docker push).

O processo de entrega adotado é manual, no qual o responsável realiza a criação
da imagem, o envio ao repositório e a criação do serviço de execução.

Em um cenário real, essa imagem poderia ser utilizada por um serviço de
orquestração de contêineres para disponibilizar a aplicação em um endereço público.
""")

# -------------------------------------------------
st.header("4. Documentação técnica")

st.subheader("Componentes utilizados")

st.markdown("""
- Aplicação web desenvolvida em Python (Flask)
- Contêiner Docker
- Plataforma de nuvem (AWS)
""")

st.subheader("Benefícios do modelo PaaS")

st.markdown("""
- Foco no desenvolvimento da aplicação;
- Redução da complexidade de gerenciamento de infraestrutura;
- Maior agilidade para implantação;
- Escalabilidade facilitada.
""")

st.subheader("Desafios e limitações")

st.markdown("""
- Limitações de configuração do sistema operacional e da rede;
- Custos elevados em larga escala;
- Dependência das ferramentas e versões suportadas pela plataforma;
- Responsabilidade do cliente sobre dados e acessos.
""")

# -------------------------------------------------
st.header("5. Conceitos aplicados")

st.subheader("Escalabilidade")
st.write("""
A aplicação pode ser escalada horizontalmente por meio da criação de múltiplos
contêineres.
""")

st.subheader("Elasticidade")
st.write("""
A plataforma permite aumentar ou reduzir automaticamente a quantidade de
instâncias conforme a demanda.
""")

st.subheader("Responsabilidade compartilhada")
st.write("""
O provedor de nuvem é responsável pela infraestrutura física, rede e serviços
gerenciados, enquanto a equipe é responsável pela aplicação, configuração dos
contêineres e atualização do código.
""")

st.success("Relatório apresentado por meio de aplicação em contêiner com Streamlit.")