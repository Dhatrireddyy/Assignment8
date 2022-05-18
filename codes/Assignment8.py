# CBSE Probability Grade 12
# Question 13.4.16

# Name: Velma Dhatri Reddy
# Roll number: AI21BTECH11030

""" Problem Statement
The mean of the numbers obtained on throwing a die having written 1 on three faces, 
2 on two faces and 5 on one face is
"""

from math import comb

def main():
    P_1 = 1/2
    P_2  = 1/3   
    P_3 = 1/6 
    X_1 = 1 
    X_2 = 2  
    X_3 = 5 

    #Output
    print(f"The mean of the numbers obtained on throwing is {prob(P_1,P_2,P_3,X_1,X_2,X_3)}")
     
def prob(P_1,P_2,P_3,X_1,X_2,X_3) -> float:
        """ Returns the mean of the numbers """
        return X_1*P_1 + X_2*P_2 + X_3*P_3

if __name__ == '__main__':
       main()
