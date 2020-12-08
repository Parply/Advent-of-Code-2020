import pandas as pd
import re

# PART 1
data = [{}]
i = 0
with open('input.txt', 'r') as f:
    for line in f:
        if line.replace(" ", "") == "\n":
            data.append({})
            i+=1
        else:
            d = re.split(":|\s",line)

            for v in range(len(d)//2):
                data[i][d[2*v]] = d[2*v + 1]

data = pd.DataFrame(data)

valid = data.iloc[:,data.columns!="cid"].dropna().shape[0]

print(f"Part 1: Valid Passports {valid}")

# PART 2
data=data.iloc[:,data.columns!="cid"].dropna()

# byr 
valid=data.byr.apply(len)==4
data = data.loc[valid]
data = data.loc[data.byr.astype(int).between(1920,2002)]

# iyr 
valid=data.iyr.apply(len)==4
data = data.loc[valid]
data = data.loc[data.iyr.astype(int).between(2010,2020)]

# eyr 
valid=data.eyr.apply(len)==4
data = data.loc[valid]
data = data.loc[data.eyr.astype(int).between(2020,2030)]

# hgt
def helper_h(s):
    if s[-2:] == "cm":
        temp = int(s[:-2])
        if temp>=150 and temp<=193:
            return True
        else:
            return False
    elif s[-2:] == "in":
        temp = int(s[:-2])
        if temp>=59 and temp<=76:
            return True
        else:
            return False
    return False

valid = data.hgt.apply(helper_h)
data = data.loc[valid]

# hcl 
def helper_hair(s):
    return bool(re.match("^#[0-9|a-f]{6}$",s))
valid = data.hcl.apply(helper_hair)
data = data.loc[valid]

# ecl
def helper_e(s):
    return bool(re.match("^(amb|blu|brn|gry|grn|hzl|oth)$",s))
valid = data.ecl.apply(helper_e)
data = data.loc[valid]

# pid
def helper_p(s):
    return bool(re.match("^[0-9]{9}$",s))
valid = data.pid.apply(helper_p)
data = data.loc[valid]

print(f"Part 2: Number of valid passports {data.shape[0]}")

