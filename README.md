# Automação de Relatório de Câmbio (USD/BRL) 📈

Este projeto automatiza o processo de monitoramento da cotação do dólar, gerando um relatório visual e enviando-o por e-mail de forma autônoma.

## 🚀 Funcionalidades
- **Extração de Dados:** Consome a AwesomeAPI para obter cotações atualizadas.
- **Data Viz:** Gera um gráfico de tendência dos últimos 30 dias utilizando Matplotlib.
- **Automação de E-mail:** Envia o relatório via SMTP com o gráfico em anexo.
- **Execução Agendada:** Configurado para rodar diariamente via Windows Task Scheduler.

## 🛠️ Tecnologias Utilizadas
- **Python 3.12**
- **Matplotlib** (Visualização de dados)
- **Requests** (Consumo de API)
- **Smtplib** (Protocolo de envio de e-mail)
  
---
### Como Rodar o Projeto
1. Clone o repositório.
2. Instale as dependências: `pip install matplotlib requests`.
3. Configure suas credenciais de e-mail nas variáveis de ambiente.
4. Execute o script: `python automacao_dolar.py`.
