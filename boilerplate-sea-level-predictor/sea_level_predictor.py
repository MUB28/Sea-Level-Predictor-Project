import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv' , float_precision='legacy', dtype='float64')



    # Create scatter plot
    x = df['Year'].values

    y = df['CSIRO Adjusted Sea Level'].values

    plt.scatter(x, y)


    # Create first line of best fit

    x2 = np.arange(1880, 2050, 1)

    slope, intercept, r_value, p_value, std_err  = linregress(x, y)

    plt.plot(x2, (slope*x2) + intercept, 'r')

    


    # Create second line of best fit

    x3 = np.arange(2000, 2050, 1)

    beyond_2000 = df.loc[df['Year'] >= 2000]['Year'].values

    beyond_2000_data = df.loc[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'].values

    slope1, intercept1, r_value1, p_value1, std_err1  = linregress(beyond_2000, beyond_2000_data)

    plt.plot(x3, (slope1*x3) + intercept1, 'g')


    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()