import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def import_data(file_path):
    """
    Reads the kinetics CSV file and returns a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def bisubstrate_michaelis_menten(S, Vmax, Km1, Km2): 
    """
    Calculates the rate of a bisubstrate (S1 and S2) reaction.
    """
    S1, S2 = S
    return (Vmax * S1 * S2) / (Km1 * Km2 + Km2 * S1 + Km1 * S2 + S1 * S2)

def fit_bisubstrate_kinetics(data):
    """
    Fits the bisubstrate kinetics data to the bisubstrate
    equation using curve fitting.
    """ 
    S1 = data['S1'].values
    S2 = data['S2'].values
    S = (S1, S2)
    rate = data['Rate'].values
    params, _ = curve_fit(bisubstrate_michaelis_menten, S, rate)
    
    return params

def r_squared(): 
    """
    Calculates the R-squared value for the fitted curve.
    """
    # Placeholder for R-squared calculation
    pass

def chi_squared(): 
    """
    Calculates the chi-squared value for the fitted curve.
    """
    # Placeholder for chi-squared calculation
    pass

def main():     
    file_path = 'Kinetics.csv'
    data = import_data(file_path)
    
    if data is not None:
        parameters = fit_bisubstrate_kinetics(data)
        print(f"Fitted parameters: Vmax={parameters[0]}, Km1={parameters[1]}, Km2={parameters[2]}")
    else:
        print("No data to plot.")

if __name__ == "__main__":
    main()






