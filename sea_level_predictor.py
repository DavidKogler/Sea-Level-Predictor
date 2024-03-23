import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(range(df['Year'].min(), 2051, 1), result.slope * range(df['Year'].min(), 2051, 1) + result.intercept, color='orange', label=str(df['Year'].min()) + '-2050')

    # Create second line of best fit
    result = linregress(df.loc[df['Year']>= 2000, 'Year'], df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051, 1), result.slope * range(2000, 2051, 1) + result.intercept, color='red', label='2000-2050')
    
    # Add labels and title
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()