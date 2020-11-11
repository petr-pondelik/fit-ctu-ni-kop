# HW3

## Příklady volání generátoru

	./kg2 -n 10 -N 200 -m 0.8 -W 200 -w bal -C 1000 -c uni -k 1
	./kg2/gen/kg2 -n 30 -N 500 -m 0.8 -W 300 -w bal -C 2000 -c uni -k 1 > data/normal/normal10_inst.dat
    ./kg2/gen/kg2 -n 25 -N 500 -m 0.2 -W 300 -w heavy -C 2000 -c corr -k 1 > data/normal/normal25_inst.dat
    
## Pilotní testování závislostí

### Dynamické programování

Závislost výpočetního času na maximální ceně.

Vlastnosti:
* Max W = max C
* balanced W
* silná korelace C:W

Volíme několik hodnot max C.

### Branch & Bound

#### Závislost výpočetního času na poměru kapacity batohu k sumární váze.

Čím nižší bude poměr kapacity bahotu k sumární váze, tím nižší výpočetní čas (ořezávání shora dle hmotnosti).

Vlastnosti:
* Počet instancí = 500
* Proměnný poměr kapacity batohu k sumární váze
* Maximální váha věcí: 300
* Menší korelace váha:cena
* Maximální váha = 2000
* Vyvážené rozložení vah
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

#### Závislost výpočetního času na granularitě

Závislost chyby heuristiky na granularitě při těžkých předmětech? -> Potvrzeno

    ./kg2/gen/kg2 -n 22 -N 500 -m 0.1 -W 300 -w heavy -C 1500 -k 5 > data/k5/k5_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -m 0.1 -W 300 -w heavy -C 1500 -k 60 > data/k60/k60_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -m 0.1 -W 300 -w heavy -C 1500 -k 120 > data/k120/k120_22_inst.dat
    ./kg2/gen/kg2 -n 22 -N 500 -m 0.1 -W 300 -w heavy -C 1500 -k 180 > data/k180/k180_22_inst.dat
