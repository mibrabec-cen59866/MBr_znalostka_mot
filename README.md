# MBr

## Struktura repozitáře

- `motivacni_dokumenty/` – zdrojové motivační dokumenty (PDF, Excel), členěné do podsložek dle segmentu.
  - `motivacni_dokumenty/MMA/` – podklady pro segment MMA.
- `ciselniky/` – číselníky (`positions.xml`, `product_tree.xml`).
- `technical/` – technické podklady: analýzy, prompty, extrahované odpovědi a skripty.

## Extrakce odpovědí

Skript `technical/scripts/extract_answers.py` prochází Outlook `.msg` soubory v rootu repozitáře, vybere odpovědi účastníků (`RE_`/`Re_`) a vygeneruje `answers.csv` se sloupci `odpovedel`, `den_mesic`, `hodnota`.

Lokální spuštění:

```bash
pip install -r requirements.txt
python technical/scripts/extract_answers.py --output technical/answers.csv
```
