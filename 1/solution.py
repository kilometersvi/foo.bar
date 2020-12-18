import math
import time
'''
def get_squares(area, num_sqs):
    for sq in reversed(range(1, area+1)):
        if int(math.sqrt(sq)+0.5)**2==sq:
            #print("match: "+str(sq))
            if num_sqs==0:
                return [x]
            sqs = get_squares(area-sq,num_sqs-1)
            if len(sqs)==num_sqs-1:
                sqs.append(sq)
                sqs.sort(reverse=True)
                return sqs
        #else:
            #print("no match: "+str(sq))
    if num_sqs==0:
        return []
    return get_squares(area,num_sqs-1)

def solution(area):
    return get_squares(area, area-1)
'''
def get_squares(area, num_sqs):
    for sq in reversed(range(1, area+1)):
        if int(math.sqrt(sq)+0.5)**2==sq: #check if var sq is a perfect square
            #
            if num_sqs==0:
                return [sq]
            sqs = get_squares(area-sq,num_sqs-1)
            if len(sqs)==num_sqs-1:
                sqs.append(sq)
                sqs.sort(reverse=True)
                return sqs
    # If
    if num_sqs==0:
        return []
    return get_squares(area,num_sqs-1)

def solution(area):
    valid_solutions = []
    for n in range(1,area+1):
        sqs = get_squares(area, n)
        print(sqs)
        valid_solutions.append(sqs)
    max_i = 0
    for i in range(0, len(valid_solutions)):
        if valid_solutions[i][0]<valid_solutions[1][0]:
            break
        max_i = i
    return valid_solutions[max_i]

def solution_2(area):
    sqs = []
    while area > 0:
        for possible_sq in reversed(range(1, area+1)):
            if int(math.sqrt(possible_sq)+0.5)**2==possible_sq: #check if var sq is a perfect square
                sqs.append(possible_sq)
                area -= possible_sq
                break
    return sqs

def printAll(max):
    for i in reversed(range(1, max)):
        print(solution(i))
        time.sleep(0.1)

if __name__ == "__main__":
    #printAll(4)#15324)
    print(solution_2(12))
