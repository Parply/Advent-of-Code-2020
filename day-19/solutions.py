

with open("input.txt","r") as f:
    raw_rules, message = f.read().split('\n\n')
    raw_rules = raw_rules.splitlines()
    message = message.splitlines()

def rule_process(raw_rules):
    rules = {}
    for rule in raw_rules:
        key, value = rule.split(': ')
        if value[0] == '"':
            rules[int(key)] = value[1:-1]
        else:
            values = value.split(' | ')
            temp_v = []
            for v in values:
                temp_v.append([int(vv) for vv in v.split(' ')])
            rules[int(key)] = temp_v
    return rules



def rule(e,s):
    if len(s)>len(e):
        return False
    elif len(s)==0 or len(e)==0:
        return len(s)==0 and len(e)==0
    c = s.pop()
    if isinstance(c, str):
        if e[0]==c:
            return rule(e[1:],s.copy())
    else:
        for r in rules[c]:
            if rule(e,s+list(reversed(r))):
                return True
    return False

def count(rules,messages):
    t=0
    for m in messages:
        if rule(m,list(reversed(rules[0][0]))):
            t+=1

    return t
rules = rule_process(raw_rules)
print(f"Part 1: {count(rules, message)}")
rules[8] = [[42],[42,8]]
rules[11] = [[42,31],[42,11,31]]
print(f"Part 2: {count(rules, message)}")
