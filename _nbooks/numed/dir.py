import numpy as np

def metodo_rk4_matrix(f,tsim,y0,h):
    ti = tsim[0]
    tf = tsim[1]
    yi = np.array(y0)
    T = [ti]
    Y = [yi]

    while ti < tf:
        k1 = f(ti, yi)
        k2 = f(ti + 0.5*h, yi + 0.5*k1*h)
        k3 = f(ti + 0.5*h, yi + 0.5*k2*h)
        k4 = f(ti + h, yi + k3*h)
        yi = yi + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        ti = ti + h

        T.append(ti)
        Y.append(yi)
    
    return np.array(T), np.array(Y)


def metodo_rk4(f,tsim,y0,h,show=False,latex=False):
    ti = tsim[0]
    tf = tsim[1]
    yi = np.array(y0)
    T = [ti]
    Y = [yi]

    while ti < tf:
        k1 = f(ti, yi)
        k2 = f(ti + 0.5*h, yi + 0.5*k1*h)
        k3 = f(ti + 0.5*h, yi + 0.5*k2*h)
        k4 = f(ti + h, yi + k3*h)
        yi = yi + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        ti = ti + h

        T.append(ti)
        Y.append(yi)
        
        if show: 
            for ii in range(len(k1)):
                print(f"ti={ti:0.2f} k1={k1[ii]:0.4f} k2={k2[ii]:0.6f} k3={k3[ii]:0.6f} k4={k4[ii]:0.4f} yi={yi[ii]:0.4f}")
        if latex: 
            latex_str = ""
            for ii in range(len(k1)):
                latex_str += f"{ti:0.2f} & {k1[ii]:0.4f} & {k2[ii]:0.4f} & {k3[ii]:0.4f} & {k4[ii]:0.4f} & {yi[ii]:0.4f}\\\\ \n"
            print(latex_str)
    
    return np.array(T), np.array(Y)



def metodo_euler(f,tsim,y0,h):
    ti = tsim[0]
    tf = tsim[1]
    yi = np.array(y0)
    T = [ti]
    Y = [yi]

    while ti < tf:
        yi = yi + h*f(ti, yi)
        ti = ti + h

        T.append(ti)
        Y.append(yi)
    
    return np.array(T), np.array(Y)


def metodo_euler_anterior(f,x0,xf,y0,h):
    yn = y0
    xn = x0
    XN = [xn]
    YN = [yn]

    while xn < xf:
        yn = yn + h*f(xn,yn)
        xn = xn + h

        XN.append(xn)
        YN.append(yn)
    
    return XN, YN


def metodo_euler_so(f,t0,tf,q10,u0,h):
    tn = t0
    q1n = q10
    un = u0
    TN = [tn]
    Q1N = [q1n]
    UN = [un]

    while tn < tf:
        ftqu = f(tn,q1n,un)
        q1n = q1n + h*un
        un = un + h*ftqu
        tn = tn + h

        TN.append(tn)
        Q1N.append(q1n)
        UN.append(un)
    
    return TN, Q1N, UN