# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:54:07 2019

@author: 862903
"""

def P_RK_IG(V, T, do_ideal_gas=False):
    R = 0.0821  # L-atm/K
    Pc = 37.2   # atm
    Tc = 132.5  # K

    a = 0.427 * pow(R,2) * pow(Tc,2.5) / Pc
    b = 0.0866 * R * Tc / Pc

    # Compute in atm
    P_ig = R * T / V
    P_rk = R * T / (V-b) - a/(V*(V+b)*pow(T,0.5))

    # Convert to Pascals
    if do_ideal_gas:
       return P_ig * 101325
    else:
       return P_rk * 101325

for T in range(490,511,10):
    V = 4.0
    while V < 8:
       print("----- Temperature: " + str(T) + " K")
       print("P_ig: " + str(P_RK_IG(V,T,True)) + " Pa")
       print("P_rk: " + str(P_RK_IG(V,T)) + " Pa")
       V = V + 2.0