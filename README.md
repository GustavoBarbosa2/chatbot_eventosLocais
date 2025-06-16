# Chatbot de Eventos de Viana do Castelo (2025)

Este é um chatbot simples que responde a perguntas sobre eventos culturais na região do Alto Minho, com base num conjunto de eventos fornecido manualmente.

##  Funcionalidades

- Faz perguntas sobre datas, locais ou detalhes de eventos
- Usa uma LLM gratuita via API do [Together.ai](https://www.together.ai/)
- Usa um ficheiro JSON com os eventos como contexto
- Interface web simples feita com [Gradio](https://gradio.app/)

## Como usar

1. **Pré-requisitos:**
   - Python 3.8+
   - Instalar as dependências:
     ```bash
     pip install openai gradio
     ```

2. **Inserir a tua API key do Together.ai**
   - Cria um ficheiro `.env` ou define a variável diretamente:
     ```python
     import os
     os.environ["TOGETHER_API_KEY"] = ""
     ```

3. **Executar o chatbot**
   ```bash
   python chatbot.py
