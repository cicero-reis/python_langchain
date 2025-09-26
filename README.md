# FastAPI + LangChain – User Performance Microservice

## Descrição

Microservice em **Python** desenvolvido com **FastAPI** e **LangChain** para análise de desempenho do usuário em tempo real.
O serviço é consumido diretamente pelo **frontend Vue SPA** para fornecer insights e relatórios de performance, sem intervenção do backend Laravel.

---

## Tecnologias

* **Python 3.11+**
* **FastAPI** – framework para API REST
* **LangChain** – processamento e análise de dados do usuário
* **Uvicorn** – servidor ASGI de alta performance
* **Pydantic** – validação de dados

---

## Funcionalidades

* Recebe dados de usuários e tasks do frontend
* Processa informações via LangChain para gerar insights de desempenho
* Retorna resultados em JSON para consumo direto pela SPA

---

## Endpoints Principais

* `POST /feedback` – Recebe dados do usuário e tasks, retorna análise de desempenho
* Retorno esperado: JSON com insights, pontuação de performance e recomendações

---

## Integração com Vue SPA

* O **frontend Vue.js** envia requisições diretamente ao microservice:

  1. Usuário realiza ações na SPA
  2. SPA envia dados via Axios para `/feedback`
  3. Microservice processa com LangChain
  4. SPA recebe insights e exibe em tempo real

> Observação: Laravel **não conhece nem controla** essas requisições.

