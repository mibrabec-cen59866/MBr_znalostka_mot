# Analýza motivační dokumentace bonusů – segment MMA, 3Q 2026

> Verze: **v6** (2026-07-15)
> Rozsah: segment **MMA**, období **3Q 2026**. Analýza pouze popisuje; neupravuje dokumenty ani nenavrhuje opravy.
>
> **Změny ve v6 (BA review):** doplněna sekce **5. BA review** – pohled byznys analytika na celou dokumentaci bonusů MMA (co nedává smysl / co si protiřečí / co lze zjednodušit). Do registru otevřených otázek přidáno **5 nových otázek k doptání**: **NOVÁ-1** (chování koeficientu při záporném plnění / storno pod 0 %), **NOVÁ-2** (aplikace zlatého pásma ×1,2 vs. základní koeficient – pořadí a agregát), **NOVÁ-3** (cliff na hranici 80 %: 0,0→0,8 – je to záměr?), **NOVÁ-4** (digi bonus 45 ks – práh vs. násobky, ≥45 vs. přesně 45), **NOVÁ-5** (manažerský přepočet 1/10 příslibu + FZ body → %). Nesrovnalosti a uzavřené otázky beze změny (nic se nemaže, jen se doplňuje).
>
> **Změny ve v5 (odpovědi zadavatele):** uzavřeny **O3** (provize se počítá **lineárně i pro neúplné násobky báze** – např. objem 150 000 při bázi 100 000 → 1,5× sazba), **O8** (storno se odečítá **v kvartálu, kdy ke stornu došlo**; plnění tak může být i **záporné**; odečet u skupiny pod 80 % plánu nastává cca 1× za 2 roky, zadavatel **řeší ručně** – teď neřešíme), **O9** (rekonstrukce poboček / Area lead / FLE/FLET → **není třeba řešit** → N8 uzavřeno), **O11** (autoritativní zdroj paušálů za bod = **závazně karta motivace**), **O13** (mapování pozic – viz níže → N10 a N12 uzavřeny, N11 a N13 upřesněny). **O2** označena jako **neřešíme** (pro nápočet v tomto rozsahu nepodstatná; N6 ponecháno evidenčně). Otevřené / čekající na doplnění: **O7**.
>
> **Změny ve v4 (odpovědi zadavatele):** uzavřeny **O4** (11. skupina OTHER/Ostatní nemá plán → do zlatého pásma se počítá jen 10 plánovaných skupin), **O5** (skok koeficientu 0,9→1,1 je záměr, není chyba → N7 uzavřeno), **O6** (50 % se odečítá ze **všeho** – z provize i ze započteného kusu/objemu; do plnění plánu jde jen polovina), **O14** (potvrzeno LOANS = „Nezajištěné úvěry“, HYPO = „Zajištěné úvěry“ → N4 uzavřeno). **O10** = zatím ano (žádné další dodatky), potvrdí se na vyžádání. **O7** evidována, zadavatel dovysvětlí později. Otevřené a čekající na doplnění zadavatelem: **O2, O3, O8, O9, O11, O13** (v analýze upřesněno, na co přesně se ptáme).
>
> **Změny ve v3:** doplněn nadřazený předpis **`6202_10_01R.pdf` – „Bonusy pobočkové sítě a externího prodeje“** (účinnost 01.07.2025; skenované PDF – čteno přes OCR). Doplněno shrnutí (sekce 2.7); aktualizovány nesrovnalosti N3 (nomenklatura kritéria „Digitalizace“) a N11 (bonus pozice *retail regional lead* není tímto předpisem řešen → vysvětluje chybějící kartu); potvrzeny hodnoty příslibu 20 %/15 % a výplatní pravidla; upřesněny otevřené otázky O7, O11.
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
8. **Zlaté pásmo se počítá jen z 10 plánovaných skupin.** 11. skupina **OTHER / „Ostatní“ nemá plán**, do zlatého pásma (≥100 % v min. 8 skupinách) se tedy nezahrnuje (O4).
9. **Půlení obchodů (asistence / přesměrování / dělené příležitosti):** 50 % se odečítá **ze všeho** – z **provize** i ze **započteného kusu / započteného objemu**. Do plnění plánu tak jde jen polovina obchodu (O6).
10. **Koeficient plnění – skok 0,9 (90–99 %) → 1,1 (100–109 %) bez hodnoty 1,0 je záměr**, nikoli chyba (O5).
11. **Nomenklatura úvěrových skupin:** **LOANS = „Nezajištěné úvěry“**, **HYPO = „Zajištěné úvěry“** (O14).
12. **Nápočet provize je lineární** i pro neúplné násobky báze: provize = (objem / báze) × sazba, tj. objem 150 000 Kč při bázi 100 000 Kč → 1,5× sazba (O3).
13. **Storna:** odečet se provádí **v kvartálu, kdy ke stornu došlo** (ne v kvartálu sjednání). Plnění tak může být i **záporné**. Odečet u skupiny pod 80 % plánu je vzácný (cca 1× za 2 roky) a zadavatel jej **řeší ručně** – v nápočtu ho teď neřešíme (O8).
14. **Paušály za bod:** autoritativním zdrojem je **závazně karta motivace** (OBA 1 800, OBAS 2 200 …) – ne nominační listy / rozpis (O11).
15. **Mapování pozic pro nápočet (O13):**
    - **Manažeři:** platný je **kód z `positions.xml`** (tj. MMMT + MMM1/MMM2/MMM3), nikoli MMMA ze segmentového dokumentu.
    - **FLE/FLET:** pro nápočet **úplně ignorovat**.
    - **Servis:** brát **BKPJ = CAS = „Pokladník“** jako jednu pozici a **BKPM = OBAK = „OBAH“** jako jednu pozici.
    - **Bankéři:** rozdíly v kódech (OBAJ/OBAM/OBAP/OBAMa) zatím **ignorovat**.

