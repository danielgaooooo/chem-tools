# Chem-Tools

## Step 1: Install Required Dependencies
* Make sure you have Python3 installed.
* Download [git](https://git-scm.com/downloads).

## Step 2: Navigate to Proper Directory
* Open Git Bash
* Navigate to where you've put the `main.py` script.
    * For example, if `main.py` is on your `Desktop`:
        ```
        cd ~/Desktop
        ```
        will take you to your Desktop.
        ```
        ls
        ```
        should confirm that `main.py` is present.
    * For me, since my `main.py` lives at `~/Documents/dev/chem_code`, it looks like this:
        ```
        > cd ~/Documents/dev/chem_code 
        > ls
        README.md       data.txt     main.py
        ```
## Step 3: Run Program
Once you are in the proper directory, run:
```
python3 main.py data.txt
```
where `data.txt` is your input data. You can name your data file whatever you 
want, just tell the script where to find it. For example, if your data file is 
at `~/Downloads/data/weights.txt`, run instead:
```
python3 main.py ~/Downloads/data/weights.txt
```

## Formatting Your Data
The program expects your data file to be formatted in a certain way. The file 
should have 5 lines total.  
1. Total sum (Number)
2. Error (Number, between 0 and 1)
3. Individual weights, space-separated (List-of Numbers)
4. Maximum counts of each individual weight, space-separated (List-of Numbers)
4. Required weights (List-of Numbers)

#### Example
In the below example, I'm requesting:
- a **total sum** of 20
- an **error** of 1%
- **weights** of 1, 2, 4, 6, and 8
- **max weight counts** of one 1, two 2s, one 4, three 6s, and two 8s
- **required weights** of 1 and 4
```
20
0.01
1 2 4 6 8
1 2 1 3 2
1 4
```