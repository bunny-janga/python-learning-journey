# Day 32 – Data Visualization Using Python

## 1. Introduction to Data Visualization

Data Visualization is the process of presenting information in a visual format, such as charts, graphs, and plots.

Instead of reading large amounts of numerical data, we can use graphs to understand information quickly.

### Why Do We Use Data Visualization?

- To understand large datasets easily.
- To identify patterns and trends.
- To compare different values.
- To find unusual data points.
- To communicate information clearly.
- To support better decision-making.

### Real-World Examples

- **Education:** Comparing student marks.
- **Business:** Analyzing monthly sales.
- **Healthcare:** Studying patient information.
- **Finance:** Tracking expenses and profits.
- **Sports:** Comparing player performance.

### Popular Python Visualization Libraries

| Library | Purpose |
|---|---|
| Matplotlib | Creating different types of graphs |
| Seaborn | Creating attractive statistical graphs |
| Plotly | Creating interactive visualizations |
| Bokeh | Creating interactive charts for web applications |

### Installing Required Libraries

Open the VS Code terminal and install Matplotlib, Seaborn, and Pandas.

```bash
pip install matplotlib seaborn pandas
```

### Importing the Libraries

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
```

Here:
- `matplotlib.pyplot` provides functions to create and customize plots.
- `seaborn` helps create statistical visualizations.
- `pandas` helps organize and analyze data.

## 2. Line Plots

A Line Plot is used to display data points connected by straight lines.

It is especially useful for showing changes and trends over time.

### Real-World Uses

- Monthly sales growth.
- Daily temperature changes.
- Stock market trends.
- Student performance over multiple exams.

### Syntax

```python
plt.plot(x, y)
```

### Example: Monthly Sales

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 220]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()
```

**Explanation:**

- `plt.plot()` creates a line plot.
- `marker="o"` displays a circle at each data point.
- `plt.title()` adds a chart title.
- `plt.xlabel()` labels the X-axis.
- `plt.ylabel()` labels the Y-axis.
- `plt.show()` displays the graph.

## 3. Bar Graphs

A Bar Graph represents data using rectangular bars.

It is mainly used to compare values between different categories.

### Real-World Uses

- Comparing student marks.
- Comparing product sales.
- Comparing employee performance.
- Comparing population across cities.

### Syntax

```python
plt.bar(categories, values)
```

### Example: Student Marks

```python
import matplotlib.pyplot as plt

students = ["Rahul", "Priya", "John", "Anu"]
marks = [85, 90, 75, 95]

plt.bar(students, marks)

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
```

**Explanation:**

- `plt.bar()` creates a vertical bar graph.
- Each bar represents one category.
- The height of the bar represents its value.

### Horizontal Bar Graph

We can also create horizontal bars using `plt.barh()`.

```python
plt.barh(students, marks)

plt.title("Student Marks")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()
```

## 4. Pie Charts

A Pie Chart is a circular graph divided into different slices.

Each slice represents a category's proportion of the total.

It is useful when we want to understand how a whole is divided into parts.

### Real-World Uses

- Monthly expense distribution.
- Company market share.
- Budget allocation.
- Product sales percentage.

### Syntax

```python
plt.pie(values, labels=categories)
```

### Example: Monthly Expenses

```python
import matplotlib.pyplot as plt

categories = ["Food", "Travel", "Shopping", "Bills"]
expenses = [3000, 2000, 1500, 3500]

plt.pie(
    expenses,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Monthly Expense Distribution")

plt.show()
```

**Explanation:**

- `plt.pie()` creates a pie chart.
- `labels` displays category names.
- `autopct` displays percentages.
- `startangle` controls the starting angle of the chart.

## 5. Histograms

A Histogram is used to understand the distribution of numerical data.

It groups numerical values into intervals called bins and displays how many values fall within each interval.

Unlike a bar graph, a histogram is mainly used for continuous numerical data.

### Real-World Uses

- Student marks distribution.
- Age distribution.
- Employee salary distribution.
- Exam score analysis.

### Syntax

```python
plt.hist(data, bins=number)
```

