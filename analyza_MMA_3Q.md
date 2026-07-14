# Analýza motivační dokumentace bonusů – segment MMA, 3Q 2026

> Verze: **v2** (2026-07-14)
> Rozsah: segment **MMA**, období **3Q 2026**. Analýza pouze popisuje; neupravuje dokumenty ani nenavrhuje opravy.
>
> **Změny ve v2:** doplněny podklady `product_tree.xml` a `positions.xml`; vyřešeno mapování produkt→skupina→jednotka (O1) a potvrzeny jednotky; přidány nové nesrovnalosti z `positions.xml`; pilot „Úvěry“ dle zadavatele skončil → ignorováno; doplněny odkazy (6202_10_01R, Salesforce Q&A).

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
| **product_tree.xml** | **k dispozici** (103 produktů, 10 plánovaných skupin + OTHER) |
| **positions.xml** | **k dispozici** (114 pozic, z toho 15 v segmentu MMA) |

> Pozn.: zadavatel avizoval, že může dorazit další dokumentace; pracuje se s aktuálně dostupnými podklady.

## MAPOVÁNÍ PRODUKTOVÝCH SKUPIN (dle product_tree.xml) – vyřešení O1

Plánované skupiny (`OKOM_SOURCE_ID` = O objem / K kus) a nomenklatura:

| Skupina (OKOPRODG_SOURCE_ID) | Název (OKOPRODG_NAME) | Jednotka plánu | Odpovídá plánové skupině v segm. dok./kartách |
|---|---|---|---|
| LOANS | Úvěry | **O** (objem) | „Nezajištěné úvěry“ |
| HYPO | Bydlení | **O** (objem) | „Zajištěné úvěry“ |
| ACCOUNTS | Účty | **K** (kus) | Účty |
| LOANREV | Revolvingové úvěry | **K** (kus) | Revolvingy |
| BSD | Stavební spoření | **K** (kus) | Stavební spoření |
| PENSION | Penze | **K** (kus) | Penze |
| INV_SIMPLE | Investice jednorázové | **O** (objem) | Investice jednorázové |
| INV_REGULAR | Investice pravidelné | **O** (objem) | Investice pravidelné |
| INS_LIFE | Životní pojištění | **O** (objem) | Životní pojištění |
| INS_NONLIFE | Neživotní pojištění | **O** (objem) | Neživotní pojištění |
| OTHER | Ostatní | **null** (bez plánu) | „Ostatní bez plánu“ |

**Ověřené shody (pozitivní zjištění):**
- Počet plánovaných skupin = **10** + OTHER → odpovídá segmentovému dokumentu i kartám.
- **Jednotky (objem/kus)** z `product_tree.xml` **plně sedí** s províznim listem i kartami motivace u všech skupin.
- Zařazení produktů z bloku „Ostatní“ provizního listu (Strukturovaná depozita, Účet 0-7 let, Mobilita, POVK, Cestovní pojištění, Global Payments, Přesměrování Premier/EPB, Penze navýšení, Scoring HYPO) do skupiny **OTHER (bez plánu)** je konzistentní.
- **Firemní úvěry** a **Leasing** patří do skupiny **LOANS (Úvěry) = plánová „Nezajištěné úvěry“** (objem). „Bydlení“ (HYPO/AMHYPO/Zajištěné SSČS) = plánová „Zajištěné úvěry“.


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

### 2.5 product_tree.xml (číselník produktů → skupina → jednotka)
103 produktů rozdělených do 11 skupin (viz sekce „Mapování produktových skupin“). Definuje jednotku plánu (`OKOM_SOURCE_ID`: O objem / K kus / null bez plánu). Slouží jako autoritativní zdroj pro zařazení produktu do plánové skupiny a určení jednotky. Jednotky odpovídají províznimu listu a kartám.

### 2.6 positions.xml (číselník pozic)
114 pozic napříč segmenty (EPB 11, HC 11, IS 5, KC 46, MMA 15, MSE 7, PS 6, TA 13). Segment **MMA má 15 pozic** (SALES/SERVICE/MNGR) s kódem, popisem, motivačním kódem. Použije se k ověření mapování pozic z kap. 1 segmentového dokumentu. Zjištěné nesrovnalosti viz N10–N13.

---

## 3. Report nesrovnalostí (aktivní)

