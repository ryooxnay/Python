def parentesis(n):
    k=n-2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k+1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
    k=2 * n - 2
    for i in range(0, n+1):
        for j in range(0, k):
            print(end=" ")
        k = k-1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
"""
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
"""
def parentesis_rombo(n):
    k=2*n-2
    for i in range(0, n+1):
        for j in range(0, k):
            print(end=" ")
        k=k-1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
    k=n-2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k=k+1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
   """     
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
   """
def parentesis_Trian_90G(n):
    for i in range(n, -1, -1):
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
        
        """    
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
   """

def parentesis_Trian_90G2(n):
    k=2*n-2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k=k-2
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
      
      """     
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
   """
def rombo():
    for i in range(5):
        for j in range(5):
            if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
                print("*", end="")
            else:
                print(end=" ")
        print("\r")

"""
  *  
 * * 
*   *
 * * 
  *  
   """
        
def parentesis_Trian_90G3(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")

        """     
* 
* * 
* * * 
* * * * 
* * * * * 
   """
        
def romboN(n):
    for i in range(n):
        for j in range(n):
            if i + j == (n//2) or i - j == (n//2) or i + j == (n+(n//3)) or j - i == (n//2):
                print("*", end="")
            else:
                print(end=" ")
        print("\r")
"""     
    *    
   * *   
  *   *  
 *     * 
*       *
 *     * 
  *   *  
   * *   
    * 
   """

def romboN2(n):
    for i in range(n):
        for j in range(n):
            if i + j == (n//2) or i - j == (n//2) or i + j == (n+(n//2.2)) or j - i == (n//2):
                print("*", end="")
            else:
                print(end=" ")
        print("\r")


"""   
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
   """        
def triang(n):
    k=2*n-2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end=" ")
        k=k-2
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
    k = -1
    for i in range(n-1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k+2
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")

        """ 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
   """
def trian2(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
    for i in range(n, 0, -1):
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

parentesis(5)  
parentesis_rombo(5)
parentesis_Trian_90G(5)
parentesis_Trian_90G2(5)
rombo()
parentesis_Trian_90G3(5)
romboN(9)
triang(5)
trian2(5)
