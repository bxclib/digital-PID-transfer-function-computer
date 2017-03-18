from math import *
def lg(n):
    return log(n)/log(10)
print ("P")
P=float(eval(input())) #transfer function =P/s
print ("crossover")
crossover=float(eval(input()))
crossover=float(crossover)*2*3.14
height=(20*lg(crossover)-20*lg(P))  # The gain of the middle flat part
print ("fp1,fp2")
fp1,fp2=eval(input())
w1=crossover/fp1
w2=crossover*fp2
k=10**((height+20*lg(w1))/20)
print ("(K*(1+s/w1))/(s*(1+s/w2))")
print ("k",k)
print ("w1",w1)
print ("w2",w2)
print ("psim parameters")
print ("gain",k/w1)
print ("T",1/w1)
print ("f",w2/6.28)


