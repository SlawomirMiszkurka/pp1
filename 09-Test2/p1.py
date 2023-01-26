def f(player1,player2):
    dict={
    "A":10,
    "K":10,
    "Q":10,
    "J":10,
    "T":10,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2
    }   
    sum1=0
    sum2=0
    for i in player1:
        sum1+=dict[i]
    for i in player2:
        sum2+=dict[i]
        
    return sum1>sum2
f("AJ972","AQT72")
f("9532","K8") 
f("987","AT4")
