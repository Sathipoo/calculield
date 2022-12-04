


error_parsers=['++','--','-*','*-']
iteration_stopper=15

def get_data(a):
    # a="1 1 * 2 ? 1 + (3 ?* 2 ?/ 1 + 3 )?* 2 ? 1 + 3 ? * 7 ?  + 8 7 9 ?"
    eq_buil=""
    while True:
        for char in a:
            if(char!=' '):
                if(char!='?'):
                    eq_buil+=char
                    # if(char=='+' and char==eq_buil[-2]) or (char=='-' and char==eq_buil[-2]):
                    #     print("terminating the program due to a wrong sequence")                      
                    #     return(False)
                    if(len(eq_buil)>=2):
                        checker=str(char)+str(eq_buil[-2])
                        if(checker in error_parsers):
                            print("terminating the program due to a wrong sequence")                      
                            return(False)
                else:
                    yield eq_buil

def bracket_parser(prob):
    open_brack_count=prob.count('(')
    close_brack_count=prob.count(')')
    if(open_brack_count!=close_brack_count):
        new_prob=prob.replace('(','').replace(')','')
        return(new_prob)
    else:
        return prob
        
def local_calc(prob):
    result=eval(prob)
    return(result)

def check_iteration(count):
    if(count>=iteration_stopper):
        raise Exception('reached the max iterations:',iteration_stopper)

import sys
if(len(sys.argv)>1):
    a=sys.argv[1]
else:
    # a="1+1-3-24-3-13-1?-3013?-133-13-3-4?"
    a="1-2-3-3-1-3-13-13-13-13?"
sat=get_data(a)

avg=0
vals=[]
count=0
# summ=0
while True:
    try:
        prob=next(sat)
        n_prob=bracket_parser(prob)
        # cal = Calculator(n_prob)
        vals.append(local_calc(n_prob))
        if(prob==n_prob):
            # print(prob+ " = "+str(cal.result))
            print(prob+ " = "+str(local_calc(n_prob)))
        else:
            # print(prob+ " --> "+n_prob+" = "+str(cal.result))
            print(prob+ " --> "+n_prob+" = "+str(local_calc(n_prob)))
        count+=1
        check_iteration(count)
    except StopIteration:
        print("ERROR")
        break
    except Exception as e:
        print(e)
        print("found an exeception")
        break


