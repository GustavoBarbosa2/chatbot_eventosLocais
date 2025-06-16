import gradio as gr
import requests
import json

API_KEY = "ddccea68c8137669c9f742af262715ff4f2657a4ef790948496c1bbcaac7fe08"

contexto = """
[
    {
      "titulo": "Ponte de Lima em Forma 2025",
      "data_hora": "2025-06-15T09:30:00+01:00",
      "hora": "10:30",
      "local": "Parque Do Arnado",
      "link": "https://www.viralagenda.com/pt/events/1644733/ponte-de-lima-em-forma-2025"
    },
    {
      "titulo": "Há Música Popular na Freguesia... de Cabaços",
      "data_hora": "2025-06-15T14:30:00+01:00",
      "hora": "15:30",
      "local": "Cabaços (Ponte de Lima)",
      "link": "https://www.viralagenda.com/pt/events/1641685/ha-musica-popular-na-freguesia-de-cabacos"
    },
    {
      "titulo": "Eu Sou Digital",
      "data_hora": "2025-06-17T13:00:00+01:00",
      "hora": "14:00",
      "local": "Biblioteca Municipal de Cerveira",
      "link": "https://www.viralagenda.com/pt/events/1628822/eu-sou-digital"
    },
    {
      "titulo": "Comunidade de Leitores - Chá com Letras",
      "data_hora": "2025-06-18",
      "hora": null,
      "local": "Biblioteca Municipal de Cerveira",
      "link": "https://www.viralagenda.com/pt/events/1629182/comunidade-de-leitores-cha-com-letras"
    },
    {
      "titulo": "Vaca das Cordas 2025",
      "data_hora": "2025-06-18T17:00:00+01:00",
      "hora": "18:00",
      "local": "Ponte de Lima (Cidade)",
      "link": "https://www.viralagenda.com/pt/events/1641686/vaca-das-cordas-2025"
    },
    {
      "titulo": "Tapetes Floridos",
      "data_hora": "2025-06-19",
      "hora": "00:00",
      "local": "Ponte de Lima (Cidade)",
      "link": "https://www.viralagenda.com/pt/events/1641687/tapetes-floridos"
    },
    {
      "titulo": "Corpo de Deus - Coca de Monção 2025",
      "data_hora": "2025-06-19T07:00:00+01:00",
      "hora": "08:00",
      "local": "Monção (vila)",
      "link": "https://www.viralagenda.com/pt/events/1633149/corpo-de-deus-coca-de-moncao-2025"
    },
    {
      "titulo": "Viana do Castelo recebe megaexposição de LEGO®",
      "data_hora": "2025-06-19T09:00:00+01:00",
      "hora": "10:00",
      "local": "Centro Cultural De Viana Do Castelo",
      "link": "https://www.viralagenda.com/pt/events/1643658/viana-do-castelo-recebe-megaexposicao-de-lego"
    },
    {
      "titulo": "Hora do Conto",
      "data_hora": "2025-06-21T10:00:00+01:00",
      "hora": "11:00",
      "local": "Biblioteca Municipal de Cerveira",
      "link": "https://www.viralagenda.com/pt/events/1631018/hora-do-conto"
    },
    {
      "titulo": "Filme: Missão Impossível – O Ajuste de Contas Final/ M12",
      "data_hora": "2025-06-21T14:00:00+01:00",
      "hora": "15:00",
      "local": "Centro Cultural de Paredes de Coura",
      "link": "https://www.viralagenda.com/pt/events/1643690/filme-missao-impossivel-o-ajuste-de-contas-final-m12"
    },
    {
      "titulo": "Marchas de S. João 2025",
      "data_hora": "2025-06-21T20:00:00+01:00",
      "hora": "21:00",
      "local": "Ponte de Lima (Cidade)",
      "link": "https://www.viralagenda.com/pt/events/1641688/marchas-de-s-joao-2025"
    },
    {
      "titulo": "Festas Sebastianas",
      "data_hora": "2025-06-21T20:00:00+01:00",
      "hora": "21:00",
      "local": "SIRA – Sociedade de Instrução e Recreio Ancorense",
      "link": "https://www.viralagenda.com/pt/events/1643349/festas-sebastianas"
    },
    {
      "titulo": "Eu Sou Digital",
      "data_hora": "2025-06-24T13:00:00+01:00",
      "hora": "14:00",
      "local": "Biblioteca Municipal de Cerveira",
      "link": "https://www.viralagenda.com/pt/events/1632259/eu-sou-digital"
    },
    {
      "titulo": "Comunidade de Leitores - Chá com Letras",
      "data_hora": "2025-06-25",
      "hora": null,
      "local": "Biblioteca Municipal de Cerveira",
      "link": "https://www.viralagenda.com/pt/events/1633279/comunidade-de-leitores-cha-com-letras"
    },
    {
      "titulo": "XXI Dancerveira",
      "data_hora": "2025-06-25",
      "hora": null,
      "local": "Vila Nova de Cerveira (vila)",
      "link": "https://www.viralagenda.com/pt/events/1633280/xxi-dancerveira"
    },
    {
      "titulo": "FITAVALE - Festival Itinerante de Teatro de Amadores do Vale do Minho",
      "data_hora": "2025-06-25T20:30:00+01:00",
      "hora": "21:30",
      "local": "Palco das Artes (Cerveira)",
      "link": "https://www.viralagenda.com/pt/events/1633281/fitavale-festival-itinerante-de-teatro-de-amadores-do-vale-do-minho"
    },
    {
      "titulo": "RAÍZES DE ÁFRICA",
      "data_hora": "2025-06-27T16:00:00+01:00",
      "hora": "17:00",
      "local": "Carreço (Viana Do Castelo)",
      "link": "https://www.viralagenda.com/pt/events/1587585/raizes-de-africa"
    },
    {
      "titulo": "Festival Raízes de África",
      "data_hora": "2025-06-27T18:00:00+01:00",
      "hora": "19:00",
      "local": "Carreço (Viana Do Castelo)",
      "link": "https://www.viralagenda.com/pt/events/1625606/festival-raizes-de-africa"
    },
    {
      "titulo": "Art'In Lima - Mostra Internacional de Arte Contemporânea",
      "data_hora": "2025-06-28",
      "hora": "00:00",
      "local": "Ponte de Lima (Cidade)",
      "link": "https://www.viralagenda.com/pt/events/1641689/art-in-lima-mostra-internacional-de-arte-contemporanea"
    },
    {
      "titulo": "Hora do Conto",
      "data_hora": "2025-06-28T10:00:00+01:00",
      "hora": "11:00",
      "local": "Biblioteca Municipal de Cerveira",
      "link": "https://www.viralagenda.com/pt/events/1635601/hora-do-conto"
    },
    {
      "titulo": "Passeio Sénior 2025",
      "data_hora": "2025-06-30",
      "hora": null,
      "local": "Vila Praia De Âncora",
      "link": "https://www.viralagenda.com/pt/events/1641793/passeio-senior-2025"
    },
    {
      "titulo": "XVII Feira do Cavalo",
      "data_hora": "2025-07-02T23:01:00+01:00",
      "hora": "00:01",
      "local": "Expolima",
      "link": "https://www.viralagenda.com/pt/events/1641690/xvii-feira-do-cavalo"
    },
    {
      "titulo": "3rd Gastronomy Symposium of Alto Minho",
      "data_hora": "2025-07-02T23:01:00+01:00",
      "hora": "00:01",
      "local": "Palacete Villa Moraes",
      "link": "https://www.viralagenda.com/pt/events/1641691/3rd-gastronomy-symposium-of-alto-minho"
    },
    {
      "titulo": "Feira do Alvarinho de Monção 2025",
      "data_hora": "2025-07-03T17:00:00+01:00",
      "hora": "18:00",
      "local": "Parque das Termas de Monção",
      "link": "https://www.viralagenda.com/pt/events/1630895/feira-do-alvarinho-de-moncao-2025"
    },
    {
      "titulo": "Ruta Sonora",
      "data_hora": "2025-07-04",
      "hora": null,
      "local": "Caminha (vila)",
      "link": "https://www.viralagenda.com/pt/events/1643350/ruta-sonora"
    },
    {
      "titulo": "Artbeerfest Caminha",
      "data_hora": "2025-07-10",
      "hora": null,
      "local": "Caminha (vila)",
      "link": "https://www.viralagenda.com/pt/events/1592315/artbeerfest-caminha"
    },
    {
      "titulo": "FESTIVAL CONTRASTA",
      "data_hora": "2025-07-11T20:00:00+01:00",
      "hora": "21:00",
      "local": "Fortaleza De Valença",
      "link": "https://www.viralagenda.com/pt/events/1633118/festival-contrasta"
    },
    {
      "titulo": "Há Música Popular na Freguesia... Sandiães",
      "data_hora": "2025-07-20T14:30:00+01:00",
      "hora": "15:30",
      "local": "Sandiães",
      "link": "https://www.viralagenda.com/pt/events/1641692/ha-musica-popular-na-freguesia-sandiaes"
    },
    {
      "titulo": "Caminha Medieval 2025",
      "data_hora": "2025-07-23",
      "hora": null,
      "local": "Caminha (vila)",
      "link": "https://www.viralagenda.com/pt/events/1600563/caminha-medieval-2025"
    },
    {
      "titulo": "NEOPOP Festival 2025",
      "data_hora": "2025-08-07T17:00:00+01:00",
      "hora": "18:00",
      "local": "Viana do Castelo (cidade)",
      "link": "https://www.viralagenda.com/pt/events/1538745/neopop-festival-2025"
    },
    {
      "titulo": "Festa em Honra de Nossa Senhora da Agonia",
      "data_hora": "2025-08-15",
      "hora": null,
      "local": "Caminha (vila)",
      "link": "https://www.viralagenda.com/pt/events/1617502/festa-em-honra-de-nossa-senhora-da-agonia"
    },
    {
      "titulo": "Vilar de Mouros",
      "data_hora": "2025-08-20T15:00:00+01:00",
      "hora": "16:00",
      "local": "Vilar De Mouros",
      "link": "https://www.viralagenda.com/pt/events/1638328/vilar-de-mouros"
    }
]
"""

def responder(pergunta):
    prompt = f"""
A seguir tens uma lista de eventos culturais no Alto Minho em formato JSON:

{contexto}

Com base **apenas** nesta informação, responde à pergunta abaixo em **português**. Formata a resposta em Markdown, seguindo este modelo:

**📌 Título:** nome do evento  
**📅 Data e hora:** data e hora do evento (formato DD/MM/AAAA HH:MM, ou só DD/MM/AAAA se hora não disponível) 
**📍 Local:** local do evento  
🔗 [Link para o evento](url)

Se não encontrar eventos que respondam à pergunta, responde:  
❌ Não encontrei nenhum evento com essa informação.

Pergunta: {pergunta}

Resposta:
"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "max_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.9,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erro: {response.status_code} — {response.text}"

gr.Interface(
    fn=responder, 
    inputs=gr.Textbox(lines=3, label="Faz uma pergunta sobre os eventos"), 
    outputs=gr.Markdown(label="Resposta do Chatbot"),
    title="Chatbot de Eventos Alto Minho",
    description="Pergunta sobre eventos culturais na região do Alto Minho."
).launch()
