# Midterm Exam - AI and ML for Cybersecurity
**Student:** Giorgi Bedoshvili
**ID:** g_bedoshvili25
**Date:** January 9, 2026

## Assignment 1: Finding the Correlation (10 Points)

### 1.1 Data Collection Process
To find the correlation, I accessed the online resource provided in the assignment. The process involved:
* **Interactive Extraction:** I visited `max.ge/aiml_midterm/56234_html/` where data was displayed as blue dots.
* **Coordinate Recording:** By hovering over each point, I manually recorded the X and Y coordinates.

![Step 1: Website Interface](1.png)
*Figure 1: Accessing the data points on the provided web portal.*

### 1.2 Implementation in PyCharm
I implemented the Pearson correlation calculation using Python in the PyCharm environment. 
* **Backend Fix:** To avoid Tcl/Tk errors, I used `matplotlib.use('Agg')` for non-interactive rendering.
* **Calculation:** Used `numpy.corrcoef` to determine the strength of the linear relationship.

![Step 2: PyCharm Environment](2.png)
*Figure 2: Python code implementation and environment setup.*

### 1.3 Results and Output
The execution was successful, resulting in a high correlation coefficient.
* **Pearson's Correlation Coefficient (r):** 0.9890
* **Interpretation:** This value indicates a very strong positive linear correlation between the coordinates.

![Step 3: Execution Result](3.png)
*Figure 3: Console output showing the calculated correlation coefficient.*

### 1.4 Mathematical Formula
The coefficient was calculated based on the following formula:
$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

### 1.5 Final Visualization
The generated graph illustrates the data points along with the calculated trend line:

![Correlation Graph](correlation_graph.png)
*Figure 4: Final scatter plot with regression line.*


---
## Assignment 2: Spam Email Detection (20 Points)

### 2.1 Data Source
The dataset for this task has been uploaded to the repository as required.
* **Link to Data File:** [g_bedoshvili25_56234.csv](./g_bedoshvili25_56234.csv)

2.2 Implementation in PyCharmI developed a machine learning pipeline using the scikit-learn library.Backend Fix: To ensure compatibility with the PyCharm environment and avoid Tcl/Tk errors, I used matplotlib.use('Agg').Algorithm: I utilized the LogisticRegression algorithm to build the predictive model.Warnings Handling: I implemented warnings.filterwarnings('ignore') to ensure a clean console output.Figure 5: Python implementation and successful script execution in PyCharm.2.3 Results and Model EvaluationThe model showed exceptional performance on the test data, achieving high accuracy.Accuracy Score: 0.9680 (96.8%)Model Parameters:Coefficients: [[0.00799, 0.91153, 0.44636, 0.76820]]Intercept: -9.425282.4 Mathematical FoundationThe model predicts the probability of an email being spam using the Sigmoid Function:$$P(y=1|x) = \frac{1}{1 + e^{-(\beta_0 + \sum \beta_i x_i)}}$$2.5 Visualization: Class DistributionAs part of the data insights (Requirement 2.7), I generated a bar chart to study the balance of the dataset:Figure 6: Bar chart showing the distribution of Spam vs. Legitimate emails.Insight: The dataset is well-balanced, which ensures that the model learns to identify both classes effectively without bias.2.6 Visualization: Confusion MatrixTo evaluate the model's accuracy in detail, I generated a graphical heatmap of the Confusion Matrix:Figure 7: Heatmap visualization of the model's prediction accuracy.Insight: The model correctly identified 347 legitimate emails and 379 spam emails, with minimal misclassifications, proving its reliability for cybersecurity applications.