| Č. | Typ | Dotčené dokumenty | Popis | Místo | Závažnost | Stav |
|---|---|---|---|---|---|---|
| N3 | Definiční | Segment. dok. ↔ Karta | 4. kritérium OBAH: „Digitalizace“ (tab.) vs. „Servicing“ (text/karta) | seg. str. 3 vs. str. 8 / karta OBAH | střední | otevřené (O7) |
| N4 | Definiční (nomenklatura) | product_tree/provizní list/metodika ↔ segment. dok./karty | Oficiální názvy skupin jsou **„Úvěry“ (LOANS)** a **„Bydlení“ (HYPO)**, ale plánové tabulky v segm. dok. a kartách používají **„Nezajištěné úvěry“** a **„Zajištěné úvěry“**. Mapování je vydedukovatelné, ale názvy nejsou sjednocené. | product_tree; provizní list; metodika; seg. str. 4 | střední | popsáno; potvrdit (O14) |
| N6 | Chybějící info | Provizní list ↔ ostatní | Sazba „s pojištěním“ vs. „bez“ (120/180) – podmínka uplatnění nikde nepopsána | provizní list, blok Úvěry/Bydlení | střední | otevřené (O2) |
| N7 | Logická | Segment. dok. + karty | Skok koeficientu 0,9 (90–99 %) → 1,1 (100–109 %); chybí 1,0 | seg. str. 4; karty | nízká | otevřené (O5) |
| N8 | Úplnost | Segment. dok. | Rekonstrukce poboček neuvádí Area lead ani FLE/FLET | seg. str. 9 | nízká | otevřené (O9) |
| N9 | Definiční (drobné) | Provizní list ↔ Metodika | Odlišné názvy/seskupení: Mobilita vs. Kodex mobility; Živ. poj. dvě sazby vs. jeden řádek | provizní list vs. metodika | nízká | otevřené |
| N10 | Pokrytí segmentu | positions.xml ↔ segment. dok./karty | **FLE/FLET nejsou v positions.xml** (v žádném segmentu), přestože segmentový dokument i karty popisují pozice Future LAB expert (FLE) a FLET pro MMA. | positions.xml (MMA); seg. str. 15, karta str. 7–8 | vysoká | nové |
| N11 | Definiční / pokrytí | positions.xml ↔ segment. dok. (kap. 1) | **Kolize kódů manažerských pozic.** Seg. dok.: MMMT = team lead, **MMMA = area lead**. positions.xml pro MMA má MMMT (mot=Manažer_MMA) + navíc **MMM1** (retail team lead), **MMM2** (retail area lead), **MMM3** (retail regional lead); **kód MMMA neexistuje**. Karta pro „Regional lead“ chybí, ač se v seg. dok. zmiňuje. | positions.xml; seg. str. 1, str. 17 | vysoká | nové |
| N12 | Definiční | positions.xml ↔ segment. dok. (kap. 1) | **Servisní pozice nekonzistentní.** Seg. dok.: BKPJ = „Pokladník“, BKPM = „OBAH“. positions.xml má navíc **CAS** (Pokladník) a **OBAK** (Bankéř klientské péče, mot=OBAH), přičemž řádky **BKPJ i BKPM mají v popisu shodně „OBAH“**. Nejednoznačné, který kód je platný. | positions.xml; seg. str. 1 | střední | nové |
| N13 | Definiční | positions.xml ↔ segment. dok. (kap. 1) | Motivační kódy nesouhlasí se seskupením v seg. dok. Seg. dok.: OBAJ/OBAM = „OBA“, OBAS/OBAMa = „OBAS“. positions.xml: OBAJ (mot=OBAJ), OBAM (mot=OBAM) – **negrupováno**; navíc **OBAP** (Osobní bankéř Plus) neuvedený v seg. dok., a **OBAMa (master)** ze seg. dok. v positions.xml chybí. | positions.xml; seg. str. 1 | střední | nové |

---

## 4. Otevřené otázky (register – opakuje se, dokud nezavřeme)

**Uzavřené:** segment/období z názvu · Mass Affluent = Mass Market · sjednaný vs. započtený objem · reference data (odloženo) · **O1 mapování produkt→skupina→jednotka (vyřešeno přes product_tree.xml)** · product_tree.xml (dodán) · pilot „Úvěry“ (skončil → ignorovat).

| ID | Otázka | Proč | Stav |
|---|---|---|---|
| O2 | Podmínka pro sazbu „s pojištěním“ vs. „bez“ | výpočet provize | otevřené |
| O3 | Vzorec provize = (objem / báze) × sazba, lineárně i u neúplných násobků? | vzorec | otevřené |
| O4 | Zlaté pásmo: 8 z 10 skupin; jak se počítají skupiny bez plánu / s nulovým plánem | koef. 1,2 | otevřené |
| O5 | Hranice pásem (≥100 %→1,1?), absence 1,0, zaokrouhlení před zařazením | koeficient | otevřené |
| O6 | Půlení obchodů 50 % – z provize, nebo z objemu/ks (a dopad na plán) | výpočet + plán | otevřené |
| O7 | „Digitalizace“ vs. „Servicing“ (OBAH) – závazný název kritéria | definiční | otevřené |
| O8 | Storna přes čtvrtletí; odečet u skupiny pod 80 % plánu | nápočet 3Q | otevřené |
| O9 | Rekonstrukce poboček – mají nárok Area lead a FLE/FLET? | úplnost | otevřené |
| O10 | Jsou tyto soubory finální verze bez dodatků? | platnost | otevřené |
| O11 | Autoritativní zdroj paušálů za bod (karta vs. nominační listy/rozpis) | hodnoty | otevřené |
| O13 | Platné kódy pozic MMA: MMMA vs. MMM1/2/3; existence FLE/FLET; CAS/OBAK vs. BKPJ/BKPM; OBAP/OBAMa | mapování pozic pro nápočet | nové (N10–N13) |
| O14 | Potvrdit nomenklaturu skupin úvěrů: LOANS=„Nezajištěné úvěry“, HYPO=„Zajištěné úvěry“ | konzistence plánu | nové (N4) |
