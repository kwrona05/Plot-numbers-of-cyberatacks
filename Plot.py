import matplotlib.pyplot as plt

# Data for the chart
categories = ["Cyberprzestępstwa", "Ogólna liczba przestępstw"]
values = [83000, 792000]

# Creating the bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(categories, values, color=['skyblue', 'orange'])

# Adding labels to the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height):,}', 
             ha='center', va='bottom', fontsize=12)

# Customizing the chart
plt.title("Porównanie liczby cyberprzestępstw z ogólną liczbą przestępstw w Polsce (2023)", fontsize=14)
plt.ylabel("Liczba przestępstw", fontsize=12)
plt.ylim(0, 850000)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Displaying the chart
plt.tight_layout()
plt.show()