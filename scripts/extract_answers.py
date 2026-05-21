#!/usr/bin/env python3
"""Extrakce odpovědí z Outlook .msg souborů do CSV."""

from __future__ import annotations

import argparse
import csv
import glob
import re
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Iterable

import extract_msg

NUMBER_PATTERN = re.compile(r"[-+]?\d{1,3}(?:[ .\u00A0]\d{3})*(?:[.,]\d+)?|\d+(?:[.,]\d+)?")
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")
ENCODING_FALLBACKS = (None, "cp1250")
MISSING_DATE_SORT_KEY = "99.99"


# Kontrola názvu souboru, zda jde o odpověď účastníka.
def is_participant_reply(file_name: str) -> bool:
    return file_name.strip().lower().startswith("re_")


# Odstranění citovaného původního textu pod oddělovačem.
def trim_quoted_text(body: str) -> str:
    lines = body.splitlines()
    kept_lines: list[str] = []

    for line in lines:
        normalized = line.strip().lower()
        if (
            normalized.startswith("from:")
            or normalized.startswith("od:")
            or normalized.startswith("-----original message-----")
            or re.match(r"^_{3,}\s*$", normalized)
        ):
            break
        kept_lines.append(line)

    return "\n".join(kept_lines)


# Vytáhne první číselnou odpověď z textu.
def extract_first_number(body: str) -> str:
    match = NUMBER_PATTERN.search(body)
    return match.group(0) if match else ""


# Zprávu převede na DD.MM; při chybě vrací prázdný řetězec.
def format_day_month(message: extract_msg.Message) -> str:
    for attribute in ("parsedDate", "date"):
        value = getattr(message, attribute, None)
        if not value:
            continue

        if isinstance(value, datetime):
            return value.strftime("%d.%m")

        if isinstance(value, str):
            stripped = value.strip()
            if not stripped:
                continue
            try:
                parsed = parsedate_to_datetime(stripped)
            except (TypeError, ValueError):
                continue
            if parsed:
                return parsed.strftime("%d.%m")

    return ""


# Vytáhne adresu odesílatele, případně fallback na zobrazované jméno.
def extract_sender(message: extract_msg.Message) -> str:
    candidates: Iterable[str | None] = (
        getattr(message, "sender_email", None),
        getattr(message, "sender", None),
        getattr(message, "from", None),
        getattr(message, "from_", None),
    )

    first_non_empty = ""
    for value in candidates:
        if not value:
            continue

        cleaned = str(value).strip()
        if not cleaned:
            continue

        if not first_non_empty:
            first_non_empty = cleaned

        email_match = EMAIL_PATTERN.search(cleaned)
        if email_match:
            return email_match.group(0)

    return first_non_empty


def process_msg_file(path: Path) -> dict[str, str]:
    last_error: Exception | None = None
    for encoding in ENCODING_FALLBACKS:
        kwargs = {}
        if encoding:
            kwargs["overrideEncoding"] = encoding

        message = extract_msg.Message(str(path), **kwargs)
        try:
            sender = extract_sender(message)
            day_month = format_day_month(message)
            body = message.body or ""
            value = extract_first_number(trim_quoted_text(body))
            return {"odpovedel": sender, "den_mesic": day_month, "hodnota": value}
        except UnicodeDecodeError as exc:
            last_error = exc
        finally:
            message.close()

    if last_error:
        raise last_error
    raise RuntimeError(f"Nepodařilo se zpracovat soubor: {path.name}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extrakce odpovědí z MSG souborů")
    parser.add_argument("--root", default=".", help="Adresář se vstupními .msg soubory")
    parser.add_argument("--output", default="answers.csv", help="Název výstupního CSV")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output = Path(args.output)
    if not output.is_absolute():
        output = root / output

    rows: list[dict[str, str]] = []
    processed = 0
    skipped = 0
    no_number = 0

    for file_path in sorted(Path(p) for p in glob.glob(str(root / "*.msg"))):
        if not is_participant_reply(file_path.name):
            skipped += 1
            continue

        try:
            row = process_msg_file(file_path)
        except Exception as exc:  # noqa: BLE001
            skipped += 1
            print(f"Chyba při zpracování {file_path.name}: {exc}")
            continue

        processed += 1
        if not row["hodnota"]:
            no_number += 1
        rows.append(row)

    rows.sort(key=lambda row: (row["den_mesic"] or MISSING_DATE_SORT_KEY, row["odpovedel"].lower()))

    with output.open("w", encoding="utf-8-sig", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["odpovedel", "den_mesic", "hodnota"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Zpracováno: {processed}")
    print(f"Přeskočeno: {skipped}")
    print(f"Bez čísla: {no_number}")


if __name__ == "__main__":
    main()
