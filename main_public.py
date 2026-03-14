import requests
import matplotlib.pyplot as plt
import datetime
import smtplib
from email.message import EmailMessage
import os

# --- CONFIGURAÇÕES DO E-MAIL DO USUÁRIO---
# Substitua os valores abaixo pelos seus dados antes de rodar localmente
MEU_EMAIL = "seu_email@gmail.com"
SENHA_APP = "sua_senha_de_app_aqui" #Aqui voce põem sua senha app que pode obter nas configurações de segurança da sua conta google
                                    #(autentificação de 2 fatores precisa estar ativada)
EMAIL_CHEFE = "destinatario@gmail.com"
def gerar_e_enviar():
    try:
        # 1. BUSCAR DADOS
        url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/30"
        dados = requests.get(url).json()
        datas, precos = [], []
        for dia in dados:
            dt = datetime.datetime.fromtimestamp(int(dia['timestamp']))
            datas.append(dt.strftime('%d/%m'))
            precos.append(float(dia['bid']))
        datas.reverse(); precos.reverse()

        # 2. GERAR O GRÁFICO (O QUE VOCÊ APROVOU)
        plt.style.use('seaborn-v0_8-muted')
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.plot(datas, precos, marker='o', color='#1b5e20', linewidth=3, markersize=6)
        ax.fill_between(datas, precos, min(precos) - 0.1, color='#4caf50', alpha=0.15)

        for i in range(len(datas)):
            ax.text(datas[i], precos[i] + 0.008, f'{precos[i]:.2f}', 
                    ha='center', va='bottom', fontsize=8, color='#1b5e20', fontweight='bold')

        ax.set_title(f'Relatório Diário: Evolução do Dólar ({datetime.date.today().strftime("%d/%m/%Y")})', 
                     fontsize=18, fontweight='bold', pad=30)
        plt.xticks(rotation=45)
        ax.set_ylim(min(precos) - 0.1, max(precos) + 0.15)
        ax.grid(True, linestyle=':', alpha=0.5)
        plt.tight_layout()

        # Salva a imagem temporariamente
        nome_img = 'relatorio_final.png'
        plt.savefig(nome_img, dpi=300)
        plt.close()

        # 3. CONSTRUIR O E-MAIL
        msg = EmailMessage()
        msg['Subject'] = f"Relatório de Cotação Dólar - {datetime.date.today().strftime('%d/%m/%Y')}"
        msg['From'] = MEU_EMAIL
        msg['To'] = EMAIL_CHEFE
        msg.set_content(f"Bom dia!\n\nSegue anexo o relatório de cotação dos últimos 30 dias.\nValor de fechamento mais recente: R$ {precos[-1]:.2f}")

        with open(nome_img, 'rb') as f:
            msg.add_attachment(f.read(), maintype='image', subtype='png', filename=nome_img)

        # 4. ENVIAR
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(MEU_EMAIL, SENHA_APP)
            smtp.send_message(msg)
        
        print("Relatório enviado com sucesso para o chefe!")

        # ... (final do seu código de envio)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(MEU_EMAIL, SENHA_APP)
            smtp.send_message(msg)
        
        print("E-MAIL ENVIADO COM SUCESSO!")
        import time
        time.sleep(5) # Dá 5 segundos para o Windows processar o envio
        
        # Remove a imagem depois de enviar para não deixar rastro
        os.remove(nome_img)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    gerar_e_enviar()