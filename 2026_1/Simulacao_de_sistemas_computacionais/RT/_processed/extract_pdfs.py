from pathlib import Path
import json
from pypdf import PdfReader


def clean_text(text: str) -> str:
    if not text:
        return ""
    # Normalize excessive whitespace while preserving paragraph breaks.
    lines = [line.strip() for line in text.splitlines()]
    cleaned = []
    for line in lines:
        if line:
            cleaned.append(line)
        elif cleaned and cleaned[-1] != "":
            cleaned.append("")
    return "\n".join(cleaned).strip()


def main() -> None:
    base = Path(__file__).resolve().parent.parent
    out_dir = Path(__file__).resolve().parent

    pdfs = sorted(base.glob("*.pdf"))
    metadata = {}

    for pdf_path in pdfs:
        reader = PdfReader(str(pdf_path))
        page_texts = []
        for page in reader.pages:
            extracted = page.extract_text() or ""
            page_texts.append(clean_text(extracted))

        full_text = "\n\n".join([p for p in page_texts if p])
        txt_name = f"{pdf_path.stem}.txt"
        (out_dir / txt_name).write_text(full_text, encoding="utf-8")

        sample_start = full_text[:3000]
        sample_end = full_text[-2000:] if len(full_text) > 2000 else full_text
        metadata[pdf_path.name] = {
            "pages": len(reader.pages),
            "characters": len(full_text),
            "txt_file": txt_name,
            "sample_start": sample_start,
            "sample_end": sample_end,
        }

    (out_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
