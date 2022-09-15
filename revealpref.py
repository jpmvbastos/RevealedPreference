""""
Revealed Preferences
See: https://github.com/jpmvbastos/RevealedPreference
Author: João Pedro Bastos 
Version: September 2022
"""

import numpy as np
import pandas as pd


def revealpref(prices, quantities):
    """"
    This function check if choices are consistent with Weak Axiom of Revealed Preferences
    
    Parameters
    ----------
    prices: DataFrame or Series object
        Data on prices. Each column should represent one good, and each line a different period of time.

    quantities: DataFrame or Series object    
        Data on quantities. Each column should represent one good, and each line a different period of time.

    axiom: {"warp", "sarp", "both"}, default="both"

        Check if choices among bundles satisfy the Weak Axiom of Revelead Preferences (WARP), the Strong Axiom of Revelead Preferences (SARP), or both.

    print: True, False

        Prints the comparison of each bundle in the set. 

    axiom='warp', print=False

    """   

    if prices.shape != quantities.shape:
        raise IndexError("Number of prices and quantities are different. Check dimensions of tables.")
    
    else:
        pq = np.array([])
        for i in range(0,len(prices)):
            for j in range(0,len(prices)):
                pq = np.append(pq,sum(prices.iloc[i,:]*quantities.iloc[j,:]))            
    rows = ["p"+str(i) for i in range(0,len(prices))]
    columns = ["q"+str(i) for i in range(0,len(prices))]
    pq=pd.DataFrame(pq.reshape((len(prices),len(prices))),columns=columns, index=rows)

    #if axiom =="both":
    #if print==True: 

#Check WARP
    for i in range(0,len(prices)):
        for j in range(0,len(prices)):
            if pq.iloc[i,i] >= pq.iloc[i,j] and pq.iloc[j,j] < pq.iloc[j,i]:     
                    print("Bundle " + str(i) +" (= "+ str(pq.iloc[i,i]) + ") is revealed preferred (>=) to bundle " + str(j) + " (= " +str(pq.iloc[i,j]) + ")",
                            "       and bundle " + str(j) + " (= "+ str(pq.iloc[j,j]) + ") is NOT revealed preferred (>/) bundle " + str(i) + " (= " +str(pq.iloc[j,i]) + ")", 
                            "           These choices are consistent with the Weak Axiom of Revealed Preferences (WARP).", sep=os.linesep)
            else:
                continue
            
            if (pq.iloc[i,i] >= pq.iloc[i,j] and pq.iloc[j,j] < pq.iloc[j,i]) or pq.iloc[i,i] == pq.iloc[j,j]:
                continue

            else: 
                print("Choices among bundles " + str(i) + " (=" + str(pq.iloc[i,i]) + ") and " + str(j) + " (=" + str(pq.iloc[i,j]) + ") violate the Weak Axiom of Revelead Preferences.")                

#Check SARP        
    if [pq.iloc[i,i] >= pq.iloc[i,i+1] for i in range(0,len(prices)-1)] and pq.iloc[len(prices)-1,len(prices)-1] < pq.iloc[len(prices)-1,0]:
        print("These choices also satisfy SARP!")

    else:
        print("These choices do NOT satisfy SARP!")
            

