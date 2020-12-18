
def domain(pegs):
    #find domain
    difs = [pegs[i] - pegs[i-1] for i in range(1, len(pegs))]
    difs_of_difs = [difs[i] - difs[i-1] for i in range(1, len(difs))]
    min_r0 = []
    max_r0 = []
    for i in range(len(difs_of_difs)):
        if difs_of_difs[i] < 0:
            current_r0 = difs_of_difs[i] * -1
            for pi in reversed(range(i)):
                current_r0 = difs[pi] - current_r0
            min_r0.append(current_r0)
        if difs_of_difs[i] > 0:
            current_r1 = difs_of_difs[i]
            for pi in reversed(range(i)):
                current_r1 = difs[pi+1] - current_r1
            current_r0 = difs[0]-current_r1
            max_r0.append(current_r0)

    dmin = max(min_r0) if len(min_r0) > 0 else 0
    dmax = min(max_r0) if len(max_r0) > 0 else difs[0]
    return (dmin, dmax)

def solution(pegs):


    if len(pegs)==2:
        n, d = [2*(pegs[1]-pegs[0]),3]
        return [n/d, 1] if n%d == 0 else [n, d]
    (dmin, dmax) = domain(pegs)
    if dmin  <= 0:# or dmax <= 0:
        return [-1, -1]
    accuracy = 1000 #higher the number, more likely to find a match
    for n in range(1, accuracy):
        for d in range(1,n+1):
            #print("0:"+str(n)+","+str(d))
            rs = [[n,d]]

            for i in range(1, len(pegs)):
                n2 = (pegs[i]-pegs[i-1])*rs[i-1][1]-rs[i-1][0]
                d2 = rs[i-1][1]
                #print(str(i)+":"+str(n2)+","+str(d2))
                if n2 < 0:
                    break
                rs.append([n2,d2])
            else:
                if rs[len(rs)-1][0]/rs[len(rs)-1][1]*2==rs[0][0]/rs[0][1]:
                    return [n,d]
                else: pass#print( (rs[0][0]/rs[0][1])/(rs[len(pegs)-1][0]/rs[len(pegs)-1][1]) if rs[len(pegs)-1][0]!=0 else 0 )
    return [-1,-1]
    #return [-1,-1]

def solution_2(pegs):
    difs = [pegs[i] - pegs[i-1] for i in range(1, len(pegs))]
    difs_of_difs = [difs[i] - difs[i-1] for i in range(1, len(difs))]
    
'''
import math
from fraction import Fraction

def solution(pegs):
    #init sum:
    sum = -1*pegs[0]+pegs[len(pegs)-1] if len(pegs)%2==0 else -1*pegs[0]-pegs[len(pegs)-1]

    #add for middle gears:
    if len(pegs) > 2:
        for i in range(1, len(pegs)-1):
            sum += 2*math.pow(-1,i+1)*pegs[i]

    firstGear = Fraction((2*sum/3.0 if len(pegs)%2==0 else sum)).limit_denominator()

    #check
    if firstGear < 2: return [-1,-1]

    currentRadius = firstGear
    for i in range(0, len(pegs)-2):
        centerDistance = pegs[index+1] - pegs[index]
        nextRadius = centerDistance - currentRadius
        if currentRadius < 1 or nextRadius < 1:
            return [-1, -1]
        else:
            currentRadius = nextRadius
    return [firstGear.numerator, firstGear.denominator]
'''
if __name__ == "__main__":
    print(solution([4, 30]))
    print(solution([4, 17, 50]))
    #print(domain([4,30,50]))
    #print(domain([4,17,50]))
