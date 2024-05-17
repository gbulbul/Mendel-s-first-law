import random
k = 2
m = 2
n = 2
def MultipLy(multiList, n):
    return [ele for ele in multiList for _ in range(n)]
def domnnt_all(k,h,r):
    trials = 0
    dominants = 0
    full_comb=[]
    while True:
        list_AA=['AA'] 
        full_comb1=MultipLy(list_AA,k)
        list_Aa=['Aa'] 
        full_comb2=MultipLy(list_Aa,h)
        list_aa= ['aa'] 
        full_comb3=MultipLy(list_aa,r)
        full_comb=full_comb1+full_comb2+full_comb3
        pairs = [(a, b) for idx, a in enumerate(full_comb) for b in full_comb[idx + 1:]]
        trials=sum(4 for ele in pairs)
        result=4*sum(ele==('AA','aa') for ele in pairs)+4*sum(ele==('AA','Aa') for ele in pairs)+ 2*sum(ele== ('Aa','aa') for ele in pairs)+3*sum(ele==('Aa','Aa') for ele in pairs) + 4*sum(ele==('AA','AA') for ele in pairs)
        return pairs, result/trials,trials
print(domnnt_all(k,m,n))
