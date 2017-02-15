from sympy import *
class PID():
    def __init__(self,expr,method="Forward"):
        k,s,T1,T2,T3,z,Ts=symbols("k,s,T1,T2,T3,z,Ts")
        self.s2z={"Forward":"(1-z**-1)/(Ts*z**-1)","Backward":"(1-z**-1)/Ts","Tustin":"2*(1-z**-1)/(1+z**-1)/Ts"}
        expr=sympify(expr)
        #print (expr)
        self.expr=simplify(expr.subs(s,self.s2z[method]))
        
        n,d=fraction(self.expr)
        #print (expand(n))
        #print (expand(d))
        nlist=[0]
        dlist=[0]
        while simplify(n-nlist[len(nlist)-1])!=0:
            a=simplify(n.subs(z,0))
            nlist.append(a)
            n=simplify((n-a)/z)
        while simplify(d-dlist[len(dlist)-1])!=0:
            a=simplify(d.subs(z,0))
            dlist.append(a)
            d=simplify((d-a)/z)
        self.nlist=nlist[1:len(nlist)-1]
        self.dlist=dlist[1:len(dlist)-1]
        ml=max(len(nlist),len(dlist))
        for i in range(len(nlist),ml):
            self.nlist.append(sympify("0"))
        for i in range(len(dlist),ml):
            self.dlist.append(sympify("0"))    

        print (self.nlist)
        print (self.dlist)
    def printEquation(self,parameters={}):
        k,s,T1,T2,T3,z,Ts=symbols("k,s,T1,T2,T3,z,Ts")
        nlist_Print=self.nlist[::]
        dlist_Print=self.dlist[::]
        for j,i in enumerate(nlist_Print):
            if "T1" in parameters.keys():
                i=i.subs(T1,parameters["T1"])
            if "T2" in parameters.keys():
                i=i.subs(T2,parameters["T2"])
            if "T3" in parameters.keys():
                i=i.subs(T3,parameters["T3"])
            if "Ts" in parameters.keys():
                i=i.subs(Ts,parameters["Ts"])
            if "k" in parameters.keys():
                i=i.subs(k,parameters["k"])
            nlist_Print[j]=simplify(i)
        #print (nlist_Print)
        for j,i in enumerate(dlist_Print):
            if "T1" in parameters.keys():
                i=i.subs(T1,parameters["T1"])
            if "T2" in parameters.keys():
                i=i.subs(T2,parameters["T2"])
            if "T3" in parameters.keys():
                i=i.subs(T3,parameters["T3"])
            if "Ts" in parameters.keys():
                i=i.subs(Ts,parameters["Ts"])
            if "k" in parameters.keys():
                i=i.subs(k,parameters["k"])
            dlist_Print[j]=simplify(i)
        #print (dlist_Print)
        first=True
        for i in range(len(dlist_Print)):
            if dlist_Print[len(dlist_Print)-1-i]==0:
                continue
            if first is False:
                print ("+",end=" ")
            else:
                first=False
            if i!=0:
                print (dlist_Print[len(dlist_Print)-1-i],"*y(k-",i,")",end="",sep="")
            else:
                print (dlist_Print[len(dlist_Print)-1-i],"*y(k)",end="",sep="")

        print ("=",end="")
        first=True
        for i in range(len(nlist_Print)):
            if nlist_Print[len(nlist_Print)-1-i]==0:
                continue
            if first is False:
                print ("+",end=" ")
            else:
                first=False
            if i!=0:
                print (nlist_Print[len(nlist_Print)-1-i],"*r(k-",i,")",end="",sep="")
            else:
                print (nlist_Print[len(nlist_Print)-1-i],"*r(k)",end="",sep="")
            
