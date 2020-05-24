TEST_STR = "123456789"

#write a function that prints contents in a string in a reverse order
#in: "123456789"
#out: "987654321"
def print_reverse(str_):
    #hint: use while loop
   revercedString=[]
   index = len(TEST_STR) #calculate index lenght 
   while index > 0:
       revercedString += TEST_STR[ index - 1 ] #saving the value for the reverced string??? seem wrong 
       index = index - 1 # decrementing by 1
       print(revercedString) # prinitng shit....
   
   

   pass


#write a function that prints all odd characters in the test string 
#in: "123456789"
#out: "13579"
def print_odd(str_):
    #hint - see modulo operator - %
    # if i % 2 == 0
    pass


#write a function that cuts a string each time it loops by 1 bytes
#in: "123456789"
#out: 
#1 loop - 123456789
#2 loop - 23456789
#3 loop - 3456789
#...
#last loop - 9
def cut_offn(str_):
    #hint: use array slice [n:m]
    pass



if __name__ == "__main__":
    print_reverse(TEST_STR)
    print_odd(TEST_STR)
    cut_offn(TEST_STR)