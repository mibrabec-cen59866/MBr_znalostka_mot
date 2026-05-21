# MBr

## Extrakce odpovědí

Skript `scripts/extract_answers.py` prochází Outlook `.msg` soubory v rootu repozitáře, vybere odpovědi účastníků (`RE_`/`Re_`) a vygeneruje `answers.csv` se sloupci `odpovedel`, `den_mesic`, `hodnota`.

Lokální spuštění:

```bash
pip install -r requirements.txt
python scripts/extract_answers.py
```
