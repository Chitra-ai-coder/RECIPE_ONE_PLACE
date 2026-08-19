import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
try:
    df = pd.read_csv('Cleaned_Indian_Food_Dataset.csv')
    print(f"Total Recipes: {len(df)}")
except FileNotFoundError:
    print("Error: CSV file not found!")
    exit()

# 2. Count recipes per Cuisine
cuisine_counts = df['Cuisine'].value_counts()

# 3. Setup the visualization
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")

# We'll plot the top 20 cuisines so the chart remains readable
top_n = 20
sns.barplot(x=cuisine_counts.head(top_n).values, 
            y=cuisine_counts.head(top_n).index, 
            palette="viridis")

# 4. Add labels and title
plt.title(f'Top {top_n} Cuisines by Recipe Count', fontsize=16, fontweight='bold')
plt.xlabel('Number of Recipes', fontsize=12)
plt.ylabel('Cuisine', fontsize=12)

# Add the exact count on the end of each bar
for i, v in enumerate(cuisine_counts.head(top_n).values):
    plt.text(v + 3, i + .25, str(v), color='black', fontweight='bold')

plt.tight_layout()

# 5. Save the visualization as an image
plt.savefig('cuisine_distribution.png')
print("✅ Visualization saved as 'cuisine_distribution.png'")

# 6. Show the plot
plt.show()