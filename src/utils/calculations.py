def calculate_years_to_millionaire(current_savings, monthly_contribution, annual_interest_rate):
    target_amount = 1_000_000
    years = 0
    total_savings = current_savings

    while total_savings < target_amount:
        total_savings += monthly_contribution * 12
        total_savings *= (1 + annual_interest_rate)
        years += 1

    return years

def suggest_investment_options(current_savings, monthly_contribution, years_to_millionaire):
    suggestions = []
    
    if current_savings < 10000:
        suggestions.append("Consider starting with a high-yield savings account.")
    
    if monthly_contribution < 500:
        suggestions.append("Increase your monthly contributions to at least $500 for better growth.")
    
    if years_to_millionaire > 20:
        suggestions.append("Look into stock market investments or mutual funds for higher returns.")
    
    if years_to_millionaire <= 20 and years_to_millionaire > 10:
        suggestions.append("Consider a diversified portfolio including stocks, bonds, and ETFs.")
    
    if years_to_millionaire <= 10:
        suggestions.append("Explore aggressive investment strategies, such as index funds or real estate.")
    
    return suggestions