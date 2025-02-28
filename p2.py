import math
import sys

class Bnet:
    def __init__(self):
        pass

    def main(self):
        if len(sys.argv)<6 or len(sys.argv)>6:
            print("no aruguments were given provide valid values")
        else:
            s = sys.argv[1]
            lis = []
            with open(s,"r") as f:
                for i in f:
                    values = i.split()  # split by whitespace, default separator
                    f1=[]
                    for j in values:
                        f1.append(int(j))
                    lis.append(f1)
            if sys.argv[2] =="Bt":
                b1 = 1
            else:
                b1=0
            if sys.argv[3] == "Gt":
                g1 = 1
            else:
                g1 = 0
            if sys.argv[4] == "Ct":
                c1 = 1
            else:
                c1 = 0
            if sys.argv[5] == "Ft":
                f1 = 1
            else:
                f1 = 0
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
            print("probability",res[b1][g1][c1][f1])
s = Bnet()
s.main()
