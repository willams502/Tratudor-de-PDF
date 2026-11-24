import pytest
from tradutor import translate_pdf


def test_missing_pdf_raises():
    with pytest.raises(FileNotFoundError):
        translate_pdf("arquivo_inexistente.pdf", "out.pdf")
