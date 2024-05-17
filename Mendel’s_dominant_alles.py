import random
k = 2
m = 2
n = 2
def duplicate(testList, n):
    return [ele for ele in testList for _ in range(n)]
def domin_all(k,h,r):
    trials = 0
    dominants = 0
    full_comb=[]
    while True:
        list_AA=['AA'] 
        full_comb1=duplicate(list_AA,k)
        list_Aa=['Aa'] 
        full_comb2=duplicate(list_Aa,h)
        list_aa= ['aa'] 
        full_comb3=duplicate(list_aa,r)
        full_comb=full_comb1+full_comb2+full_comb3
        res = [(a, b) for idx, a in enumerate(full_comb) for b in full_comb[idx + 1:]]
        trials=sum(4 for ele in res)
        result=4*sum(ele==('AA','aa') for ele in res)+4*sum(ele==('AA','Aa') for ele in res)+ 2*sum(ele== ('Aa','aa') for ele in res)+3*sum(ele==('Aa','Aa') for ele in res) + 4*sum(ele==('AA','AA') for ele in res)
        return res, result/trials,trials
print(domin_all(k,m,n))