import math
import sys

class Bnet:
    def __init__(self):
        pass

    def main(self):

        if len(sys.argv)<2:
            print("no aruguments were given provide valid values")
        else:
            given = False
            e=""
            q=""
            for i in sys.argv:

                if i=="given":
                    given = True
                    continue
                if len(i)>=3:
                    continue
                if given==True:
                    e+=i
                else:
                    q+=i
            # print(e)
            # print(q)
            s = sys.argv[1]
            lis = []
            with open(s,"r") as f:
                for i in f:
                    values = i.split()  # split by whitespace, default separator
                    f1=[]
                    for j in values:
                        f1.append(int(j))
                    lis.append(f1)
            b = [0]*2
            g = [[0 for j in range(2)] for i in range(2)]
            c = [0]*2
            f = [[[0 for k in range(2)] for j in range(2)] for i in range(2)]
            for i in lis:
                b[i[0]]+=1
                g[i[0]][i[1]]+=1
                c[i[2]]+=1
                f[i[1]][i[2]][i[3]]+=1

            b_p = [0.]*2
            g_p = [[0. for j in range(2)] for i in range(2)]
            c_p = [0.]*2
            f_p = [[[0. for k in range(2)] for j in range(2)] for i in range(2)]
            for i in range(2):
                b_p[i]  = b[i]/len(lis)
                for j in range(2):

                    g_p[i][j] = g[i][j]/b[i]
                    for k in range(2):
                        fr = 0
                        c_p[k] = c[k]/len(lis)
                        for l in range(2):
                            fr += f[j][k][l]
                        for l in range(2):
                            f_p[j][k][l] = f[j][k][l]/fr
            res = [[[[0. for k in range(2)] for j in range(2)] for i in range(2)] for l in range(2)]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        for l in range(2):
                            res[i][j][k][l] = b_p[i]*c_p[k]*g_p[i][j]*f_p[j][k][l]
                            # print(res[i][j][k][l])
            if "Bt" in q:
                b2=1
            else:
                b2=0
            if "Gt" in q:
                g2=1
            else:
                g2=0
            if "Ct" in q:
                c2=1
            else:
                c2=0
            if "Ft" in q:
                f2=1
            else:
                f2=0
            if "Bt" in e:
                b3=1
            elif "Bf" in e:
                b3=0
            else:
                b3=-1
            if "Gt" in e:
                g3=1
            elif "Gf" in e:
                g3=0
            else:
                g3=-1
            if "Ct" in e:
                c3=1
            elif "Cf" in e:
                c3=0
            else:
                c3 = -1
            if "Ft" in e:
                f3=1
            elif "Ff" in e:
                f3=0
            else:
                f3 = -1

            res_e = 0.
            res_q = 0.
            res1 = [[[[0. for i in range(2)] for j in range(2)] for k in range(2)] for l in range(2)]
            if c3>=0 or b3>=0 or g3>=0 or f3>=0:
                for i in range(2):
                    for j in range(2):
                        for k in range(2):
                            for l in range(2):
                                if (b3<0 or i == b3) and (g3<0 or j==g3) and (c3<0 or c3==k) and (f3<0 or f3==l):
                                    res_e = res_e + res[i][j][k][l]
                                    if (b2<0 or i == b2) and (g2<0 or j==g2) and (c2<0 or c2==k) and (f2<0 or f2==l):
                                        res_q = res_q+ res[i][j][k][l]
            else:
                for i in range(2):
                    for j in range(2):
                        for k in range(2):
                            for l in range(2):
                                res_e = res_e + res[i][j][k][l]
                                if (b2<0 or i == b2) and (g2<0 or j==g2) and (c2<0 or c2==k) and (f2<0 or f2==l):
                                    res_q = res_q+ res[i][j][k][l]
            # print(res_q,res_e)
            # print(b2,g2,c2,f2)
            if res_e == 0:
                print("evidence is invalid",-1)
            else:
                print("probability",res_q/res_e)



s = Bnet()
s.main()
