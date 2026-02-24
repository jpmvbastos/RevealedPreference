""""
Revealed Preferences
See: https://github.com/jpmvbastos/RevealedPreference
Author: João Pedro Bastos
Version: September 2022
"""

import math
import numpy as np
import pandas as pd


def revealpref(prices, quantities, axiom='both', print_results=True):

    if prices.shape != quantities.shape:
        raise IndexError("Number of prices and quantities are different. Check dimensions of tables.")

    n = len(prices)

    # Build expenditure matrix: pq[i,j] = cost of bundle j at prices i
    pq = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            pq[i, j] = sum(prices.iloc[i,:] * quantities.iloc[j,:])
    rows = ["p"+str(i) for i in range(n)]
    columns = ["q"+str(i) for i in range(n)]
    pq = pd.DataFrame(pq, columns=columns, index=rows)

    # Construct RP table: RP[i,j] = 1 if bundle i is directly revealed preferred to bundle j
    index = [str(i+1) for i in range(n)]
    RP = pd.DataFrame(np.zeros([n, n]), columns=index, index=index)
    for i in range(n):
        for j in range(n):
            if pq.iloc[i,i] >= pq.iloc[i,j]:
                RP.iloc[i,j] = 1

    # Compute transitive closure of RP via Floyd-Warshall (used for SARP)
    # TC[i,j] = True if bundle i is directly OR transitively revealed preferred to bundle j
    TC = RP.values.astype(bool).copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                TC[i,j] = TC[i,j] or (TC[i,k] and TC[k,j])

    # Number of unordered off-diagonal pairs (the meaningful comparisons)
    n_comparisons = n * (n - 1) // 2

    def _check_warp():
        n_violations = 0
        for i in range(n):
            for j in range(n):
                if i != j and RP.iloc[i,j] == 1 and RP.iloc[j,i] == 1:
                    n_violations += .5  # each pair is encountered twice in the double loop
                    if print_results:
                        print("Choices between bundles " + str(i+1) + " and " + str(j+1) + " violate the Weak Axiom of Revealed Preference (WARP)")
        if print_results:
            if n_comparisons > 0:
                print(str(n_violations / n_comparisons * 100) + "% of the choices violate WARP")
            else:
                print("Only one observation — no comparisons to make.")

    def _check_sarp():
        sarp_violated = any(
            TC[i,j] and TC[j,i]
            for i in range(n) for j in range(n) if i != j
        )
        if print_results:
            if sarp_violated:
                print("These choices do not satisfy SARP!")
            else:
                print("These choices satisfy SARP!")

    if axiom == 'both':
        _check_warp()
        _check_sarp()
        return RP

    elif axiom == 'warp':
        _check_warp()
        return RP

    elif axiom == 'sarp':
        _check_sarp()
        return RP

    else:
        raise ValueError("Please select an axiom {'both', 'warp', 'sarp'} or leave it blank for both")
