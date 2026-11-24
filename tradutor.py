import os
import sys
import fitz  # PyMuPDF
from deep_translator import GoogleTranslator
from fpdf import FPDF


def translate_pdf(pdf_path: str, output_pdf_path: str, target_lang: str = "pt") -> int:
    """Lê um arquivo PDF, traduz página a página e gera um novo PDF traduzido."""
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"Arquivo PDF não encontrado: {pdf_path}")

    doc = fitz.open(pdf_path)
    translator = GoogleTranslator(source="auto", target=target_lang)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Helvetica", size=10)

    translated_pages = 0
    for page_num, page in enumerate(doc):
        text = page.get_text().strip()
        if not text:
            continue
        try:
            translated = translator.translate(text)
            pdf.add_page()
            safe_text = f"Página {page_num + 1}\n\n{translated}".encode("latin-1", "replace").decode("latin-1")
            pdf.multi_cell(0, 5, safe_text)
            translated_pages += 1
            print(f"Página {page_num + 1} traduzida.")
        except Exception as exc:
            print(f"Erro na página {page_num + 1}: {exc}")

    pdf.output(output_pdf_path)
    return translated_pages


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "entrada.pdf"
    dst = sys.argv[2] if len(sys.argv) > 2 else "saida_traduzido.pdf"
    try:
        pages = translate_pdf(src, dst)
        print(f"Tradução finalizada! {pages} página(s) salva(s) em: {dst}")
    except Exception as err:
        print(f"Falha ao traduzir PDF: {err}")
        sys.exit(1)
