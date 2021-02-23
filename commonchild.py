
def main():
    tests = [(('HARRY','SALLY'),2),
             (('AA','BB'),0),
             (('SHINCHAN','NOHARAAA'),3),
             (('ASHINCHAN','NOHARAAA'),3),
             (('ABCDEF','FBDAMN'),2),
             (('APMCTKBUKYRGZPAUVZEBVUXRGDVITOYXWQWRVCSXESMEHQLHPDJQWETAWQVSBRRNRRFDLFTRXOTKQHFTYAZSGBORDNAMUAJTPVOKERLVOLEALDQQLUDCUIRXJHQEZBRWYPFJXNTPELEZHNJILIZVZLYQJDFYSYQNRFFAOYXHQBQVRLFDIIOGWKQIZGVELYOUKZBKMHVYGIKIPSEMWSCWYOJTHOQKMLBAIZYNAKYNCXKDTTESODDAEAHKCDHCJYAHERACMLYQHXIRDFUSRTZDNVHSYFKCSPPYSLHOGIBTNUJTZQWVTHKUNDNWZADMATSUXEISCACQNQXIHNTXGCZUGIGBDONYTUXAXFINAYGZJVDCTZCWPGFNQDPERUCNJUXIFDSQHULYPZRNUOKMLMMQAJMLKCHJMEFJVRYZIPFQOBSDPAITHGMNKROCWJEGESCGOIUOQHOYUEQNPJPBMCNRZUHOSQNSUNCSTVQVWFGMUFJZGMEUVUPH','JUVSDRRSHFGSSLLLZEPJDVAWDPKQBKUHHOZFFXKQMGAACZUYOMNPHWGTYZWQGSMNYXWNFYNOIVVMPZXUNKJQYBYJINBOHXUWIVRTVLEKCOPDMTKTGDBWECDAVPMLHQLERZHDVZJZODPSAPGSRWJXNGFEBQBLTLNDIEGFHEGHJWFOIYXRUJMODSNXUFWBIJJMXTFMUKQEYPNBTZFEJNLDNWCGQLVUQUKGZHJOKZNPMUYEQLEYNNORKJQAMSTHTBCCPQTTCPRZATWNJQJXPODRXKIWDOFUBZVSDTAPFRMXJBJMUGVRZOCDUIPXVEGMRQNKXDKNWXMTNDJSETAKVSYMJISAREEJPLRABMXJSRQNASOJNEEVAMWCFJBCIOCKMHCMYCRCGYFNZKNALDUNPUSTSWGOYHOSWRHWSMFGZDWSBXWXGVKQPHGINRKMDXEVTNNZTBJPXYNAXLWZSBUMVMJXDIKORHBIBECJNKWJJJSRLYQIKKPXSNUT'),155),
            ]
    clean = True

    for t,k in tests:
        a = commonChild(*t)
        clean *= a==k
        if a != k: print('Words:',t,'| Output:',a,'| Expected',k)
    if clean: print('All tests checkout!')

    while True:
        w1 = input('Word1: ')
        w2 = input('Word2: ')
        if w1 == 'q' and input('Do you want to quit? (y/n): ') == 'y': break
        print(commonChild(w1,w2))


def commonChildA1(s1, s2):
    commonset = set(s1).intersection(set(s2))
    s1 = [s for s in s1 if s in commonset]
    s2 = [s for s in s2 if s in commonset]
    if not commonset: return 0

    def pair_string(c1,c2):
        if len(c1) > len(c2):
            c1,c2 = c2,c1
        return ''.join(c1)+'_'+''.join(c2)

    def order(c1,c2):
        if len(c1) > len(c2):
            return c2,c1
        return c1,c2

    shead = []
    m = 0
    lastc = 0
    c1, c2 = order(s1, s2)
    dpmf = {'_':0}
    icount = 0

    while True:
        ps = pair_string(c1,c2)

        if m < 2:
            if m == 0:
                cand1, cand2 = c1[1:], c2[c2.index(c1[0])+1:]
            elif m == 1:
                dpmf[ps] = lastc + 1
                cand1, cand2 = c1[1:], c2[:]
            candcommon = set(cand1).intersection(set(cand2)) 
            cand1 = [c for c in cand1 if c in candcommon]
            cand2 = [c for c in cand2 if c in candcommon]
            candps = pair_string(cand1,cand2)

            m += 1
            if candps in dpmf:
                lastc = dpmf[candps]
            elif len(candcommon) == 1:
                lastc = min(len(cand1),len(cand2))
            else:
                shead.append((c1,c2,m))
                m = 0
                c1,c2 = order(cand1,cand2)
        else:
            dpmf[ps] = max(dpmf[ps],lastc)
            if not shead: break
            lastc = dpmf[ps]
            c1,c2,m = shead.pop()

    return dpmf[pair_string(s1,s2)]
        
def commonChild(s1, s2):
    A = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for r in range(1,len(s1)+1):
        for c in range(1,len(s2)+1):
            if s1[r-1] == s2[c-1]:
                A[r][c] = A[r-1][c-1]+1
            else:
                A[r][c] = max(A[r-1][c],A[r][c-1])

    return A[-1][-1]

if __name__ == '__main__': main()
