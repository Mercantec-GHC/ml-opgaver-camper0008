# 1. Regression

## 1.1 Simpel Lineær Regression med Syntetiske Data

I denne første del udforsker vi lineær regression med et simpelt datasæt for at forstå de grundlæggende koncepter.

### Læringsmål

Efter at have gennemført denne øvelse, vil du kunne:

- Tilpasse følgende hyperparametre:
  - Læringsrate (learning rate)
  - Antal epoker (epochs)
  - Batchstørrelse (batch size)
- Fortolke forskellige typer af tabskurver (loss curves)

### Nøglekoncepter

- Modellen trænes ved hjælp af TensorFlow/Keras
- Vi bruger et syntetisk datasæt med 12 eksempler
- Vi visualiserer resultaterne med matplotlib
- Vi eksperimenterer med forskellige hyperparametre for at optimere modellen

### Praktiske Opgaver

1. Undersøg graferne og identificer hvordan modellen tilpasser sig data
2. Eksperimenter med antal epoker for at opnå konvergens
3. Undersøg effekten af forskellige læringsrater
4. Find den optimale kombination af epoker og læringsrate
5. Eksperimenter med forskellige batchstørrelser

### Vigtige Observationer

- For høj læringsrate kan føre til ustabil træning
- For få epoker kan resultere i undertilpasning
- Batchstørrelsen påvirker træningshastighed og stabilitet

For mere detaljeret teori og baggrund, se [Notion Regression](https://www.notion.so/mercantec/Machine-Learning-e89a2baf0d414172b13d07465366482e?pvs=4#cceeafe8d5b9432d8709b1329caf6969).

# 1.2 Simple Linear Regression: Forudsige brændstofforbrug

I denne del arbejder vi med:

- Auto MPG datasættet til at forudsige brændstofeffektivitet
- Implementering af både lineære modeller og neurale netværk
- Træning af modeller med forskellige input-kombinationer
- Evaluering og sammenligning af modellernes ydeevne

# 1.3 Anvendelse af Regressionsværktøjer på Aktiedata

I denne opgave skal I anvende jeres viden om regression til at analysere og forudsige aktiepriser. Herunder finder I en guide til at komme i gang.

## 1. Dataforberedelse

- Vælg en aktie I er interesserede i (behøver ikke være Microsoft)
- Anvend `yfinance` til at hente historiske data
- Opdel jeres data i trænings- og testsæt (typisk 80/20 fordeling)

## 2. Feature Engineering

- Overvej hvilke features der kunne være relevante:
  - Glidende gennemsnit over forskellige perioder
  - Daglige prisændringer
  - Handelsvolumen
  - Tidligere dages priser som input

## 3. Modelopbygning

Brug teknikkerne fra de tidligere øvelser:

- Start med en simpel lineær regression
- Eksperimenter med forskellige hyperparametre:
  - Læringsrate (learning rate)
  - Antal epoker (epochs)
  - Batchstørrelse (batch size)

## 4. Evaluering

- Visualiser resultaterne med plots
- Sammenlign forudsigelser med faktiske værdier
- Beregn relevante fejlmål (MSE, MAE)

## 5. Eksperimenter

- Test forskellige tidsperioder
- Afprøv forskellige kombinationer af features
- Sammenlign forskellige aktier

## Vigtige bemærkninger

- Formålet er ikke at udvikle en perfekt handelsmodel
- Fokuser på at anvende regressionsværktøjerne korrekt
- Dokumentér jeres observationer og resultater
- Eksperimenter med forskellige tilgange

## Tips

- Start simpelt og byg gradvist mere kompleksitet ind
- Brug visualiseringer til at forstå jeres data
- Sammenlign forskellige modelkonfigurationer
- Husk at validere jeres resultater

God arbejdslyst med opgaven!
