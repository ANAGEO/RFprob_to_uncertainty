# Random Forest probabilities to uncertainty measure

This repository contains a piece of Python code used to compute "uncertainty level" for a Random Forest (RF) probabilistic output.

From a input .csv similar to the following :

|cat|ACS|BARE|PLAN|UNPLAN|VEG|
|---|---|---|---|---|---|
|1|0.00100000000|0.26700000000|0.00100000000|0.00300000000|0.73000000000|
|2|0.00000000000|0.53100000000|0.00050000000|0.00300000000|0.46550000000|
|3|0.00000000000|0.13100000000|0.00550000000|0.01400000000|0.84950000000|
|4|0.10900000000|0.32000000000|0.11200000000|0.16650000000|0.29250000000|
|5|0.08000000000|0.00500000000|0.52000000000|0.39100000000|0.00400000000|


It return a new .csv file : 

|cat|ACS|BARE|PLAN|UNPLAN|VEG|first_label|second_label|first_prop|second_prop|uncert_level|
|---|---|---|---|---|---|---|---|---|---|---|
|1|0.001|0.267|0.001|0.003|0.73|VEG|BARE|0.73|0.267|0.463|
|2|0.0|0.531|0.0005|0.003|0.4655|BARE|VEG|0.531|0.4655|0.0655|
|3|0.0|0.131|0.0055|0.014|0.8495|VEG|BARE|0.8495|0.131|0.7185|
|4|0.109|0.32|0.112|0.1665|0.2925|BARE|VEG|0.32|0.2925|0.0275|
|5|0.08|0.005|0.52|0.391|0.004|PLAN|UNPLAN|0.52|0.391|0.129|


Here after are the meaning of the different new columns:
- first\_label : Column with the highest probability
- second\_label : Column with the second highest probability
- first\_prop : Value of the highest probability
- second\_prop : Value of the second highest probability
- uncert\_level : "Uncertainty level" which is simply the difference between first\_prop  and  second\_prop. 

A low value of the "uncert\_level" indicates a high uncertainty of classification from RF.
