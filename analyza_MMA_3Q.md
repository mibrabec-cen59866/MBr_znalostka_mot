# Analýza motivační dokumentace bonusů – segment MMA, 3Q 2026

> Verze: **v1** (2026-07-13)
> Rozsah: segment **MMA**, období **3Q 2026**. Analýza pouze popisuje; neupravuje dokumenty ani nenavrhuje opravy.

## Dohodnutá pravidla práce (zadavatel)

1. **Žádná řídicí hierarchie dokumentů.** Pokud se dokumenty liší nebo neshodují, je to nesrovnalost, kterou je nutné řešit (nic se automaticky „neprohlašuje za správné“ podle nadřazenosti dokumentu).
2. Segment i období se ověřuje **z názvu souboru** (provizní list a metodika uvnitř identifikaci neobsahují – uzavřeno).
3. **„Mass Affluent“ = „Mass Market“** – brát jako totéž (uzavřeno).
4. **Definice objemu:**
   - **Sjednaný objem** = objem, který bankéř reálně uzavře s klientem (reálná smlouva).
   - **Započtený objem** = to, co se bankéři započte do motivačního plnění; může být oříznut limitem.
   - Příklad: limit na hypotéku 2 mil. Kč, reálná smlouva 5 mil. Kč → započte se pouze 2 mil. Kč.
5. **product_tree.xml** je zdroj mapování produkt → skupina → jednotka plánu. Sloupce:
   - `OKOPROD_SOURCE_ID` – název produktu anglicky
   - `OKOPROD_NAME` – název produktu česky
   - `OKOPRODG_SOURCE_ID` – produktová skupina anglicky
   - `OKOPRODG_NAME` – produktová skupina česky
   - `OKOM_SOURCE_ID` – na co se plánuje: **O = objem, K = kus, null = skupina OTHER (bez plánu)**
6. Referenční data pro validaci oracle: **budou později**, zatím se na ně neptat.
7. Výstup: ukládat do tohoto souboru a **verzovat**, zároveň odpovídat i v chatu.

## STAV VSTUPNÍCH PODKLADŮ

| Podklad | Stav |
|---|---|
| segmentovy_dokument_mma_2026_3q.pdf | k dispozici |
| metodika_zapocitavani_mma_2026_3q.xlsx | k dispozici |
| karta_motivace_mma_3q2026.pdf | k dispozici |
| provizní list_mma_3q2026.pdf | k dispozici |
| **product_tree.xml** | **CHYBÍ – nedorazil do repozitáře/prostředí** (blokuje O1: mapování produkt→skupina) |

---

## 1. Přehled analyzovaných dokumentů

| Dokument | Typ | Segment | Období | Poznámka |
|---|---|---|---|---|
| segmentovy_dokument_mma_2026_3q.pdf | Segmentový dokument | MMA (str. 2) | 3Q 2026 (titulní strana) | 18 stran, obsahuje i karty motivace |
| metodika_zapocitavani_mma_2026_3q.xlsx | Metodika započítávání | dle názvu souboru | dle názvu souboru | 1 list „metodika“, 28 řádků |
| karta_motivace_mma_3q2026.pdf | Karta motivace | dle názvu (uvnitř „MMA“ jen v kódu MMMA) | 3Q2026 (záhlaví stran) | 8 pozic |
| provizní list_mma_3q2026.pdf | Provizní list | dle názvu souboru | dle názvu souboru | 1 strana, matice provizí |

---

## 2. Shrnutí jednotlivých dokumentů

### 2.1 Segmentový dokument motivace MMA (3Q 2026)
**Klíčové hodnoty:** váhy kritérií (OBA/OBAS 60/40; OBAH 25/25/25/25; Pokladník 60/40; manažeři 60/40; FLE/FLET 30/70; nováček paušál 7 000 Kč). Roční příslib: OBA/OBAS/…_pov/FLE 20 %, OBAH/Pokladník 15 %, manažeři 20 %. Výplata čtvrtletně, min. 100 Kč. Koeficient plnění: <80 %→0,0; 80–89→0,8; 90–99→0,9; 100–109→1,1; 110–119→1,2; 120+→1,3. Zlaté pásmo: ≥100 % v min. 8 skupinách → ×1,2. 10 plánovaných skupin. Digi bonus: 45 obchodů v mobilu. Salesforce příležitosti/předání s definovanými platnostmi.

### 2.2 Metodika započítávání (Excel)
**Klíčové hodnoty:** pro každý produkt podmínky započtení, datum, zdrojová aplikace/pole s ID, odečet při stornu. Limity: Firemní úvěr/Leasing max **2 700 000 Kč**; IS jednorázové do 10 mil. Kč; IS pravidelné do 40 000 Kč; stav. spoření min. vklad 1 500 Kč; DPS min. 500 Kč / navýšení 100 Kč. Novost účtu 90 dnů, věková pásma, pravidla asistence bankéře, dělení 50:50 u příležitostí na investování.