## STAV VSTUPNÍCH PODKLADŮ

| Podklad | Stav |
|---|---|
| segmentovy_dokument_mma_2026_3q.pdf | k dispozici |
| metodika_zapocitavani_mma_2026_3q.xlsx | k dispozici |
| karta_motivace_mma_3q2026.pdf | k dispozici |
| provizni_list_mma_3q2026.pdf | k dispozici |
| **product_tree.xml** | **k dispozici** (103 produktů, 10 plánovaných skupin + OTHER) |
| **positions.xml** | **k dispozici** (114 pozic, z toho 15 v segmentu MMA) |
| **6202_10_01R.pdf** (nadřazený předpis „Bonusy pobočkové sítě a externího prodeje“) | **k dispozici** (6 stran, skenované PDF čteno přes OCR; účinnost 01.07.2025, verze „Aktuální“) |

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
| provizni_list_mma_3q2026.pdf | Provizní list | dle názvu souboru | dle názvu souboru | 1 strana, matice provizí |
| 6202_10_01R.pdf | **Nadřazený předpis** (bonusy pobočkové sítě a ext. prodeje) | napříč segmenty | účinnost od 01.07.2025 | 6 stran, skenované (OCR); rámcová pravidla, detaily odkazuje do segm. dokumentů |

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

### 2.7 6202_10_01R – Bonusy pobočkové sítě a externího prodeje (nadřazený předpis)
Rámcový předpis č. **6202 10 01R**, účinnost **01.07.2025**, verze „Aktuální“ (poslední změna 1. 7. 2025), autor Irena Melounová. Skenované PDF (6 stran), text získán přes OCR. Definuje společná pravidla bonusů pro pobočkovou síť a vybrané pozice externího prodeje; **detaily jednotlivých kritérií i segmentů odkazuje do segmentových dokumentů**.

