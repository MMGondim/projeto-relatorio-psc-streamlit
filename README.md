# Projeto – Relatório PSC (Streamlit)

Este repositório contém a aplicação em Python desenvolvida com Streamlit para apresentação do relatório do projeto da disciplina Provimento de Serviços Computacionais.

A aplicação foi empacotada em uma imagem Docker e publicada no serviço de registro de imagens da AWS (Amazon ECR).

---

## Pré-requisitos

- Docker instalado

---

## Como executar a aplicação do relatório

1. Baixar a imagem a partir do repositório da AWS:

docker pull 869919305101.dkr.ecr.us-east-1.amazonaws.com/projeto-python:relatorio

2. Executar o contêiner:

docker run -p 8501:8501 869919305101.dkr.ecr.us-east-1.amazonaws.com/projeto-python:relatorio

3. Acessar no navegador:

http://localhost:8501

---

## Observação

Esta aplicação é utilizada exclusivamente para apresentação do relatório técnico do projeto.
