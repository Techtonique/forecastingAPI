import forecastingapi as fapi
import numpy as np
import pandas as pd 
from time import time
import matplotlib.pyplot as plt
import ast 

# examples in https://github.com/Techtonique/datasets/tree/main/time_series        
path_to_file = 'https://raw.githubusercontent.com/Techtonique/datasets/refs/heads/main/time_series/univariate/AirPassengers.csv'
#path_to_file = '/Users/t/Documents/datasets/time_series/univariate/AirPassengers.csv' 
    
start = time() 
res_get_forecast = fapi.get_forecast(path_to_file,     
base_model="RidgeCV",
n_hidden_features=5,
lags=25,
type_pi='scp2-kde',
replications=10,
h=10)
print(f"Elapsed: {time() - start} seconds \n")

print(res_get_forecast)

# Convert lists to numpy arrays for easier handling
mean = np.asarray(res_get_forecast['mean']).ravel()
lower = np.asarray(res_get_forecast['lower']).ravel()
upper = np.asarray(res_get_forecast['upper']).ravel()
sims = np.asarray(res_get_forecast['sims'])

# Plotting
plt.figure(figsize=(10, 6))

# Plot the simulated lines
for sim in sims:
    plt.plot(sim, color='gray', linestyle='--', alpha=0.6, label='Simulations' if 'Simulations' not in plt.gca().get_legend_handles_labels()[1] else "")

# Plot the mean line
plt.plot(mean, color='blue', linewidth=2, label='Mean')

# Plot the lower and upper bounds as shaded areas
plt.fill_between(range(len(mean)), lower, upper, color='lightblue', alpha=0.2, label='Prediction Interval')

# Labels and title
plt.xlabel('Time Point')
plt.ylabel('Value')
plt.title('Spaghetti Plot of Mean, Bounds, and Simulated Paths')
plt.legend()
plt.show()

