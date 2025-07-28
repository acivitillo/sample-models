# Constants
average_coffee_price = 3.0  # Average price of coffee in euros
fixed_costs = 1000.0  # Monthly fixed costs in euros (rent, utilities, etc.)
variable_cost_per_client = 1.0  # Variable cost per client in euros (ingredients, etc.)
desired_profit = 1000.0  # Desired profit per month in euros

# Calculate total costs
total_costs = fixed_costs + desired_profit

# Calculate the number of clients needed per month
clients_needed_per_month = total_costs / (average_coffee_price - variable_cost_per_client)

# Calculate the number of clients needed per day (assuming 30 days in a month)
clients_needed_per_day = clients_needed_per_month / 30

# Print the result
print(f"Clients needed per day to be profitable: {clients_needed_per_day:.2f}")