#!/bin/bash

# Measure avg statistics (time and relative error)
# Slowing SA cooling (changing cooling rate) and changing equilibrium length
python3 ./../src/main.py 'NK' 32 1000 0.5 1 1 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.5 1 2 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.5 1 4 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.9 1 1 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.9 1 2 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.9 1 4 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.95 1 1 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.95 1 2 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.95 1 4 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.995 1 1 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.995 1 2 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.995 1 4 1 500 0

# Measure SA error evolving in runtime on picked instances
#python3 ./../src/main.py 'NK' 32 1000 0.5 1 1 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.5 1 2 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.5 1 4 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.9 1 1 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.9 1 2 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.9 1 4 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.95 1 1 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.95 1 2 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.95 1 4 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.995 1 1 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.995 1 2 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.995 1 4 1 1 1