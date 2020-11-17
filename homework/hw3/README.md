# HW3: Experimentální hodnocení kvality algoritmů

## Prerequisites

* python3

## Struktura projektu

    bin/
        Bash scripty pro získávání optimálních řešení a měření.

    data/
        Vstupní datové sady vygenerované pomocí generátoru instancí problému batohu.
        
    kg2/
        Generátor instancí problému batohu.
        
    results/
        Výsledky běhu programu (algoritmů).
        
    src/
        Zdrojový kód řešení algoritmů a skriptů pro transformaci výsledků běhu programu.
        

## Příklady volání generátoru

	./kg2 -n 10 -N 200 -m 0.8 -W 200 -w bal -C 1000 -c uni -k 1
	./kg2/gen/kg2 -n 30 -N 500 -m 0.8 -W 300 -w bal -C 2000 -c uni -k 1 > data/normal/normal10_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.2 -W 300 -w heavy -C 2000 -c corr -k 1 > data/normal/normal25_inst.dat
    
## Pilotní testování závislostí

### Branch & Bound

#### Závislost výpočetního času na poměru kapacity batohu k sumární váze

**Hypotéza**  
Předpokládejme, že pro poměr kapacity batohu k sumární váze v intervalu $[0.0, 0.5]$ bude při rostoucím poměru růst rovněž výpočetní čas. Dále předpokládejme, že pro poměr v intervalu $(0.5, 1.0]$ bude výpočetní čas klesat. Hypotéza je založena na myšlence, že pokud je poměr v intervalu $[0.0, 0.5]$, dochází s klesajícím poměrem k většímu ořezávání shora (na základě překročení kapacity batohu), resp. pokud je poměr v intervalu $(0.5, 1.0]$, dochází s rostoucím poměrem k většímu ořezávání zdola (stávající řešení nemůže být lepší než nejlepší dosud nalezené).

PILOTNĚ POTVRZENO

**Vlastnosti datových sad:**
* Počet instancí: 500
* Poměr kapacity batohu k sumární váze: {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9}
* Maximální váha věcí: 300
* Vyvážené rozložení vah
* Maximální cena: 1500
* Menší korelace váha:cena
* Exponent granuality 1

##### Příklad generování dat pilotního testu
    
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.05 -W 300 -C 1500 -c corr > data/m005/m005_25_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.1 -W 300 -C 1500 -c corr > data/m01/m01_25_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.2 -W 300 -C 1500 -c corr > data/m02/m02_25_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.3 -W 300 -C 1500 -c corr > data/m03/m03_25_inst.dat

### Greedy heuristika

#### Závislost chyby na granularitě

**Hypotéza**  
Mějme batoh s kapacitou relativně nízkou vůči sumární váze předmětů. Dále měníme granularitu předmětů směrem dolů (tedy dostáváme stále menší předměty - předměty s nižší vahou). Předpokládejme, že chyba heuristiky bude klesat.

PILOTNĚ POTVRZENO

**Vlastnosti datových sad:**
* Počet instancí: 500
* Poměr kapacity batohu k sumární váze: 0.2
* Maximální váha věcí: 300
* Převaha lehkých věcí
* Maximální cena: 1500
* Žádná korelace váha:cena
* Exponent granularity k: {1, 5, 10, 50, 100, 200, 300}

**Získání optimálních řešení**  
Díky -m 0.2 lze rychle získat výsledky za využití Branch&Bound (viz předchozí závislost).

**Pozn.:**  
S jinými vlastnostmi tato závislost neplatí !!!

##### Příklad generování dat pilotního testu

    ./kg2/gen/kg2 -n 22 -N 500 -m 0.2 -W 300 -w light -C 1500 -k 50 > data/k5/k5_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -m 0.2 -W 300 -w light -C 1500 -k 100 > data/k60/k60_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -m 0.2 -W 300 -w light -C 1500 -k 200 > data/k120/k120_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -m 0.2 -W 300 -w light -C 1500 -k 300 > data/k180/k180_22_inst.dat

#### Závislost chyby na poměru kapacity batohu k sumární váze

**Hypotéza**  
Předpokládejme, že s rostoucím poměrem kapacity batohu vůči sumární váze předmětů bude chybovost heuristiky klesat. Hypotéza je založena na myšlence, že na konci pole předmětů seřazeného dle poměru $\frac{C_i}{m_i}$ zbude méně předmětů tvořících případnou chybu heuristiky.

PILOTNĚ POTVRZENO

**Vlastnosti datových sad:**
* Počet instancí: 500
* Poměr kapacity batohu k sumární váze: {0.1 0.2 0.4 0.8 1.0}
* Maximální váha věcí: 300
* Převaha těžkých věcí
* Maximální cena: 1500
* Žádná korelace váha:cena
* Exponent granularity: 1

##### Příklad generování dat pilotního testu

    ./kg2/gen/kg2 -n 22 -m 0.1 -N 500 -W 300 -w heavy -C 1500 > data/gm01/gm01_22_inst.dat
    ./kg2/gen/kg2 -n 22 -m 0.2 -N 500 -W 300 -w heavy -C 1500 > data/gm02/gm02_22_inst.dat
    ./kg2/gen/kg2 -n 22 -m 0.4 -N 500 -W 300 -w heavy -C 1500 > data/gm04/gm04_22_inst.dat
    ./kg2/gen/kg2 -n 22 -m 0.8 -N 500 -W 300 -w heavy -C 1500 > data//gm08/gm08_22_inst.dat
    ./kg2/gen/kg2 -n 22 -m 1.0 -N 500 -W 300 -w heavy -C 1500 > data/gm1/gm1_22_inst.dat

### Dynamické programování

#### Závislost výpočetního času na maximální ceně

**Hypotéza**  
Mějme silnou korelaci váhy s cenou. Předpokládejme, že s rostoucí maximální cenou poroste výpočetní čas DP. Hypotéza je založena na skutečnosti, že vyšší maximální cena předmětů povede na vyšší sumární váhu $C_M$, což povede na vyšší složitost, jelikož $C_M$ vystupuje jako činitel v asymptotické složitosti DP při dekompozici dle ceny ($O(n^2 C_M)$).

PILOTNĚ POTVRZENO

**Vlastnosti datových sad:**
* Počet instancí: 500
* Poměr kapacity batohu k sumární váze: 0.8
* Maximální váha věcí: 300
* Vyvážené věci
* Maximální cena: {100, 500, 1500, 4000}
* Silná korelace váha:cena
* Exponent granularity: 1  

##### Příklad generování dat pilotního testu

    ./kg2/gen/kg2 -n 22 -N 500 -W 300 -C 100 -c strong > data/C100/C100_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -W 300 -C 500 -c strong > data/C500/C500_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -W 300 -C 1500 -c strong > data/C1500/C1500_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -W 300 -C 4000 -c strong > data/C4000/C4000_22_inst.dat

