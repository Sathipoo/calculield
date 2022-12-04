


error_parsers=['++','--','-*','*-']
iteration_stopper=15

def check_iteration(count):
    if(count>=iteration_stopper):
        # raise Exception('reached the max iterations:',iteration_stopper)
        print('reached the max iterations:',iteration_stopper)
        return(True)
        
def get_data(a):
    count=0
    eq_buil=""
    while True:
        for char in a:
            if(char!=' '):
                if(char!='?'):
                    count+=1
                    if(not check_iteration(count)):
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
                        return(False)
                else:
                    count=0
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



def main_yeilder(a):

    sat=get_data(a)

    avg=0
    vals=[]
    count=0
    # summ=0
    ch_buil=""
    while True:
        
        try:
            prob=next(sat)
            n_prob=bracket_parser(prob)
            # cal = Calculator(n_prob)
            vals.append(local_calc(n_prob))
            if(prob==n_prob):
                # print(prob+ " = "+str(cal.result))
                t_var=(prob+ " = "+str(local_calc(n_prob)))
                # print(t_var)
                ch_buil+=t_var+"\n"
            else:
                # print(prob+ " --> "+n_prob+" = "+str(cal.result))
                o_var=(prob+ " --> "+n_prob+" = "+str(local_calc(n_prob)))
                # print(o_var)
                ch_buil+=o_var+"\n"
            count+=1
            if(check_iteration(count)):
                return(ch_buil)
        except StopIteration:
            # print(ch_buil)
            ch_buil+=("ERROR")
            break
        except Exception as e:
            # print(ch_buil)
            ch_buil+=str(e)
            break
    return(ch_buil)

if (__name__=="__main__"):
    # res=main_yeilder("1+2+3?5-4-3?-4-6?-2++?")
    res=main_yeilder("1+1-3-24-3-13-1-3013-133-13-3-4?")
    print("----------")
    print(res)
    # main_yeilder("1+2+35-4-3-4-6-2")