# HW3

## Příklady volání generátoru

	./kg2 -n 10 -N 200 -m 0.8 -W 200 -w bal -C 1000 -c uni -k 1
	./kg2/gen/kg2 -n 30 -N 500 -m 0.8 -W 300 -w bal -C 2000 -c uni -k 1 > data/normal/normal10_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.2 -W 300 -w heavy -C 2000 -c corr -k 1 > data/normal/normal25_inst.dat
    
## Pilotní testování závislostí

### Branch & Bound

#### Závislost výpočetního času na poměru kapacity batohu k sumární váze

Hypotéza: Čím nižší bude poměr kapacity bahotu k sumární váze, tím nižší výpočetní čas (ořezávání shora dle hmotnosti).

-> POTVRZENO

Vlastnosti:
* Počet instancí: 500
* Proměnný poměr kapacity batohu k sumární váze
* Maximální váha věcí: 300
* Vyvážené rozložení vah
* Maximální cena: 1500
* Menší korelace váha:cena
* Exponent granuality 1

##### Generování dat pilotního testu

    ./kg2/gen/kg2 -n 25 -N 500 -m 0.05 -W 300 -w heavy -C 1500 -c corr > data/m005/m005_25_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.1 -W 300 -w heavy -C 1500 -c corr > data/m01/m01_25_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.2 -W 300 -w heavy -C 1500 -c corr > data/m02/m02_25_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.3 -W 300 -w heavy -C 1500 -c corr > data/m03/m03_25_inst.dat
    
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.05 -W 300 -C 1500 -c corr > data/m005/m005_25_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.1 -W 300 -C 1500 -c corr > data/m01/m01_25_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.2 -W 300 -C 1500 -c corr > data/m02/m02_25_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.3 -W 300 -C 1500 -c corr > data/m03/m03_25_inst.dat

### Greedy heuristika

#### Závislost chyby na granularitě

Hypozéta: Závislost chyby heuristiky na granularitě při těžkých předmětech a nízké kapacitě batohu vůči sumě vah.

-> POTVRZENO

Vlastnosti:
* Počet instancí: 500
* Poměr kapacity batohu k sumární váze: 0.2
* Maximální váha věcí: 300
* Převaha těžkých věcí
* Maximální cena: 1500
* Žádná korelace váha:cena
* Proměnný exponent granularity k

Díky -m 0.1 lze rychle získat výsledky za využití Branch&Bound (viz předchozí závislost).

S jinými vlastnostmi tato závislost neplatí !!!

    ./kg2/gen/kg2 -n 22 -N 500 -m 0.1 -W 300 -w heavy -C 1500 -k 5 > data/k5/k5_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -m 0.1 -W 300 -w heavy -C 1500 -k 60 > data/k60/k60_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -m 0.1 -W 300 -w heavy -C 1500 -k 120 > data/k120/k120_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -m 0.1 -W 300 -w heavy -C 1500 -k 180 > data/k180/k180_22_inst.dat

#### Závislost chyby na poměru kapacity batohu k sumární váze

Hypotéza: S rostoucí relativní kapacitou batohů vůči sumární váze by měla klesat chybovost heuristiky.

-> POTVRZENO

Vlastnosti:
* Počet instancí: 500
* Proměnný poměr kapacity batohu k sumární váze
* Maximální váha věcí: 300
* Převaha těžkých věcí
* Maximální cena: 1500
* Žádná korelace váha:cena
* Exponent granularity: 1 


    ./kg2/gen/kg2 -n 22 -m 0.1 -N 500 -W 300 -w heavy -C 1500 > data/gm01/gm01_22_inst.dat
    ./kg2/gen/kg2 -n 22 -m 0.2 -N 500 -W 300 -w heavy -C 1500 > data/gm02/gm02_22_inst.dat
    ./kg2/gen/kg2 -n 22 -m 0.4 -N 500 -W 300 -w heavy -C 1500 > data/gm04/gm04_22_inst.dat
    ./kg2/gen/kg2 -n 22 -m 0.8 -N 500 -W 300 -w heavy -C 1500 > data//gm08/gm08_22_inst.dat
    ./kg2/gen/kg2 -n 22 -m 1.0 -N 500 -W 300 -w heavy -C 1500 > data/gm1/gm1_22_inst.dat

### Dynamické programování

#### Závislost výpočetního času na maximální ceně

Hypotéza: Mějme silnou korelaci váhy s cenou. S rostoucí maximální cenou roste výpočetní čas DP.

-> POTVRZENO

Vlastnosti:
* Počet instancí: 500
* Poměr kapacity batohu k sumární váze: 0.8
* Maximální váha věcí: 300
* Vyvážené věci
* Proměnná maximální cena
* Silná korelace váha:cena
* Exponent granularity: 1  


    ./kg2/gen/kg2 -n 22 -N 500 -W 300 -C 200 -c strong > data/k5/k5_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -W 300 -C 400 -c strong > data/k60/k60_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -W 300 -C 800 -c strong > data/k120/k120_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -W 300 -C 1600 -c strong > data/k180/k180_22_inst.dat
