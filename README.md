# 📄 Tradutor de PDF

Automação em **Python** para extrair texto de documentos PDF, traduzir automaticamente para português e gerar um novo PDF traduzido.

## ✨ Funcionalidades
- Extração de texto página a página com **PyMuPDF (`fitz`)**
- Tradução automática com **GoogleTranslator (`deep-translator`)**
- Geração de novo documento PDF formatado com **FPDF**
- Tratamento de erros para arquivos ausentes e falhas de rede

## 🛠️ Tecnologias
- Python 3.10+
- PyMuPDF (`fitz`)
- `deep-translator`
- `fpdf2`
- `pytest`

## 🚀 Instalação e Uso
```bash
git clone https://github.com/willams502/Tratudor-de-PDF.git
cd Tratudor-de-PDF
pip install -r requirements.txt
python tradutor.py caminho/entrada.pdf caminho/saida.pdf
```

## 🧪 Testes
```bash
pytest
```

## 👤 Autor
**Matheus Willams** — [GitHub](https://github.com/willams502) · [LinkedIn](https://www.linkedin.com/in/matheuswillams/)
