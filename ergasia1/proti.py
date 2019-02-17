'''
Η ασκηση δεν ειναι ολοκληρωμενη διοτι καταφερα να μετατρεψω μια επικαλυπτωμενη λιστα
σε μη επικαλυπτωμενη αλλα δεν καταφερα να υπολογισω το συνολικο αθροισμα των ψηφιων των
εσωτερικων λιστων
'''
def compresoneadjtuple(s):
    """useful to compress adjacent entries"""
    if len(s)<1:return s,True
    finals=[]
    for pos in range(len(s)-1):
        firstt, secondt=s[pos],s[pos+1]
        if (firstt[1]==secondt[0]) or (firstt[1]+1==secondt[0]):
            finals.append((firstt[0],secondt[1]))
            finals.extend(s[pos+2:])
            return finals,False
        else:
            finals.append(firstt)
    finals.append(s[-1])
    return finals,True


def merge_intervals(intervals):
    s = sorted(intervals, key=lambda t: t[0])
    m = 0
    for  t in s:
        if t[0] >= s[m][1]:
            m += 1
            s[m] = t
        else:
            s[m] = (s[m][0], t[1])
    done=False
    s=s[:m+1]
    while(not done):
        s,done=compresoneadjtuple(s)
    return s

f=((merge_intervals([[1,2], [6, 10], [11, 15] ])))


def flatten_list(k):
    result = list()
    for i in k:
        if isinstance(i,list):

           
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
ll=flatten_list(f)
print(ll)



