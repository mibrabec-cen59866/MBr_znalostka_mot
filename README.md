# MBr

## Struktura repozitáře

- `motivacni_dokumenty/` – zdrojové motivační dokumenty (PDF, Excel), členěné do podsložek dle segmentu.
  - `motivacni_dokumenty/MMA/` – podklady pro segment MMA (Mass Market).
  - `motivacni_dokumenty/EPB/` – podklady pro segment EPB.
  - `motivacni_dokumenty/PREM/` – podklady pro segment PREM (Premier).
  - `motivacni_dokumenty/IS/` – podklady pro segment IS (Investiční specialisté).
  - `motivacni_dokumenty/HC/` – podklady pro segment HC (Hypoteční centrum).
  - `motivacni_dokumenty/PS/` – podklady pro segment PS (Private Segment).
  - `motivacni_dokumenty/OBECNE/` – podklady platné napříč segmenty (obecná pravidla, nadřazené předpisy).
- `ciselniky/` – číselníky (`positions.xml`, `product_tree.xml`).
- `technical/` – technické podklady: analýzy, prompty, extrahované odpovědi a skripty.

## Extrakce odpovědí

Skript `technical/scripts/extract_answers.py` prochází Outlook `.msg` soubory v rootu repozitáře, vybere odpovědi účastníků (`RE_`/`Re_`) a vygeneruje `answers.csv` se sloupci `odpovedel`, `den_mesic`, `hodnota`.

Lokální spuštění:

```bash
pip install -r requirements.txt
python technical/scripts/extract_answers.py --output technical/answers.csv
```