### 2.3 Karta motivace (8 pozic)
**Paušály za bod:** OBA 1 800 Kč; OBAS 2 200 Kč; OBAH 700 Kč (+ paušál za prodej 400 Kč/skupinu; Podpora 80+ →4 200 / 40–79 →2 600 / <40 →0; Servicing min. 20 op.: 80 %+→4 200 / 60–79 %→2 600 / <60 %→0); Pokladník 1 300 Kč (paušál prodej 800 Kč/skupinu); manažeři 1/10 příslibu + převod bodů FZ na %; FLE/FLET dle počtu přesměrování (30+→100 %, 20–29→50 %, <20→0 %). Digi bonus +45 ks = 800 Kč (OBA/OBAS).

### 2.4 Provizní list
**Jednotka / báze / sazba** (výběr): Úvěry (objem/100 000) 120/180 Kč (bez/s poj.), Firemní úvěry & Leasing 80/120; Bydlení (objem/100 000) 40/60; Účty (ks) Plus 70, Student/Standard 35, Firemní 100, Živnostník 50; Revolvingy (ks) 25, Firemní KTK 50; Stavební spoření (ks) 40; Investice jednorázové (objem/100 000) 30; Investice pravidelné (objem/1 000) 15; Penze (ks) 40; Životní poj. (objem/1 000) 40, Soběstačnost 15; Neživotní (objem/1 000) Nemovitostní 25 / Auto 10 / Odp. zaměstnance 5 / Podnikatelská 15; Ostatní: Strukturovaná depozita (objem/100 000) 15, Účet 0-7 let 35, Mobilita 50, POVK 50, Cestovní 50, Global Payments 100, Přesměrování Erste Premier 400, EPB 1 200, Penze navýšení 10, Scoring HYPO 100 (vše ks).

---

## 3. Report nesrovnalostí (aktivní)

| Č. | Typ | Dotčené dokumenty | Popis | Místo | Závažnost | Stav |
|---|---|---|---|---|---|---|
| N3 | Definiční | Segment. dok. ↔ Karta | 4. kritérium OBAH: „Digitalizace“ (tab.) vs. „Servicing“ (text/karta) | seg. str. 3 vs. str. 8 / karta OBAH | střední | otevřené (O7) |
| N4 | Mezidokumentová | Provizní list ↔ Metodika ↔ plán | Skupiny „Úvěry“/„Bydlení“ (provizní list, metodika) vs. „Nezajištěné/Zajištěné úvěry“ (plán). Mapování nejasné. | provizní list; metodika; seg. str. 4 | střední | čeká na product_tree.xml (O1) |
| N6 | Chybějící info | Provizní list ↔ ostatní | Sazba „s pojištěním“ vs. „bez“ (120/180) – podmínka uplatnění nikde nepopsána | provizní list, blok Úvěry/Bydlení | střední | otevřené (O2) |
| N7 | Logická | Segment. dok. + karty | Skok koeficientu 0,9 (90–99 %) → 1,1 (100–109 %); chybí 1,0 | seg. str. 4; karty | nízká | otevřené (O5) |
| N8 | Úplnost | Segment. dok. | Rekonstrukce poboček neuvádí Area lead ani FLE/FLET | seg. str. 9 | nízká | otevřené (O9) |
| N9 | Definiční (drobné) | Provizní list ↔ Metodika | Odlišné názvy/seskupení: Mobilita vs. Kodex mobility; Živ. poj. dvě sazby vs. jeden řádek | provizní list vs. metodika | nízká | otevřené |

---

## 4. Otevřené otázky (register – opakuje se, dokud nezavřeme)

**Uzavřené:** segment/období z názvu (bod 2) · Mass Affluent = Mass Market (bod 3) · sjednaný vs. započtený objem definován (bod 4) · reference data – odloženo (bod 5).

| ID | Otázka | Proč | Stav |
|---|---|---|---|
| O1 | Mapování produkt → plánová skupina + jednotka | plnění plánu | čeká na **product_tree.xml** |
| O2 | Podmínka pro sazbu „s pojištěním“ vs. „bez“ | výpočet provize | otevřené |
| O3 | Vzorec provize = (objem / báze) × sazba, lineárně i u neúplných násobků? | vzorec | otevřené |
| O4 | Zlaté pásmo: 8 z kolika; jak se počítají skupiny bez plánu | koef. 1,2 | otevřené |
| O5 | Hranice pásem (≥100 %→1,1?), absence 1,0, zaokrouhlení před zařazením | koeficient | otevřené |
| O6 | Půlení 50 % – z provize, nebo z objemu/ks | výpočet + plán | otevřené |
| O7 | „Digitalizace“ vs. „Servicing“ (OBAH) | název kritéria | otevřené |
| O8 | Storna přes čtvrtletí; odečet u skupiny pod 80 % | nápočet 3Q | otevřené |
| O9 | Rekonstrukce poboček – Area lead a FLE/FLET? | úplnost | otevřené |
| O10 | Jsou tyto soubory finální verze bez dodatků? | platnost | otevřené |
| O11 | Autoritativní zdroj paušálů za bod (karta vs. nominační listy/rozpis) | hodnoty | otevřené |
| O12 | Nahrání **product_tree.xml** (nedorazil) | mapování | otevřené |
