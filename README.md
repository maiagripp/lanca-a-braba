# 🤖 Lança Braba ChatBot 🔥💪

![Badge Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) 
![DeepSeek](https://img.shields.io/badge/DeepSeek-1E88E5?style=for-the-badge&logo=deepseek&logoColor=white) 
![LangChain](https://img.shields.io/badge/LangChain-512DA8?style=for-the-badge&logo=langchain&logoColor=white)

**O coach carioca mais brabo da internet!** Receba motivação explosiva sobre **fitness, código, viagens e vida** com gíria RJ, samba no pé e energia de Copacabana. *Lança a braba!*

[![Deploy](https://img.shields.io/badge/Deploy-Streamlit_Cloud-orange?style=for-the-badge&logo=streamlit&logoColor=white)](https://seu-app.streamlit.app)

## 🚀 Funcionalidades Brabas

- 💬 **Chat com memória** - Lembra toda conversa!
- 🧠 **Persona Carioca** - Coach "Lança Braba" com gíria RJ e motivação 24/7
- ⚡ **DeepSeek API** - IA chinesa barata e potente (compatível OpenAI)
- 📱 **UI Nativa Streamlit** - Chat como WhatsApp
- 🔒 **Secrets Seguros** - API key no .env/Streamlit Secrets
- 🏖️ **Temáticas**: Musculação, programação, viagens, vida de dev brasileiro

## 🎯 Demo

User: Tô desmotivado com Python hoje...
Lança Braba: EITA MALUCO! Python é tipo samba no pé - quanto mais tu treina, mais vira mestre!
Pega esse venv brabo aí e lança uns decorators que é só alegria!
Lança a braba! 🔥💪

text

## 🛠️ Tech Stack

| Frontend | Backend | IA |
|----------|---------|----|
| Streamlit | LangChain | DeepSeek |
| ChatInput | SessionState | OpenAI-compatible |

## 🚀 Deploy Fácil (Streamlit Cloud)

### 1. Estrutura
projeto/
├── app.py # 💎 Código principal
├── requirements.txt # 📦 Dependências
└── .streamlit/secrets.toml # 🔑 API Key (NÃO no Git!)

### 2. requirements.txt
```txt
streamlit>=1.38.0
python-dotenv
langchain-openai>=0.2.0
langchain-core>=0.3.0
```

### 3. Secrets (Streamlit Cloud)
```text
DEEPSEEK_API_KEY = "sk-sua-chave"
```

### 4. Deploy 2min
share.streamlit.io → GitHub → app.py → Secrets → Lançou! 🎉

## 🏃‍♂️ Rodar Local
bash
# 1. Clone
git clone seu-repo
cd projeto

# 2. API Key
export DEEPSEEK_API_KEY="sk-..."  # Ou .env

# 3. Instalar & Rodar
pip install -r requirements.txt
streamlit run app.py
🔧 Customizar Persona
Edite SystemMessage em app.py:
"Você é coach carioca explosivo..."

# Carioca default → "Coach explosivo RJ..."
# Ideias: Personal trainer, Professor React, Guia turístico debochado

🤝 Contribuições
Fork → Modifica → PR

⭐ Star pra motivar devs BR!

Issues com sugestões brabas!

Feito com ❤️ pro dev brasileiro! Rio, 2026

**Lança a braba pro seu próximo level! 🔥💪🏖️**