### Example: Student Marks Distribution

```python
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()
```

**Explanation:**

- `plt.hist()` creates a histogram.
- `bins=5` divides the data into five intervals.
- `edgecolor` adds borders to the bars.

## 6. Scatter Plots

A Scatter Plot displays individual data points using dots.

It helps us understand the relationship between two numerical variables.

### Real-World Uses

- Study hours versus exam marks.
- Height versus weight.
- Advertising cost versus sales.
- Temperature versus electricity usage.

### Syntax

```python
plt.scatter(x, y)
```

### Example: Study Hours and Marks

```python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [40, 50, 55, 65, 75, 90]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()
```

**Explanation:**

- `plt.scatter()` creates a scatter plot.
- Each dot represents one observation.
- The position of each dot shows the relationship between two values.

## 7. Box Plots

A Box Plot is used to understand the distribution and spread of numerical data.

It helps identify the median, quartiles, and possible outliers.

### Important Terms

- **Minimum:** Lowest value excluding outliers.
- **Q1:** First quartile (25th percentile).
- **Median:** Middle value (50th percentile).
- **Q3:** Third quartile (75th percentile).
- **Maximum:** Highest value excluding outliers.
- **Outliers:** Values unusually far from the rest of the data.

### Real-World Uses

- Comparing student marks.
- Analyzing salary distribution.
- Finding unusual measurements.
- Understanding data spread.

### Example: Student Marks

```python
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 150]

plt.boxplot(marks)

plt.title("Student Marks Distribution")
plt.ylabel("Marks")

plt.show()
```

**Explanation:**

- `plt.boxplot()` creates a box plot.
- The line inside the box represents the median.
- The box represents the middle 50% of the data.
- Individual points beyond the whiskers may represent outliers.

## 8. Heatmaps

A Heatmap uses colors to represent numerical values in a table-like structure.

It helps us identify patterns and relationships in data quickly.

Seaborn provides a simple way to create heatmaps.

### Real-World Uses

- Correlation between variables.
- Student performance analysis.
- Sales performance comparison.
- Website activity analysis.

### Example: Student Marks Heatmap

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Maths": [85, 90, 75],
    "Science": [80, 95, 70],
    "English": [90, 85, 80]
}

df = pd.DataFrame(
    data,
    index=["Rahul", "Priya", "John"]
)

sns.heatmap(df, annot=True, cmap="coolwarm")

plt.title("Student Marks Heatmap")

plt.show()
```

**Explanation:**

- `sns.heatmap()` creates a heatmap.
- `annot=True` displays numerical values inside cells.
- `cmap` controls the color scheme.
- The index contains student names.

## 9. Subplots

Subplots allow us to display multiple graphs inside a single figure.

Instead of opening separate figures for every chart, we can arrange them together.

### Real-World Uses

- Comparing sales and expenses.
- Displaying different student performance charts.
- Comparing multiple datasets.
- Creating analytical dashboards.

### Syntax

```python
plt.subplots(rows, columns)
```

### Example: Multiple Graphs

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 180]
expenses = [80, 100, 90, 130]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# First graph
axes[0].plot(months, sales, marker="o")
axes[0].set_title("Monthly Sales")
axes[0].set_xlabel("Months")
axes[0].set_ylabel("Sales")

# Second graph
axes[1].bar(months, expenses)
axes[1].set_title("Monthly Expenses")
axes[1].set_xlabel("Months")
axes[1].set_ylabel("Expenses")

plt.tight_layout()
plt.show()
```

**Explanation:**

- `plt.subplots(1, 2)` creates one row with two graphs.
- `fig` represents the complete figure.
- `axes` contains the individual plotting areas.
- `axes[0]` accesses the first graph.
- `axes[1]` accesses the second graph.
- `plt.tight_layout()` adjusts spacing between graphs.

## 10. Data Visualization Mini Project – Student Performance Dashboard

Now let's combine different visualization techniques into one small project.

The goal is to analyze student marks using different charts.

