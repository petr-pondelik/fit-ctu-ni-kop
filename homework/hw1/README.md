# HW1: 0/1 Decision Knapsack problem Bruteforce + Branch & Bound

NI-KOP HW1 application solution.

## Prerequisites

* python3

## Project structure

    data/
        Contains input data sets and original solution sets.
        There are solution preprocessed by Python script (src/preprocess_solutions.py)
        to match decision Knapsack problem inside data/{data-set}/preprocessed directories.
        
    src/
        Contains source code of problem solution.
        
    res/
        Directory for storing result after running the application in testing mode.

## Commands

### Run the application
Run following command inside the src/ directory:

    python3 main.py <algorithm> <data-set> <items-amount> <testing-mode> <instances-interval>

#### Options 
 
**\<algorithm\>**

* 1: Bruteforce
* 2: Branch & Bound

**\<data-set\>**

* N: NR data-set
* Z: ZR data-set

**\<items-amount\>**

Amount of items (n) from [4, 10, 15, 20, 22, 25, 27, 30, 32, 25, 37, 40] list.

**\<testing-mode\>**

* 0: False
* 1: True

**\<instances-interval\>**

Interval of evaluated instances (in 0-0 to 0-499 range).

## Developer notes

There is a bug in comparison of application run result after running in testing mode.  
If the application is run with other than 0-499 interval, it's still compared with solution for 0-499 interval.