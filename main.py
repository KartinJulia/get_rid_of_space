string = """
// d e p e n d e n ci e s
c o n s t e x p r e s s = r e q u i r e ( ’ e x p r e s s ’ ) ;
c o n s t u r l = r e q u i r e ( ’ u rl ’ ) ;
// c r e a t e the s e r v e r
c o n s t app = e x p r e s s ( ) ;
c o n s t p o r t = 3 0 0 1;
// the methods
app . g e t ( ’ / ’ , ( r e q u e s t , r e s p o n s e ) => {
var u rlP a r t s = u r l . p a r s e ( r e q u e s t . u rl , t r u e ) ;
var p a r ame te r s = u rl P a r t s . query ;
var e x p r e s si o n = p a r ame te r s . e x p r e s si o n ;
r e s p o n s e . send ( e x p r e s si o n + " = ? " ) ;
} ) ;
// s t a r t the s e r v e r
app . l i s t e n ( port , ( )
=> c o n s ol e . l o g ( ’ Li s t e ni n g on p o r t ’ + p o r t ) ) ;
"""

def lst_2_str(lst):
    res = ""
    for i in lst:
        res += i
    return res

temp = []
for i in range (len(string)):
    #print(string[i])
    letter = string[i]
    if letter != " ":
        temp.append(letter)
    if letter == "\n" :
        #print(str(temp))
        res = lst_2_str(temp)
        print(res)
        temp = []
