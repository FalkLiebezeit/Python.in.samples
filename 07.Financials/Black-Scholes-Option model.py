import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Black-Scholes formula for a European call and put option
def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Calculate the Black-Scholes price for a European option.

    Parameters:
        S : float - Current stock price
        K : float - Strike price
        T : float - Time to maturity (in years)
        r : float - Risk-free interest rate (annual, as a decimal)
        sigma : float - Volatility of the underlying asset (annual, as a decimal)
        option_type : str - 'call' for call option, 'put' for put option

    Returns:
        float: Option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    return price

# Parameters for the diagram
K = 100      # Strike price
T = 1        # Time to maturity (1 year)
r = 0.05     # Risk-free interest rate (5%)
sigma = 0.2  # Volatility (20%)

# Range of stock prices for plotting
S_values = np.linspace(50, 150, 200)

# Calculate call and put prices for each stock price
call_prices = [black_scholes(S, K, T, r, sigma, option_type='call') for S in S_values]
put_prices = [black_scholes(S, K, T, r, sigma, option_type='put') for S in S_values]

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(S_values, call_prices, label='Call Option Price', color='blue')
plt.plot(S_values, put_prices, label='Put Option Price', color='red')
plt.axvline(K, color='gray', linestyle='--', label='Strike Price')
plt.xlabel('Stock Price (S)')
plt.ylabel('Option Price')
plt.title('Black-Scholes Option Prices vs. Stock Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()