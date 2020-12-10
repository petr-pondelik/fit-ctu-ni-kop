#!/bin/bash

# Measure with accepted freeze implementation

# Measure avg statistics (time and relative error)
# Slowing SA cooling (changing cooling rate) and changing equilibrium length
#python3 ./../src/main.py 'NK' 32 1000 0.5 'accepted' 1 1 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.5 'accepted' 1 2 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.5 'accepted' 1 4 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.9 'accepted' 1 1 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.9 'accepted' 1 2 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.9 'accepted' 1 4 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.95 'accepted' 1 1 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.95 'accepted' 1 2 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.95 'accepted' 1 4 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.995 'accepted' 1 1 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.995 'accepted' 1 2 1 500 0
#python3 ./../src/main.py 'NK' 32 1000 0.995 'accepted' 1 4 1 500 0
#
## Measure SA error evolving in runtime on picked instances
#python3 ./../src/main.py 'NK' 32 1000 0.5 'accepted' 1 1 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.5 'accepted' 1 2 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.5 'accepted' 1 4 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.9 'accepted' 1 1 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.9 'accepted' 1 2 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.9 'accepted' 1 4 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.95 'accepted' 1 1 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.95 'accepted' 1 2 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.95 'accepted' 1 4 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.995 'accepted' 1 1 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.995 'accepted' 1 2 1 1 1
#python3 ./../src/main.py 'NK' 32 1000 0.995 'accepted' 1 4 1 1 1



# Measure with static freeze implementation

# Measure avg statistics (time and relative error)
# Slowing SA cooling (changing cooling rate) and changing equilibrium length
python3 ./../src/main.py 'NK' 32 1000 0.5 'static' 0.1 1 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.5 'static' 0.1 2 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.5 'static' 0.1 4 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.9 'static' 0.1 1 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.9 'static' 0.1 2 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.9 'static' 0.1 4 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.95 'static' 0.1 1 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.95 'static' 0.1 2 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.95 'static' 0.1 4 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.995 'static' 0.1 1 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.995 'static' 0.1 2 1 500 0
python3 ./../src/main.py 'NK' 32 1000 0.995 'static' 0.1 4 1 500 0

# Measure SA error evolving in runtime on picked instances
python3 ./../src/main.py 'NK' 32 1000 0.5 'static' 0.1 1 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.5 'static' 0.1 2 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.5 'static' 0.1 4 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.9 'static' 0.1 1 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.9 'static' 0.1 2 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.9 'static' 0.1 4 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.95 'static' 0.1 1 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.95 'static' 0.1 2 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.95 'static' 0.1 4 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.995 'static' 0.1 1 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.995 'static' 0.1 2 1 1 1
python3 ./../src/main.py 'NK' 32 1000 0.995 'static' 0.1 4 1 1 1