**Klíčová pravidla / hodnoty:**
- **Rozsah:** týká se zaměstnanců OM a vybraných pozic externího prodeje. **Nezabývá se základními mzdami a bonusem pozice *retail regional lead*.** Do motivace za prodej jdou pouze produkty, u nichž lze identifikovat zaměstnance, který obchod sjednal (výjimka: digitální obchody na zařízení klienta bez asistence).
- **Bonusová kritéria (kap. 1.1):** Prodej/Poradenský prodej · Portfolio · Kvalita · Mimořádný bonus · Klientská spokojenost · **Digitalizace** · Akvizice · Finanční zdraví. Některá platí jen pro některé segmenty; složky bonusu jsou navzájem nezávislé.
- **Výplata:** čtvrtletně nebo pololetně dle typu pozice, se mzdou za měsíc následující po hodnoceném období → výplatní měsíce **leden, duben, červenec, říjen** (EPB o dva měsíce později). Bonus se vyplácí, je-li **≥ 100 Kč**. Bonus je nenárokovou složkou mzdy.
- **Krácení (kap. 1.2):** nekorektní jednání, neabsolvované povinné kurzy v AMOS, střet zájmů (produkt pro osoby blízké / pro sebe se nezapočítává). Kontrolní útvary 6610, 6620, 6940, 6950, 5030 01.
- **Rozpis plánů (kap. 2):** obchodní plány stanovuje útvar 5030 (tým 5030 03); rozpis na jednotlivce přes aplikaci; **Nominační listy** jsou klíčovým zdrojem dat pro výpočet bonusu (rozpis provádí manažer org. jednotky).
- **Příslib (kap. 4):** celkový roční příslib **20 %** roční základní mzdy u manažerských a prodejních pozic, **15 %** u podpůrných pozic (neplatí pro EPB a pozice externí prodejní sítě). Přísliby vycházejí z % váhy kritéria, u některých pozic pevnou částkou; **detaily v segmentových dokumentech**.
- **Zohlednění doby na pozici (kap. 4.9):** poměrné krácení při částečném úvazku, pracovní neschopnosti, nástupu/odchodu, přechodu mezi segmenty apod.
- **Odkazy/definice:** související předpis **6202.00.01R Mzdový řád**; definice EPB, OM (obchodní místo), ČS.

**Ověřené shody (pozitivní zjištění):**
- Roční příslib **20 % (prodej/manažeři) / 15 % (podpora)** sedí se segmentovým dokumentem (OBA/OBAS/…_pov/FLE 20 %; OBAH/Pokladník 15 %).
- Výplata čtvrtletně a **minimální hranice 100 Kč** sedí se segmentovým dokumentem.
- Kritérium se v nadřazeném předpisu jmenuje **„Digitalizace“** (kap. 1.1 a 4.6); pojem **„Servicing“ zde vůbec nefiguruje** (souvisí s N3/O7).

---

## 3. Report nesrovnalostí (aktivní)

