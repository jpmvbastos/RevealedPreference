""""
Revealed Preferences
See: https://github.com/jpmvbastos/RevealedPreference
Author: João Pedro Bastos 
Version: September 2022
"""

import numpy as np
import pandas as pd


def revealpref(prices, quantities, axiom='both', print_results=True):
    
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

    #Construct RP table 
    index = [str(i+1) for i in range(0,len(prices))]
    RP = pd.DataFrame(np.zeros([len(prices),len(prices)]),columns=index, index=index)
    n_violations = 0
    n_comparisons = 0
    for i in range(0,len(prices)):
        for j in range(0,len(prices)):
            n_comparisons +=.5
            if pq.iloc[i,i] >= pq.iloc[i,j] or i==j:
                RP.iloc[i,j] = 1       
            else:
                pass

    if axiom=='both': #Check both
        #Check WARP
                      
        #Check WARP violations              
        for i in range(0,len(prices)):       
            for j in range(0,len(prices)):
                if RP.iloc[i,j]==RP.iloc[j,i] and i!=j:
                    n_violations+=.5
                    if print_results==True:
                        print("Choices between bundles " + str(i+1) + " and " + str(j+1) + " violate the Weak Axiom of Revelead Preference (WARP)")  
                    else:
                        pass                                       
                else:
                    pass
        print(str(n_violations/n_comparisons*100) + "% of the choices violate WARP")
            

        #Check SARP
        sarp_count=0         
        if [RP.iloc[i,i-1]==1 for i in range(1,len(prices))]: # Checks if Bundle N is RP to bundle N-1 for all N>1
                sarp_count+=1
        elif RP.iloc[0,len(prices)-1]==1: #Checks if bundle 1 is RP to bundle N
            print('These choices do no satisfy SARP!')
        else:
            pass
        if sarp_count==len(prices):        
            print('These choices satisfy SARP!')
        else:
            print('These choices do no satisfy SARP!')
    
        return RP

    elif axiom=='warp':  #Check only WARP                                    
        
        for i in range(0,len(prices)):       
            for j in range(0,len(prices)):
                if RP.iloc[i,j]==RP.iloc[j,i] and i!=j:
                    n_violations+=.5                   
                    if print_results==True:
                            print("Choices between bundles " + str(i+1) + " and " + str(j+1) + " violate the Weak Axiom of Revelead Preference (WARP)")  
                    else:
                        pass                                                             
                else:
                    continue
        print(str(n_violations/n_comparisons*100) + "% of the choices violate WARP")
        return RP
    
    elif axiom=='sarp':  # Check only SARP
        sarp_count=0         
        if [RP.iloc[i,i-1]==1 for i in range(1,len(prices))]: # Checks if Bundle N is RP to bundle N-1 for all N>1
                sarp_count+=1
        elif RP.iloc[0,len(prices)-1]==1: #Checks if bundle 1 is RP to bundle N
            print('These choices do no satisfy SARP!')
        else:
            pass
        if sarp_count==len(prices): 
            print('These choices satisfy SARP!')
        else:
            print('These choices do no satisfy SARP!')

    else:
        raise "Please select an axiom {'both', 'warp', 'sarp'} or leave it blank for both"                
