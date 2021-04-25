## SAMPLE INPUT
1467.4236         <----- sum goal
0.000001          <----- margin of error
232.1462          <----- can be summed up to 5 times
323.2131          <----- can be summed up to 2 times
100.9184          |  all these can 
200.8275          |  only be summed 
255.5545          |  0 or 1 times
300.7376          V  
5                 |  denotes the "multiplier"
2                 |  for that index's value
1                 |
1                 |
1                 |
1                 V

## TEST "SOLUTIONS"
five.txt sum is (232.1462 * 4) + (323.2131 * 2) + (200.8275 * 1) = 1775.8385