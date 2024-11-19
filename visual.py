import matplotlib.pyplot as plt

# Data for each graph
#Line
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
#Scatter
a = [10, 20, 30, 40, 50]
b = [15, 25, 35, 45, 55]
#Bar
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 10, 15, 20, 25]

#Line plot customization
plt.figure(1, figsize=(8, 6))  
plt.plot(x, y, color='#ff6347', linestyle='--', linewidth=2, marker='o', label='Line points')
plt.title('Line Plot of Prime Numbers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()
plt.annotate('Highest peak', (x[y.index(max(y))], max(y)), textcoords="offset points", xytext=(0,5), ha='center')
plt.tight_layout()
plt.savefig('line_plot.png')

#Scatter graph customization
plt.figure(2, figsize=(8, 6))  
plt.scatter(a, b, color='#1e90ff', s=50, marker='^', label='Scatter points')
plt.title('Scatter Plot with Triangle Markers')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.grid(True)
plt.legend()
plt.annotate('40,45', (40, 45), textcoords="offset points", xytext=(0,5), ha='center')
plt.tight_layout()
plt.savefig('scatter_plot.png')

#Bar chart customization
plt.figure(3, figsize=(8, 6))  
plt.bar(categories, values, color='#32cd32', width=0.5, label='Green Bars')
plt.title('Bar Chart with Custom Width')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(True, axis='y')  
plt.legend()
for i, v in enumerate(values):
    plt.text(i, v, str(v), color='#32cd32', ha='center')
plt.tight_layout()
plt.savefig('bar_chart.png')

plt.show()
