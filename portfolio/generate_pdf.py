#!/usr/bin/env python3
"""Generate a Korean-friendly PDF from a markdown portfolio file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def register_korean_font() -> Tuple[str, str]:
    """Register a system font that can render Korean text."""
    candidates = [
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansKR-Regular.otf",
        "/usr/share/fonts/truetype/macos/SanFrancisco.ttf",
    ]

    for font_path in candidates:
        if Path(font_path).exists():
            font_name = "PortfolioKRFont"
            pdfmetrics.registerFont(TTFont(font_name, font_path))
            return font_name, font_path

    raise FileNotFoundError(
        "Korean-capable font was not found. "
        "Install a CJK font (e.g., Noto Sans CJK KR)."
    )


def build_styles(font_name: str) -> Dict[str, ParagraphStyle]:
    return {
        "title": ParagraphStyle(
            "title",
            fontName=font_name,
            fontSize=21,
            leading=28,
            spaceAfter=12,
        ),
        "h1": ParagraphStyle(
            "h1",
            fontName=font_name,
            fontSize=17,
            leading=24,
            spaceBefore=12,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "h2",
            fontName=font_name,
            fontSize=14,
            leading=20,
            spaceBefore=9,
            spaceAfter=6,
        ),
        "h3": ParagraphStyle(
            "h3",
            fontName=font_name,
            fontSize=12,
            leading=18,
            spaceBefore=7,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            fontName=font_name,
            fontSize=10.5,
            leading=16,
            spaceAfter=3,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName=font_name,
            fontSize=10.5,
            leading=16,
            leftIndent=12,
            firstLineIndent=-8,
            spaceAfter=2,
        ),
        "quote": ParagraphStyle(
            "quote",
            fontName=font_name,
            fontSize=10,
            leading=15,
            leftIndent=16,
            textColor="#4A4A4A",
            spaceAfter=3,
        ),
        "table": ParagraphStyle(
            "table",
            fontName=font_name,
            fontSize=9.3,
            leading=14,
            leftIndent=6,
            textColor="#333333",
            spaceAfter=1,
        ),
        "code": ParagraphStyle(
            "code",
            fontName=font_name,
            fontSize=9.5,
            leading=14,
            leftIndent=12,
            textColor="#222222",
            spaceAfter=2,
        ),
    }


def normalize_inline_markdown(text: str) -> str:
    """Very small markdown normalization for Paragraph rendering."""
    escaped = escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<font color='#444444'>\1</font>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", escaped)
    return escaped


def parse_markdown_to_story(markdown_text: str, styles: Dict[str, ParagraphStyle]) -> List:
    story: List = []
    in_code_block = False

    for raw_line in markdown_text.splitlines():
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            story.append(Spacer(1, 5))
            continue

        if not stripped:
            story.append(Spacer(1, 7))
            continue

        if stripped == "---":
            story.append(Spacer(1, 10))
            continue

        if in_code_block:
            story.append(Paragraph(normalize_inline_markdown(stripped), styles["code"]))
            continue

        if stripped.startswith("# "):
            story.append(Paragraph(normalize_inline_markdown(stripped[2:]), styles["title"]))
            continue

        if stripped.startswith("## "):
            story.append(Paragraph(normalize_inline_markdown(stripped[3:]), styles["h1"]))
            continue

        if stripped.startswith("### "):
            story.append(Paragraph(normalize_inline_markdown(stripped[4:]), styles["h2"]))
            continue

        if stripped.startswith("#### "):
            story.append(Paragraph(normalize_inline_markdown(stripped[5:]), styles["h3"]))
            continue

        if re.match(r"^\d+\.\s+", stripped):
            story.append(
                Paragraph(normalize_inline_markdown(stripped), styles["bullet"])
            )
            continue

        if stripped.startswith("- "):
            item = "• " + stripped[2:]
            story.append(Paragraph(normalize_inline_markdown(item), styles["bullet"]))
            continue

        if stripped.startswith("> "):
            story.append(
                Paragraph(normalize_inline_markdown(stripped[2:]), styles["quote"])
            )
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            row = stripped.strip("|")
            cells = [c.strip() for c in row.split("|")]
            story.append(
                Paragraph(
                    normalize_inline_markdown(" | ".join(cells)),
                    styles["table"],
                )
            )
            continue

        story.append(Paragraph(normalize_inline_markdown(stripped), styles["body"]))

    return story


def build_pdf(input_path: Path, output_path: Path) -> None:
    font_name, font_path = register_korean_font()
    styles = build_styles(font_name)
    markdown_text = input_path.read_text(encoding="utf-8")
    story = parse_markdown_to_story(markdown_text, styles)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=42,
        rightMargin=42,
        topMargin=42,
        bottomMargin=42,
        title="AI Agents Practice Projects Portfolio",
        author="AI Portfolio Generator",
    )

    def draw_page_number(canvas, _doc):
        canvas.setFont(font_name, 9)
        canvas.drawRightString(A4[0] - 42, 20, f"Page {_doc.page}")

    doc.build(story, onFirstPage=draw_page_number, onLaterPages=draw_page_number)
    print(f"[OK] PDF created: {output_path}")
    print(f"[INFO] Using font: {font_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate portfolio PDF from markdown.")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("portfolio/AI_Agents_Practice_Portfolio_KR.md"),
        help="Input markdown file path",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("portfolio/AI_Agents_Practice_Portfolio_KR.pdf"),
        help="Output PDF file path",
    )
    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")

    build_pdf(args.input, args.output)


if __name__ == "__main__":
    main()

