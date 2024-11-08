import numpy as np

# Дані
decisions = {
    'x1': [6.0, 6.2, 5.5],
    'x2': [7.5, 7.1, 7.0],
    'x3': [7.4, 7.5, 8.0],
    'x4': [7.0, 5.8, 6.0]
}
probabilities = [0.3, 0.5, 0.2]

# Розрахунок очікуваного значення
expected_values = {}
for decision, outcomes in decisions.items():
    expected_values[decision] = sum(p * x for p, x in zip(probabilities, outcomes))

# Розрахунок семіваріації та коефіцієнта семіваріації
semivariances = {}
coefficients = {}

for decision, outcomes in decisions.items():
    mean = expected_values[decision]
    downside_outcomes = [(p, (x - mean) ** 2) for p, x in zip(probabilities, outcomes) if x < mean]
    
    if downside_outcomes:
        semivariance = sum(p * sq_diff for p, sq_diff in downside_outcomes) / sum(p for p, _ in downside_outcomes)
    else:
        semivariance = 0  # Якщо немає значень менших за середнє
    
    semivariances[decision] = semivariance
    coefficients[decision] = semivariance / mean if mean != 0 else float('inf')  # Запобігаємо діленню на нуль

# Вибір оптимальних рішень
optimal_semivariance = min(semivariances, key=semivariances.get)
optimal_coefficient = min(coefficients, key=coefficients.get)

# Виведення результатів
print("Очікувані значення:", expected_values)
print("Семіваріації:", semivariances)
print("Коефіцієнти семіваріації:", coefficients)
print("Оптимальне рішення за мінімальною семіваріацією:", optimal_semivariance)
print("Оптимальне рішення за мінімальним коефіцієнтом семіваріації:", optimal_coefficient)
