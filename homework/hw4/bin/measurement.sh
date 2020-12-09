#!/bin/bash

# Slowing SA cooling (changing cooling rate) and changing equilibrium length
python3 ./../src/main.py 'NK' 32 1000 0.5 0.1 2 1
python3 ./../src/main.py 'NK' 32 1000 0.5 0.1 4 1
python3 ./../src/main.py 'NK' 32 1000 0.5 0.1 6 1
python3 ./../src/main.py 'NK' 32 1000 0.9 0.1 2 1
python3 ./../src/main.py 'NK' 32 1000 0.9 0.1 4 1
python3 ./../src/main.py 'NK' 32 1000 0.9 0.1 6 1
python3 ./../src/main.py 'NK' 32 1000 0.95 0.1 2 1
python3 ./../src/main.py 'NK' 32 1000 0.95 0.1 4 1
python3 ./../src/main.py 'NK' 32 1000 0.95 0.1 6 1
python3 ./../src/main.py 'NK' 32 1000 0.995 0.1 2 1
python3 ./../src/main.py 'NK' 32 1000 0.995 0.1 4 1
python3 ./../src/main.py 'NK' 32 1000 0.995 0.1 6 1
