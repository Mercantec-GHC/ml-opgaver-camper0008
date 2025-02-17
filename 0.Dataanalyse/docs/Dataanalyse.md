# Dataanalyse

Inden vi begynder på det store emne som er Machine Learning, vil jeg gerne have at I laver følgende 4 opgave sæt! Hele første dag af Machine Learning kurset er til at lave følgende opgaver, når man ikke dem alle er det okay, men på dag 2 går vi videre til linær regression.

### PIP - Installering af pakker

```bash
# Installering af pakker manuelt
pip install numpy pandas matplotlib
# Eller hvis I har en requirements.txt fil
pip install -r requirements.txt
```

Til større projekter, anbefaler jeg at I bruger et virtuelt miljø, som I kan installere pakkerne i. Der er en kort guide længere nede i dokumentet.

## NumPy

NumPy er et fundamentalt Python-bibliotek, der bruges til videnskabelig computing og dataanalyse. Det giver en effektiv måde at oprette og manipulere arrays, som er essentielle datastrukturer i maskinlæring. NumPy arrays kan være en- eller flerdimensionelle og bruges til at repræsentere data i rækker og kolonner, ligesom i en SQL-database.

### Læringsmål

1. **Forståelse af NumPy Arrays:**

   - Lær at oprette og manipulere NumPy arrays.
   - Forskellen mellem Python lister og NumPy arrays.

2. **Grundlæggende Array Operationer:**

   - Opret arrays med specifikke værdier ved hjælp af `np.array`.
   - Generer arrays med sekvenser af tal ved hjælp af `np.arange`.
   - Udfyld arrays med tilfældige tal ved hjælp af `np.random`.

3. **Matematiske Operationer:**

   - Udfør elementvise operationer på arrays.
   - Anvend broadcasting til at udføre operationer på arrays med forskellige dimensioner.

4. **Praktiske Opgaver:**
   - Opret et lineært datasæt ved hjælp af NumPy.
   - Tilføj tilfældig støj til datasæt for at simulere realistiske data.

Disse opgaver vil give en grundlæggende forståelse af NumPy, som er nødvendig for at kunne anvende det i maskinlæringsprojekter. NumPy's effektivitet og fleksibilitet gør det til et uundværligt værktøj i dataanalyse og videnskabelig computing.

## Pandas

Pandas er et kraftfuldt Python-bibliotek til dataanalyse og manipulation. Det tilbyder datastrukturer og operationer til at manipulere numeriske tabeller og tidsseriedata. Den centrale datastruktur i Pandas er DataFrame, som ligner en tabel i en database eller et regneark.

### Læringsmål

1. **Forståelse af Pandas DataFrames:**

   - Lær at oprette og manipulere DataFrames.
   - Forstå forskellen mellem NumPy arrays og Pandas DataFrames.

2. **Grundlæggende DataFrame Operationer:**

   - Opret DataFrames fra NumPy arrays og Python lister.
   - Tilføj nye kolonner til eksisterende DataFrames.
   - Isoler specifikke rækker, kolonner eller celler i en DataFrame.

3. **Avancerede DataFrame Operationer:**

   - Kopier DataFrames ved hjælp af referencer og ægte kopier.
   - Forstå forskellen mellem at pege på samme hukommelsesplads og at lave en ny kopi.

4. **Praktiske Opgaver:**
   - Opret en DataFrame med tilfældige data.
   - Tilføj en ny kolonne baseret på beregninger fra eksisterende kolonner.

Disse opgaver vil give en grundlæggende forståelse af Pandas, som er nødvendig for at kunne anvende det i dataanalyseprojekter. Pandas' fleksibilitet og brugervenlighed gør det til et uundværligt værktøj i dataanalyse og videnskabelig computing.

## Matplotlib

Matplotlib er et omfattende bibliotek til at skabe statiske, animerede og interaktive visualiseringer i Python. Det er et vigtigt værktøj til at visualisere data og resultater i dataanalyse og maskinlæring.

### Læringsmål

1. **Grundlæggende Plotting:**

   - Lær at oprette simple plots som linje- og søjlediagrammer.
   - Forstå hvordan man tilpasser akser, titler og etiketter.

2. **Avancerede Visualiseringer:**

   - Opret scatter plots og histogrammer.
   - Brug subplots til at vise flere plots i én figur.

3. **Tilpasning og Stil:**

   - Anvend forskellige stilarter og temaer til plots.
   - Tilpas farver, linjetyper og markører.

4. **Interaktivitet:**
   - Implementer interaktive elementer som zoom og pan.
   - Brug Matplotlib's widgets til at tilføje interaktive kontroller.

## DataOpgaver

### Opgaveoversigt

1. **Simulering af Møntkast og Statistisk Analyse**

   - **Beskrivelse:** Simuler et stort antal møntkast, analyser resultaterne statistisk, og visualiser sandsynligheden for udfald.
   - **Sværhedsgrad:** Let
   - **Detaljer:** Denne opgave fokuserer på at skrive en simpel Python-funktion til simulering og anvende grundlæggende statistiske principper. Det er en god introduktion til simulering og sandsynlighedsberegning.

2. **Analyser og visualiser data for politistop**

   - **Beskrivelse:** Rens og forbered data ved hjælp af Pandas, analyser aldersgrupper og køns- og racefordeling, og visualiser resultaterne med Matplotlib.
   - **Sværhedsgrad:** Mellem
   - **Detaljer:** Denne opgave kræver en forståelse af dataforberedelse, analyse og visualisering. Det involverer flere trin, herunder datarensning, beregning af aldersgrupper, og oprettelse af forskellige diagrammer.

3. **Porteføljeoptimering og Analyse af S&P 500 Aktier**
   - **Beskrivelse:** Analyser historiske aktiedata, design en portefølje, og beregn afkastet over en 10-årig periode.
   - **Sværhedsgrad:** Avanceret
   - **Detaljer:** Denne opgave kræver en dybere forståelse af finansiel analyse, datahåndtering, og strategisk porteføljedesign. Det involverer normalisering af data, visualisering, og implementering af en investeringsstrategi.

Disse opgaver er designet til at give praktisk erfaring med dataanalyse, simulering, og finansiel analyse ved hjælp af Python og dets biblioteker.

## Opsætning af Virtuelt Miljø i Python

#### Opsætning med Windows (CMD/Powershell)

```bash
python -m venv myenv
myenv\Scripts\activate # Windows
pip install numpy pandas matplotlib
deactivate # For at deaktivere miljøet
```

#### Opsætning med Linux/MacOS

```bash
python3 -m venv myenv
source myenv/bin/activate # Linux/MacOS
pip install numpy pandas matplotlib
deactivate # For at deaktivere miljøet
```

Hvis I skal bruge jeres venv i Jupyter Notebook, så skal I starte Jupyter Notebook med følgende kommando:

```bash
jupyter notebook --notebook-dir=myenv/Scripts
```

Eller opsætte Jupyter Notebook i jeres venv:

```bash
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```