| Č. | Typ | Dotčené dokumenty | Popis | Místo | Závažnost | Stav |
|---|---|---|---|---|---|---|
| N3 | Definiční | Segment. dok. ↔ Karta ↔ Nadřazený předpis | 4. kritérium OBAH: „Digitalizace“ (tab.) vs. „Servicing“ (text/karta). **Nadřazený předpis 6202_10_01R uvádí jako standardní kritérium „Digitalizace“ (kap. 1.1/4.6); „Servicing“ v něm nefiguruje** → název „Servicing“ v kartě/segmentu je nekonzistentní s nadřazeným předpisem. | seg. str. 3 vs. str. 8 / karta OBAH; 6202_10_01R kap. 1.1, 4.6 | střední | otevřené (O7) |
| N4 | Definiční (nomenklatura) | product_tree/provizní list/metodika ↔ segment. dok./karty | Oficiální názvy skupin jsou **„Úvěry“ (LOANS)** a **„Bydlení“ (HYPO)**, ale plánové tabulky v segm. dok. a kartách používají **„Nezajištěné úvěry“** a **„Zajištěné úvěry“**. **Zadavatel potvrdil mapování: LOANS = „Nezajištěné úvěry“, HYPO = „Zajištěné úvěry“ (O14).** Jde tedy jen o rozdílné labely téhož, ne o věcný rozpor. | product_tree; provizní list; metodika; seg. str. 4 | nízká | **uzavřeno (O14)** |
| N6 | Chybějící info | Provizní list ↔ ostatní | Sazba „s pojištěním“ vs. „bez“ (120/180) – podmínka uplatnění nikde nepopsána | provizní list, blok Úvěry/Bydlení | střední | neřešíme – dle zadavatele pro tento rozsah nepodstatné (O2) |
| N7 | Logická | Segment. dok. + karty | Skok koeficientu 0,9 (90–99 %) → 1,1 (100–109 %); chybí 1,0. **Zadavatel potvrdil, že jde o záměr (motivace „skočit“ přes 100 %), nikoli chybu (O5).** | seg. str. 4; karty | nízká | **uzavřeno – dle zadání záměr (O5)** |
| N8 | Úplnost | Segment. dok. | Rekonstrukce poboček neuvádí Area lead ani FLE/FLET | seg. str. 9 | nízká | **uzavřeno – dle zadavatele netřeba řešit (O9)** |
| N9 | Definiční (drobné) | Provizní list ↔ Metodika | Odlišné názvy/seskupení: Mobilita vs. Kodex mobility; Živ. poj. dvě sazby vs. jeden řádek | provizní list vs. metodika | nízká | otevřené |
| N10 | Pokrytí segmentu | positions.xml ↔ segment. dok./karty | **FLE/FLET nejsou v positions.xml** (v žádném segmentu), přestože segmentový dokument i karty popisují pozice Future LAB expert (FLE) a FLET pro MMA. **Zadavatel: FLE/FLET se pro nápočet úplně ignorují (O13)** → pro naši analýzu bezpředmětné. | positions.xml (MMA); seg. str. 15, karta str. 7–8 | vysoká | **uzavřeno – FLE/FLET ignorovat (O13)** |
| N11 | Definiční / pokrytí | positions.xml ↔ segment. dok. (kap. 1) ↔ nadřazený předpis | **Kolize kódů manažerských pozic.** Seg. dok.: MMMT = team lead, **MMMA = area lead**. positions.xml pro MMA má MMMT (mot=Manažer_MMA) + navíc **MMM1** (retail team lead), **MMM2** (retail area lead), **MMM3** (retail regional lead); **kód MMMA neexistuje**. **Chybějící karta pro „Regional lead“ je vysvětlena: nadřazený předpis 6202_10_01R se bonusem pozice *retail regional lead* výslovně nezabývá (kap. 1). Zadavatel: manažeři se řídí kódem z `positions.xml` (MMMT + MMM1/2/3), MMMA se nepoužívá (O13).** | positions.xml; seg. str. 1, str. 17; 6202_10_01R kap. 1 | vysoká | **uzavřeno – platí kódy z positions.xml (O13)** |
| N12 | Definiční | positions.xml ↔ segment. dok. (kap. 1) | **Servisní pozice nekonzistentní.** Seg. dok.: BKPJ = „Pokladník“, BKPM = „OBAH“. positions.xml má navíc **CAS** (Pokladník) a **OBAK** (Bankéř klientské péče, mot=OBAH), přičemž řádky **BKPJ i BKPM mají v popisu shodně „OBAH“**. **Zadavatel: pro analýzu brát BKPJ = CAS = „Pokladník“ jako jednu pozici a BKPM = OBAK = „OBAH“ jako jednu pozici (O13).** | positions.xml; seg. str. 1 | střední | **uzavřeno – sloučení pozic dle O13** |
| N13 | Definiční | positions.xml ↔ segment. dok. (kap. 1) | Motivační kódy nesouhlasí se seskupením v seg. dok. Seg. dok.: OBAJ/OBAM = „OBA“, OBAS/OBAMa = „OBAS“. positions.xml: OBAJ (mot=OBAJ), OBAM (mot=OBAM) – **negrupováno**; navíc **OBAP** (Osobní bankéř Plus) neuvedený v seg. dok., a **OBAMa (master)** ze seg. dok. v positions.xml chybí. **Zadavatel: rozdíly u bankéřů zatím ignorovat (O13).** | positions.xml; seg. str. 1 | střední | odloženo – dle zadavatele zatím ignorovat (O13) |

