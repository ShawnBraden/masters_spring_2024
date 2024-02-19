import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from fitter import Fitter, get_common_distributions

class European_Call_Payoff:
    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self, stock_price):
        if stock_price > self.strike:
            return stock_price - self.strike
        else:
            return 0

class BetaMotion:
    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.beta(20, 8) - 0.25  # Beta motion with shift to left of .65
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            # print("Change in price: {0}", dYt)
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Accound for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()

class part_1():
    def __init__(self, strike = 100) -> None:
        # Model Parameters
        paths = 5000
        initial_price = 100
        drift = .01
        volatility = .7
        dt = 1/365
        T = 1
        price_paths = []
        strike_price = strike

        # Generate a set of sample paths
        for i in range(0, paths):
            price_paths.append(BetaMotion(initial_price, drift, volatility, dt, T).prices)

        call_payoffs = []
        final_prices = []
        ec = European_Call_Payoff(strike_price)
        risk_free_rate = .01
        for price_path in price_paths:
            call_payoffs.append(ec.get_payoff(price_path[-1])/(1 + risk_free_rate))  # We get the last stock price in the series generated to determine the payoff and discount it by one year
            final_prices.append(price_path[-1])

        # Plot the set of generated sample paths
        for price_path in price_paths:
            plt.plot(price_path)
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.title("Simulations of Stock Price Based on Beta Distribution")
        plt.show()

        print(f"Average stock price after {int(1 / dt) * T} days: $", np.average(final_prices))
        print("\nAverage payoff(option block of 100): $", np.average(call_payoffs)*100)  # Options are in blocks of 100
        print("Cost of option: $", np.average(call_payoffs))

class part_2():
    def __init__(self) -> None:

        print('------- Fitting Distrabutions: -------')
        # Load datasets
        dataset1 = pd.read_csv("stock1.csv")
        dataset2 = pd.read_csv("stock2-1.csv")

        plt.figure(1)
        plt.hist(dataset1, bins=100, alpha=0.5, color='blue', label='Stock 1')
        plt.legend()

        # Define common distributions
        distributions = get_common_distributions()

        # Fitting distributions for dataset 1
        f1 = Fitter(dataset1, distributions=distributions)
        f1.fit(progress=False)
        best_fit1 = f1.get_best(method='sumsquare_error')
        f1.summary()

        plt.figure(2)
        plt.hist(dataset2, bins=100, alpha=0.5, color='red', label='Stock 2')
        plt.legend()

        # Fitting distributions for dataset 2
        f2 = Fitter(dataset2, distributions=distributions)
        f2.fit(progress=False)
        best_fit2 = f2.get_best(method='sumsquare_error')
        f2.summary()

        plt.tight_layout()
        plt.show()

        print(f"Best fitting distribution for stock 1 using sumsquare_error: {best_fit1}")
        print(f"Best fitting distribution for stock 2 using sumsquare_error: {best_fit2}")

        print('\n------- New simultaions Using new options: -------')

        print('\n------- Using the Avg of both stockes: -------')
        avg_one = np.average(dataset1)
        avg_two = np.average(dataset2)
        avg_both = (avg_one + avg_two) / 2
        print(f"Avg of both options: {avg_both}")
        print("Rerunning simulation with new strike price.")
        part_1(strike=avg_both)
        print()

        print('\n------- New simultaions Using max of stock 1: -------')
        max_val_1 = np.max(dataset1)
        print(f"Max of stock 1 {max_val_1}")
        print("Rerunning simulation with new strike price.")
        part_1(strike=max_val_1)
        print()
        
        print('\n------- New simultaions Using max of stock 2: -------')
        max_val_2 = np.max(dataset2)
        print(f"Max of stock 1 {max_val_2}")
        print("Rerunning simulation with new strike price.")
        part_1(strike=max_val_2)

def main():
    print()
    print("############## Part 1 ##############")
    part1 = part_1()
    print()
    print("############## Part 2 ##############")
    part2 = part_2()
main()