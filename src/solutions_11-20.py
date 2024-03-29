import pandas as pd 
import numpy as np 
import sys

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from math import sqrt, floor

def solution_11(args):
    m = [[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
     [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
     [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
     [52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
     [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
     [24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
     [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
     [67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
     [24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
     [21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
     [78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
     [16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
     [86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
     [19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
     [4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
     [88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
     [4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
     [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
     [20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
     [1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]

    up_down = get_up_down_max_product(m)  
    left_right = get_left_right_max_product(m)
    right_diag = get_right_diag_max_product(m)
    left_diag = get_left_diag_max_product(m)
    
    return max(up_down, left_right, right_diag, left_diag)

def get_up_down_max_product(m):
    max_product = 1
    for i in range(17):
        for j in range(20):
            max_product = max(max_product,m[i][j]*m[i+1][j]*m[i+2][j]*m[i+3][j])
    return max_product

def get_left_right_max_product(m):
    max_product = 1
    for i in range(20):
        for j in range(17):
            max_product = max(max_product,m[i][j]*m[i][j+1]*m[i][j+2]*m[i][j+3])
    return max_product

def get_right_diag_max_product(m):
    max_product = 1
    for i in range(17):
        for j in range(17):
            max_product = max(max_product,m[i][j]*m[i+1][j+1]*m[i+1][j+2]*m[i+1][j+3])
    return max_product

def get_left_diag_max_product(m):
    max_product = 1
    for i in range(17):
        for j in range(3,20):
            max_product = max(max_product,m[i][j]*m[i+1][j-1]*m[i+2][j-2]*m[i+3][j-3])
    return max_product

def solution_12(args):
    factor_goal = 500
    i = 1
    triangle_num = 0
    notComplete = True
    while notComplete:
        triangle_num += i
        i += 1
        factors_count = get_factors_count(triangle_num)
        if factors_count >= factor_goal:
            break
            notComplete = False
    return triangle_num

def get_factors_count(number):
    factors_count = 0
    i = 1
    j = number
    while i < j:
        if number%i == 0:
            factors_count += 2
        j = int(number/i)
        i += 1
    if i==j:
        if i*j == number:
            factors_count += 1
    return factors_count

def solution_13(args):
    d = [37107287533902102798797998220837590246510135740250,46376937677490009712648124896970078050417018260538,74324986199524741059474233309513058123726617309629,91942213363574161572522430563301811072406154908250,23067588207539346171171980310421047513778063246676,89261670696623633820136378418383684178734361726757,28112879812849979408065481931592621691275889832738,44274228917432520321923589422876796487670272189318,47451445736001306439091167216856844588711603153276,70386486105843025439939619828917593665686757934951,62176457141856560629502157223196586755079324193331,64906352462741904929101432445813822663347944758178,92575867718337217661963751590579239728245598838407,58203565325359399008402633568948830189458628227828,80181199384826282014278194139940567587151170094390,35398664372827112653829987240784473053190104293586,86515506006295864861532075273371959191420517255829,71693888707715466499115593487603532921714970056938,54370070576826684624621495650076471787294438377604,53282654108756828443191190634694037855217779295145,36123272525000296071075082563815656710885258350721,45876576172410976447339110607218265236877223636045,17423706905851860660448207621209813287860733969412,81142660418086830619328460811191061556940512689692,51934325451728388641918047049293215058642563049483,62467221648435076201727918039944693004732956340691,15732444386908125794514089057706229429197107928209,55037687525678773091862540744969844508330393682126,18336384825330154686196124348767681297534375946515,80386287592878490201521685554828717201219257766954,78182833757993103614740356856449095527097864797581,16726320100436897842553539920931837441497806860984,48403098129077791799088218795327364475675590848030,87086987551392711854517078544161852424320693150332,59959406895756536782107074926966537676326235447210,69793950679652694742597709739166693763042633987085,41052684708299085211399427365734116182760315001271,65378607361501080857009149939512557028198746004375,35829035317434717326932123578154982629742552737307,94953759765105305946966067683156574377167401875275,88902802571733229619176668713819931811048770190271,25267680276078003013678680992525463401061632866526,36270218540497705585629946580636237993140746255962,24074486908231174977792365466257246923322810917141,91430288197103288597806669760892938638285025333403,34413065578016127815921815005561868836468420090470,23053081172816430487623791969842487255036638784583,
        11487696932154902810424020138335124462181441773470,63783299490636259666498587618221225225512486764533,67720186971698544312419572409913959008952310058822,95548255300263520781532296796249481641953868218774,76085327132285723110424803456124867697064507995236,37774242535411291684276865538926205024910326572967,23701913275725675285653248258265463092207058596522,29798860272258331913126375147341994889534765745501,18495701454879288984856827726077713721403798879715,38298203783031473527721580348144513491373226651381,34829543829199918180278916522431027392251122869539,40957953066405232632538044100059654939159879593635,29746152185502371307642255121183693803580388584903,41698116222072977186158236678424689157993532961922,62467957194401269043877107275048102390895523597457,23189706772547915061505504953922979530901129967519,86188088225875314529584099251203829009407770775672,11306739708304724483816533873502340845647058077308,82959174767140363198008187129011875491310547126581,97623331044818386269515456334926366572897563400500,42846280183517070527831839425882145521227251250327,55121603546981200581762165212827652751691296897789,32238195734329339946437501907836945765883352399886,75506164965184775180738168837861091527357929701337,62177842752192623401942399639168044983993173312731,32924185707147349566916674687634660915035914677504,99518671430235219628894890102423325116913619626622,73267460800591547471830798392868535206946944540724,76841822524674417161514036427982273348055556214818,97142617910342598647204516893989422179826088076852,87783646182799346313767754307809363333018982642090,10848802521674670883215120185883543223812876952786,71329612474782464538636993009049310363619763878039,62184073572399794223406235393808339651327408011116,66627891981488087797941876876144230030984490851411,60661826293682836764744779239180335110989069790714,85786944089552990653640447425576083659976645795096,66024396409905389607120198219976047599490197230297,64913982680032973156037120041377903785566085089252,16730939319872750275468906903707539413042652315011,94809377245048795150954100921645863754710598436791,78639167021187492431995700641917969777599028300699,15368713711936614952811305876380278410754449733078,40789923115535562561142322423255033685442488917353,44889911501440648020369068063960672322193204149535,41503128880339536053299340368006977710650566631954,81234880673210146739058568557934581403627822703280,82616570773948327592232845941706525094512325230608,22918802058777319719839450180888072429661980811197,77158542502016545090413245809786882778948721859617,72107838435069186155435662884062257473692284509516,20849603980134001723930671666823555245252804609722,53503534226472524250874054075591789781264330331690]
    d_str = [str(x) for x in d]

    final_digits = [0]*55
    for i in range(1,51):
        ith_digits = [int(x[-i]) for x in d_str]
        ith_sum = final_digits[-i] + sum(ith_digits)
        ith_digit = ith_sum%10
        final_digits[-i] = ith_digit
        carry = floor(ith_sum/10)
        final_digits[-i-1] = carry

    final_answer = ""
    non_zero_found = False
    for num in final_digits:
        if not(non_zero_found):
            if num != 0:
                final_answer += str(num)
                non_zero_found = True
        else:
            final_answer += str(num)
    return int(final_answer[:10])

def solution_14(args):
    all_sequence_dict = {1:1,2:2,3:8,4:3}
    length_set = set([1,2,3,4])
    max_seq = 8
    for i in range(5,1000000):
        if i in length_set:
            continue
        else:
            seq_length, all_sequence_dict, length_set = get_collatz_sequence_length(i,all_sequence_dict,length_set)
            if seq_length > max_seq:
                max_seq = seq_length
                #print("New max: {} has collatz sequence length {}".format(i,max_seq))
    return max_seq

def get_collatz_sequence_length(n,all_sequence_dict,length_set):
    sequence_length = 0
    notFoundInDict = True
    new_data_to_add = {}
    while notFoundInDict:
        if n in length_set:
            sequence_length += all_sequence_dict[n]
            notFoundInDict = False
        else:
            new_data_to_add[int(n)] = sequence_length
            if n%2 == 0:
                n = n/2
            else:
                n = 3*n + 1
            sequence_length += 1
    for item in new_data_to_add.keys():
        all_sequence_dict[int(item)] = sequence_length-new_data_to_add[item]
        length_set.add(int(item))
    return sequence_length, all_sequence_dict, length_set

def solution_15(args):
    path_dict = {"1x1":2,"2x2":6,"3x3":20}
    for i in range(4,21):
        new_grid = str(i) + "x" + str(i)
        # formula for new grid = 2(i-1xi-1) + 2(ixi-2) == 2(a) + 2(b)
        a_key = str(i-1) + "x" + str(i-1)
        a = path_dict.get(a_key)
    
        b_key = str(i) + "x" + str(i-2)
        b, path_dict = determine_paths_of_uneven_lattice(b_key,path_dict)
        answer = 2*a + 2*b
        path_dict[new_grid] = answer
    return path_dict["20x20"]

def determine_paths_of_uneven_lattice(board,path_dict):
    entries = list(path_dict.keys())
    if board in entries:
        return path_dict.get(board),path_dict
    [first_digit, second_digit] = board.split("x")
    if int(first_digit) >= int(second_digit):
        if second_digit == "0":
            path_dict[board] = 1
            return 1,path_dict
        elif second_digit == "1":
            path_dict[board] = (int(first_digit)+1)
            return (int(first_digit)+1), path_dict
        else:
            # formula = 2(a-1xb-1) + a-2xb + axb-2 == 2(c) + d + e
            c_key = str(int(first_digit)-1) + "x" + str(int(second_digit)-1)
            c, path_dict = determine_paths_of_uneven_lattice(c_key,path_dict)
            d_key = str(int(first_digit)-2) + "x" + second_digit        
            d, path_dict = determine_paths_of_uneven_lattice(d_key,path_dict)
            e_key = first_digit + "x" + str(int(second_digit)-2)
            e, path_dict = determine_paths_of_uneven_lattice(e_key,path_dict)
        
            paths = 2*c + d + e
            path_dict[board] = paths
            return paths, path_dict
    else:
        flipped_board = second_digit + "x" + first_digit
        rev_val, path_dict = determine_paths_of_uneven_lattice(flipped_board,path_dict)
        path_dict[board] = rev_val
        return rev_val, path_dict

def solution_16(args):
    sum_ = 0
    for item in str(2**1000):
        sum_ += int(item)
    return sum_

def solution_17(args):
    word_list = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',0:''}
    total_length = 0
    for i in range(1000):
        words = number_to_words_under_1000(i,word_list).replace(" ","")
        total_length += len(words)
        print(words)
    return total_length + len("onethousand")

def number_to_words_under_100(tens_digit,units_digit,word_list):
    if tens_digit < 2 or units_digit == 0:
        number = tens_digit*10 + units_digit
        return word_list.get(number)
    else:
        words = word_list.get(tens_digit*10) + " " + word_list.get(units_digit)
        return words

def number_to_words_under_1000(number,word_list):
    if number > 999:
        raise ValueError("Please Enter a number under 1000")
    units_digit = (number%10)
    tens_digit = int((number-units_digit)/10)%10
    hundreds_digit = int((number-units_digit-(tens_digit*10))/100)
    
    if hundreds_digit == 0:
        return number_to_words_under_100(tens_digit,units_digit,word_list)
    first_word = word_list.get(hundreds_digit)
    if tens_digit == 0 and units_digit == 0:
        return first_word + " hundred"
    else:
        words = first_word + " hundred and " + number_to_words_under_100(tens_digit,units_digit,word_list)
        return words

def solution_18(args):
    d = [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

    rows = len(d)
    max_path = d
    max_path[-1] = d[-1]
    for i in range(2,rows+1):
        row = rows-i
        for j in range(len(d[row])):
            row_below = max_path[row+1]
            max_val = max(row_below[j],row_below[j+1])
            max_path[row][j] = d[row][j] + max_val

    return max_path[0][0]

def solution_19(args):
    month_dict = {'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}

    sunday_first_day_count = 0
    prev_day = 6 # we start 1900 Jan 1 on a Monday, so prev day was a sunday (Mon-Sun == 0-6)
    for i in range(1900,2001):
        for month in month_dict.keys():
            #print("{} starts on {}".format(month,(prev_day+1)%7))
            days = month_dict[month]
            if month == 'February' and i%4 == 0 and i!=1900:
                days += 1
            if prev_day == 5:
                #print("Sunday Found: {} {}".format(month,i))
                if i != 1900:
                    sunday_first_day_count += 1
            days_change = days%7 # if zero, day stays same throughout month, if 1, add 1 to day, etc
            prev_day = (prev_day+days_change)%7

    return sunday_first_day_count  

def solution_20(args):
    from math import factorial
    x = str(factorial(100))
    s = 0
    for item in x:
        s += int(item)
    return s

def main(argument_list):
    if len(argument_list) >= 2:
        solution_no = str(argument_list[1])
        args = argument_list[2:]
        solution_dict = {"11":solution_11,"12":solution_12,"13":solution_13,"14":solution_14,"15":solution_15,
                        "16":solution_16,"17":solution_17,"18":solution_18,"19":solution_19,"20":solution_20}
        answer = solution_picker(solution_dict.get(solution_no), args)
        logger.info(" Answer: {}".format(answer))
    else:
        logger.error(" ERROR: You must pass in a solution number")
        
def solution_picker(func,args):
    return func(args)

if __name__ == "__main__":
    main(list(sys.argv))