---

## 4. Otevřené otázky (register – opakuje se, dokud nezavřeme)

**Uzavřené:** segment/období z názvu · Mass Affluent = Mass Market · sjednaný vs. započtený objem · reference data (odloženo) · **O1 mapování produkt→skupina→jednotka (product_tree.xml)** · product_tree.xml (dodán) · pilot „Úvěry“ (skončil → ignorovat) · **6202_10_01R (nadřazený předpis dodán)** · **O4 (11. skupina OTHER nemá plán – zlaté pásmo počítá jen 10 plánovaných skupin)** · **O5 (skok koeficientu 0,9→1,1 je záměr, ne chyba → N7)** · **O6 (50 % se odečítá ze všeho – provize i započtený kus/objem; do plnění plánu jde jen polovina)** · **O10 (zatím finální, žádné dodatky – potvrdí se na vyžádání)** · **O14 (LOANS=„Nezajištěné úvěry“, HYPO=„Zajištěné úvěry“ → N4)** · **O3 (provize lineárně i pro neúplné násobky báze)** · **O8 (storno se odečítá v Q storna; plnění může být záporné; skupina pod 80 % ~1× za 2 roky → řeší se ručně)** · **O9 (rekonstrukce/Area lead/FLE/FLET → netřeba řešit → N8)** · **O11 (paušály za bod závazně z karty motivace)** · **O13 (mapování pozic: manažeři dle positions.xml; FLE/FLET ignorovat; servis BKPJ=CAS=Pokladník a BKPM=OBAK=OBAH; bankéři zatím ignorovat → N10/N12)**.
**Neřešíme (dle zadavatele nepodstatné):** **O2 (podmínka sazby „s pojištěním“ vs. „bez“) – N6 ponecháno evidenčně.**

**Legenda stavů:** ⏳ *čeká na dovysvětlení zadavatelem* · 🅴 *evidováno, zadavatel doplní později*.

| ID | Otázka | Proč | Stav |
|---|---|---|---|
| O7 | „Digitalizace“ vs. „Servicing“ (OBAH) – závazný název 4. kritéria (nadř. předpis uvádí „Digitalizace“) | definiční (N3) | 🅴 evidováno, zadavatel doplní později |
| NOVÁ-1 | Jak se chová **koeficient plnění při záporném plnění** (storno)? Pásma jsou definována jen od „<80 % → 0,0“ výš; není popsáno chování pod 0 %. Koeficient 0,0 fakticky vynuluje storno penalizaci. | logická (souvisí O8) | ⏳ k doptání |
| NOVÁ-2 | **Aplikace zlatého pásma ×1,2** vs. základní koeficient (např. 1,1 v pásmu 100–109 %): v jakém pořadí, na jakém agregátu (per skupina vs. celkově) a zda multiplikativně? | logická | ⏳ k doptání |
| NOVÁ-3 | **Cliff na hranici 80 %** (skok 0,0 → 0,8): je to záměr stejně jako potvrzený skok 0,9→1,1 (O5)? | logická (souvisí N7/O5) | ⏳ k doptání |
| NOVÁ-4 | **Digi bonus „+45 ks = 800 Kč“**: jednorázový práh, nebo násobky? A hranice „≥45“, nebo „přesně 45“? | definiční | ⏳ k doptání |
| NOVÁ-5 | **Manažerský přepočet** „1/10 příslibu + převod bodů FZ na %“: přesná mechanika a pořadí kroků. | výpočetní | ⏳ k doptání |

---

## 5. BA review (v6) – pohled byznys analytika

Analytické shrnutí nad celou dokumentací bonusů MMA. Členěno do tří otázek: *co nedává smysl*, *co si protiřečí*, *co lze zjednodušit*. Slouží jako podklad pro doptání zadavatele (viz nové otázky NOVÁ-1 až NOVÁ-5 v sekci 4).

### 5.1 Co nedává smysl (logické / návrhové otazníky)

