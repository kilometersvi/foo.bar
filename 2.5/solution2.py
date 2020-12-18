import math
import fractions

def solution(pegs):
    #calculate solution:
    difs = [pegs[i] - pegs[i-1] for i in range(1, len(pegs))]
    sum = 0
    for i in range(0, len(difs)):
        sum += difs[i] * int(math.pow(-1, i))
    r0 = [sum*2, 1] if len(pegs)%2==1 else [sum*2, 3]

    #check if viable:
    rs = [r0]
    for i in range(1, len(pegs)):
        r_test = [(difs[i-1])*rs[i-1][1]-rs[i-1][0], rs[i-1][1]]
        #print(str(i)+":"+str(n2)+","+str(d2))
        if r_test[0] <= 0:
            return [-1,-1]
        rs.append(r_test)

    #cleanup:
    return [r0[0]/fractions.gcd(r0[0], r0[1]), r0[1]/fractions.gcd(r0[0], r0[1])]

if __name__ == "__main__":
    print(solution([4, 31]))
    #print(solution([4, 17, 50]))