### Complete Program

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Student data
data = {
    "Name": ["Rahul", "Priya", "John", "Anu", "Kiran"],
    "Maths": [85, 90, 75, 95, 80],
    "Science": [80, 95, 70, 85, 90],
    "English": [90, 85, 80, 90, 75]
}

df = pd.DataFrame(data)

# Calculate total marks
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)

# Calculate average marks
df["Average"] = df["Total"] / 3

# Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1. Bar graph
axes[0, 0].bar(df["Name"], df["Total"])
axes[0, 0].set_title("Total Marks")
axes[0, 0].set_xlabel("Students")
axes[0, 0].set_ylabel("Marks")

# 2. Line plot
axes[0, 1].plot(df["Name"], df["Average"], marker="o")
axes[0, 1].set_title("Average Marks")
axes[0, 1].set_xlabel("Students")
axes[0, 1].set_ylabel("Average")

# 3. Pie chart
axes[1, 0].pie(
    df["Total"],
    labels=df["Name"],
    autopct="%1.1f%%"
)
axes[1, 0].set_title("Marks Contribution")

# 4. Scatter plot
axes[1, 1].scatter(df["Maths"], df["Science"])
axes[1, 1].set_title("Maths vs Science")
axes[1, 1].set_xlabel("Maths Marks")
axes[1, 1].set_ylabel("Science Marks")

plt.tight_layout()
plt.show()

# Display student data
print(df)
```

### Sample Output (Terminal)

```text
    Name  Maths  Science  English  Total    Average
0  Rahul     85       80       90    255  85.000000
1  Priya     90       95       85    270  90.000000
2   John     75       70       80    225  75.000000
3    Anu     95       85       90    270  90.000000
4  Kiran     80       90       75    245  81.666667
```

The program also displays four graphs in a single dashboard.

## 11. Important Matplotlib and Seaborn Functions

| Function | Purpose |
|---|---|
| `plt.plot()` | Creates a line plot |
| `plt.bar()` | Creates a vertical bar graph |
| `plt.barh()` | Creates a horizontal bar graph |
| `plt.pie()` | Creates a pie chart |
| `plt.hist()` | Creates a histogram |
| `plt.scatter()` | Creates a scatter plot |
| `plt.boxplot()` | Creates a box plot |
| `sns.heatmap()` | Creates a heatmap |
| `plt.subplots()` | Creates multiple plotting areas |
| `plt.title()` | Adds a chart title |
| `plt.xlabel()` | Labels the X-axis |
| `plt.ylabel()` | Labels the Y-axis |
| `plt.legend()` | Displays a legend |
| `plt.grid()` | Displays grid lines |
| `plt.show()` | Displays the figure |
| `plt.savefig()` | Saves the figure as an image |

## 12. How to Run the Project in VS Code

1. Open Visual Studio Code.
2. Create a Python file named `data_visualization.py`.
3. Open the terminal.
4. Install the required libraries:

```bash
pip install matplotlib seaborn pandas
```

5. Copy the project program into the file.
6. Save the file.
7. Run the program:

```bash
python data_visualization.py
```

The dashboard will open in a separate plotting window.

## 13. What I Learned Today

After completing Day 32, I understood:

- What Data Visualization means.
- How to use Matplotlib and Seaborn.
- How to create line plots and bar graphs.
- How to display data using pie charts.
- How to understand numerical distributions using histograms.
- How to identify relationships using scatter plots.
- How to identify outliers using box plots.
- How to create heatmaps.
- How to display multiple graphs using subplots.
- How to build a Student Performance Dashboard.

## 14. Day 32 – Quick Revision

| Chart | Main Purpose |
|---|---|
| Line Plot | Shows trends over time |
| Bar Graph | Compares categories |
| Pie Chart | Shows proportions of a whole |
| Histogram | Displays numerical data distribution |
| Scatter Plot | Shows relationships between two numerical variables |
| Box Plot | Shows spread, median, quartiles, and possible outliers |
| Heatmap | Displays values using colors |
| Subplots | Displays multiple graphs in one figure |

**Day 32 completed: Data Visualization using Matplotlib and Seaborn.**