1. **Záporné plnění vs. koeficientová pásma.** Dle O8 se storno odečítá v kvartálu storna a plnění může být **záporné**. Koeficient plnění je ale definován jen od „<80 % → 0,0“ výš – chybí definice chování v záporném pásmu. Koeficient 0,0 přitom fakticky vynuluje storno penalizaci (do plnění plánu). → **NOVÁ-1**.
2. **Interakce zlatého pásma se základním koeficientem.** Zlaté pásmo dává ×1,2 a zároveň základní koeficient v pásmu 100–109 % je 1,1. Není jednoznačné pořadí, agregát (per skupina vs. celkově) ani zda se násobí multiplikativně. → **NOVÁ-2**.
3. **Cliff na hranici 80 %.** Skok 0,0 (<80 %) → 0,8 (80–89 %) je větší útes než potvrzený záměrný skok 0,9→1,1. U hranice 80 % záměr potvrzen není. → **NOVÁ-3**.
4. **Digi bonus „+45 ks = 800 Kč“.** Není jasné, zda jde o jednorázový práh nebo o násobky, a zda je hranice „≥45“ nebo „přesně 45“. → **NOVÁ-4**.
5. **FLE/FLET „duchové“.** Segmentový dokument i karta popisují pozice FLE/FLET (váhy 30/70, přesměrování), ale v `positions.xml` neexistují a dle O13 se ignorují. Dokumentace tedy nese pravidla pro pozice, které se reálně nenapočítávají.

### 5.2 Co si protiřečí (rozpory mezi dokumenty)

6. **„Digitalizace“ vs. „Servicing“ (OBAH, 4. kritérium)** – nadřazený předpis zná jen „Digitalizace“, karta/segment „Servicing“. Neuzavřeno (N3 / **O7**).
7. **Kódy manažerských pozic** – seg. dok. `MMMA` (area lead) vs. `positions.xml` `MMM1/2/3`; `MMMA` neexistuje. Vyřešeno dohodou (O13), ale rozpor v seg. dokumentu zůstává jako dokumentační dluh (N11).
8. **Servisní pozice** – `BKPJ`/`BKPM` vs. `CAS`/`OBAK`, `BKPJ` i `BKPM` mají v popisu shodně „OBAH“. Vyřešeno sloučením (O13), stále jde o rozpor mezi zdroji (N12).
9. **Bankéřské kódy** – `OBAJ/OBAM/OBAP/OBAMa`: neseskupené, `OBAP` navíc, `OBAMa` chybí. Dle O13 zatím ignorovat → rozpor odložen, ne vyřešen (N13).
10. **Nomenklatura skupin** – „Úvěry/Bydlení“ vs. „Nezajištěné/Zajištěné úvěry“. Vyřešeno mapováním (O14), ale trvalý zdroj záměny při čtení.
11. **Provizní list vs. metodika – drobné** – „Mobilita“ vs. „Kodex mobility“; životní pojištění dvě sazby (list) vs. jeden řádek (metodika). Otevřené (N9).

### 5.3 Co je zbytečně složité a šlo by zjednodušit

12. **Odměna OBAH je mimořádně členitá** – paušál za bod 700 + paušál za prodej 400/skupinu + dvě samostatné třístupňové škály (Podpora; Servicing s prahem 20 operací) + váhy 25/25/25/25. Kandidát na sjednocení mechaniky.
13. **Různé báze napříč produkty** – objem se počítá jednou /100 000, jindy /1 000. Smíšené báze zvyšují chybovost nápočtu; pomohla by sjednocená báze nebo explicitní tabulka báze na produkt.
14. **Sazba „s pojištěním“ vs. „bez“ (120/180) bez definice podmínky** (N6 / O2 „neřešíme“) – z pohledu nápočtu reálná díra, vhodné držet evidenčně živé.
15. **Manažerský přepočet** „1/10 příslibu + převod bodů FZ na %“ – jiná mechanika než u ostatních pozic (body → paušál), vyžaduje samostatný výpočetní blok. → **NOVÁ-5**.

> Pozn.: Sekce 5 pouze popisuje a navrhuje otázky k doptání; **neupravuje** pravidla ani dokumenty (v souladu se zásadami práce).
