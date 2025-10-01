# Customer Purchasing Behavior Analysis

## Data Preparation

In this project, we built a structured dataset to analyze customer purchasing behavior.  
The preprocessing steps included:

- **Dataset creation**: Defined the dependent variable (**Total Price**) and nine independent variables including continuous, categorical, and binary features (at least one of each type).  
- **Filtering**: Removed rows with `"cancelled"` values in the `Order status` column, which represent transactions that were not completed. After filtering, the dataset contained **13,432 rows**.  
- **Handling missing values**: Removed rows containing missing data (as required for this assignment).  
- **Data transformation**: Converted textual values into numerical representations.  
- **Sampling**: Selected **10,000 records** using the `RAND` method in Excel to ensure a representative dataset.

## Variables Summary

The following table summarizes all variables in the dataset, their types, ranges, and additional notes.  
For continuous and categorical variables, distribution plots are included (where applicable).
<img width="964" height="966" alt="image" src="https://github.com/user-attachments/assets/cec2d979-d54e-4033-9105-01ebafd7c1f3" />

## Correlation Analysis

In this step, we analyzed the relationships between the variables in our dataset.  

- For each independent variable (**xᵢ**) we examined its relationship with the dependent variable (**y = Total Price**).  
- For each pair of independent variables (**xᵢ, xⱼ**, where *i ≠ j*) we examined their relationships with each other.  
- Finally, we generated a **correlation heatmap** to visualize the overall relationships among all variables.  

### Variables analyzed:
- **Age** (independent)  
- **Rating** (independent)  
- **Quantity** (independent)  
- **Total Price** (dependent)  

The analysis allowed us to identify which independent variables are strongly correlated with **Total Price**, as well as potential relationships among **Age**, **Rating**, and **Quantity**.  
This step also served to check for possible **multicollinearity** issues in the dataset.  
<img width="1189" height="364" alt="image" src="https://github.com/user-attachments/assets/8cc824aa-8649-4501-a68e-b71e08165754" />
<img width="771" height="373" alt="image" src="https://github.com/user-attachments/assets/1399f043-88d4-458c-a1ea-ef8918827570" />

## Multicollinearity in The Data:
Multicollinearity refers to the correlation between the explanatory variables in a model. The phenomenon occurs when there is a relationship between the explanatory variables and this relationship causes bias during the analysis. This phenomenon can cause the dependent variable to be overestimated and result in an incorrect prediction. Sometimes it is chosen to omit one of the related variables in order not to cause an incorrect prediction.
Based on the Pearson correlation table, it can be seen that there is no relationship between the independent variables and therefore there is no concern for multicollinearity.

## Independent Variables Predicting the Dependent Variable

Based on the Pearson correlation table, the only independent variable that can effectively predict the dependent variable, **Total Price**, is **Quantity**. 
The reason for this is that **Quantity** is the only independent variable that shows a strong positive linear relationship with the dependent variable, with a Pearson correlation coefficient of **0.651**. This indicates that as the quantity of items increases, the total price tends to increase proportionally. 
Other independent variables, such as **Age** and **Rating**, do not show a significant linear correlation with **Total Price**, which implies that they are less effective as predictors for this dependent variable in a linear regression model.

## Preliminary Insights and Hypotheses

1. **Insight 1:** As the **Quantity** increases, we expect the **Total Price** to increase as well. This indicates a strong positive relationship between the number of items purchased and the total amount spent.

2. **Insight 2:** There is no apparent relationship between the customer's **Age** and the **Total Price**. This suggests that age does not significantly influence the total amount spent in this dataset.

3. **Hypothesis:** The **Purchase Date** variable may influence the number of transactions. During weekdays, there are more working days compared to weekends (Friday, Saturday, and Sunday), and customers are likely to make more online purchases during working hours. Therefore, we expect a higher number of transactions on weekdays compared to weekends.

### Hypothesis testing:
<img width="1012" height="225" alt="image" src="https://github.com/user-attachments/assets/4457e25a-bcf7-44f2-8b15-49775d65709d" />

## Checking Normality of the Target Variable

The target variable (**Total Price**) initially follows a **log-normal (LN) distribution**, which means it is not normally distributed. Since the dependent variable in many statistical analyses and modeling techniques is expected to follow a normal distribution, we applied the following corrections:
1. **Log Transformation:** We applied a natural logarithm (LN) transformation to the target variable to reduce skewness and bring the distribution closer to normality.  
2. **Removing Left Tail Outliers:** We also removed extreme values from the left tail of the distribution to further improve normality.

These adjustments helped in obtaining a more normally distributed target variable, suitable for further analysis and modeling.
<img width="1238" height="717" alt="image" src="https://github.com/user-attachments/assets/b98861e0-8f10-46b8-b12e-0309a13319a5" />

## Reducing Categories for Categorical Variables

For categorical variables, it is important to reduce the number of categories to 3-5 values to simplify analysis and improve interpretability. We performed the following steps in detail:

1. ### Payment Method:  
   The original **Payment Method** column contained 5 categories. We reduced it to 4 categories using a **Pivot Table**. Specifically, we merged the **Paypal** and **Credit Card** categories because their average transaction amounts (the dependent variable) were nearly identical. This can be observed in the accompanying graph.

**Before reduction:**

<img width="669" height="186" alt="image" src="https://github.com/user-attachments/assets/d7753d14-4f2d-4cb3-9bd5-a1c3415837ca" />
<img width="804" height="462" alt="image" src="https://github.com/user-attachments/assets/c2cd5443-79f0-4a97-94f4-03b6e56453b8" />
**After reduction:**

<img width="557" height="186" alt="image" src="https://github.com/user-attachments/assets/6f8782ce-d60e-4e19-b453-db86f46a0c09" />
<img width="898" height="425" alt="image" src="https://github.com/user-attachments/assets/c976f453-8071-4093-ba7b-74165e22d734" />



2. ### Product Type:  
   The original **Product Type** column contained 5 categories. We reduced it to 3 categories using a **Pivot Table**. In this case, we merged **Tablet**, **Laptop**, and **Smartwatch** into a single category, as their average transaction amounts (the dependent variable) were very similar. This consolidation is also illustrated in the attached graph.

**Before reduction:**

<img width="536" height="175" alt="image" src="https://github.com/user-attachments/assets/7ac1edff-22cc-4a92-8fdd-41ceda8ae2da" />
<img width="810" height="501" alt="image" src="https://github.com/user-attachments/assets/ff67d187-9ec4-4846-82c1-a946449e02f1" />
**After reduction:**

<img width="526" height="142" alt="image" src="https://github.com/user-attachments/assets/f1e3a9c1-946a-484a-9666-5eb95e95439d" />
<img width="959" height="456" alt="image" src="https://github.com/user-attachments/assets/b21f8b4f-fa20-4ed7-86ac-0cb53e1dd5c8" />

## Verifying the Changes in the Dataset

To ensure that the changes we applied to the dataset worked correctly, we performed a **sanity check** as follows:

1. **Payment Method:**  
   We filtered the **Payment Method** column for each individual value and compared the average transaction amount obtained in the Pivot Table with the average from the full Excel dataset. The averages matched, confirming that the merger of **Paypal** and **Credit Card** into a single category was done correctly.

2. **Product Type:**  
   We filtered the **Product Type** column for each individual value and compared the average transaction amount obtained in the Pivot Table with the average from the full Excel dataset. Again, the averages matched, confirming that the merger of **Tablet**, **Laptop**, and **Smartwatch** into a single category was performed correctly.

## Hypothesis Testing for a Categorical Variable

We chose the categorical variable **Rating** and performed **T-Tests** on the target variable **LN(Total Price)**, which is normally distributed, to examine whether there are significant differences between the different rating groups.

**Hypotheses:**

- \(H_0\): There is no difference in the mean LN(Total Price) between the rating groups.  
- \(H_1\): There is a difference in the mean LN(Total Price) between the rating groups.

| Rating Comparison | 1-2   | 1-3 | 1-4 | 1-5 | 2-3 | 2-4 | 2-5 | 3-4 | 3-5 | 4-5 |
|------------------|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| P-Value          | 0.0078 | 0   | 0.92 | 0.29 | 0   | 0.009 | 0.15 | 0   | 0   | 0.32 |

**Conclusion:**  

Using a significance level of \( \alpha = 0.05 \):

- If \( p < 0.05 \), we reject \(H_0\) and conclude that there is a significant difference between the group means.  
- If \( p \geq 0.05 \), we fail to reject \(H_0\) and conclude that there is no significant difference between the group means.

**Results:**

- 1-2: Reject \(H_0\), significant difference  
- 1-3: Reject \(H_0\), significant difference  
- 1-4: Fail to reject \(H_0\), no significant difference  
- 1-5: Fail to reject \(H_0\), no significant difference  
- 2-3: Reject \(H_0\), significant difference  
- 2-4: Reject \(H_0\), significant difference  
- 2-5: Fail to reject \(H_0\), no significant difference  
- 3-4: Reject \(H_0\), significant difference  
- 3-5: Reject \(H_0\), significant difference  
- 4-5: Fail to reject \(H_0\), no significant difference

### Hypothesis test results:
<img width="2000" height="940" alt="image" src="https://github.com/user-attachments/assets/ecba333a-66f3-4c76-a5f4-f67aa54bbd06" />

## Linear Regression with the Purchase Date Variable

To include the **Purchase Date** variable in a linear regression model, we created a **binary variable (`Weekend`)** based on the purchase date:

- `1` indicates a purchase made during the weekend (**Friday, Saturday, Sunday**)  
- `0` indicates a purchase made during weekdays (**Monday to Thursday**)  

Additionally, all categorical variables were encoded using **dummy variables**.

**First Run of Multiple Linear Regression:**  
<img width="791" height="532" alt="image" src="https://github.com/user-attachments/assets/5c6db163-8391-4665-bd71-5f6eee249a70" />

From the first run, we observed that some variables had **p-values greater than 0.05**, indicating they are not statistically significant. Therefore, we removed these variables from the model and re-ran the regression.

**Updated Multiple Linear Regression Model:**  
<img width="966" height="468" alt="image" src="https://github.com/user-attachments/assets/810f34c8-4df7-410d-b819-a75c94016685" />

** The variables are significant in regression according to PV<0.05: **
The variables that remained significant (**p-value < 0.05**) in the final regression are as follows:

| Variable | P-Value | Coefficient (β_i) |
|----------|---------|------------------|
| Intercept (Age, Gender, Loyalty Member, Weekend, Rating 1, Rating 4, Rating 5, Product Type 1, Payment Method 1, Payment Method 2) | 0 | β_0 = 6.297 |
| Quantity | 0 | β_1 = 0.195 |
| Product Type 2 | 0 | β_2 = 0.471 |
| Product Type 3 | 0 | β_3 = 0.955 |
| Rating 2 | 0 | β_4 = -0.111 |
| Rating 3 | 0 | β_5 = -0.115 |
| Payment Method 3 | 0 | β_6 = 0.143 |
| Payment Method 4 | 0 | β_7 = 0.217 |

** Regression Equation:**
The regression equation for the log-transformed dependent variable **LN(Total Price)** is:
\[
LN(Y) = 6.297 + 0.195X_1 + 0.471X_2 + 0.955X_3 - 0.111X_4 - 0.115X_5 + 0.143X_6 + 0.217X_7
\]

Where:
- \(X_1\) = Quantity  
- \(X_2, X_3\) = Product Type dummies  
- \(X_4, X_5\) = Rating dummies  
- \(X_6, X_7\) = Payment Method dummies  

To obtain the predicted **Total Price**, we apply the exponential transformation:
\[
Y = e^{6.297 + 0.195X_1 + 0.471X_2 + 0.955X_3 - 0.111X_4 - 0.115X_5 + 0.143X_6 + 0.217X_7}
\]

## Normal distribution:
Based on the graph, the errors of the regression model are normally distributed
<img width="1069" height="548" alt="image" src="https://github.com/user-attachments/assets/a5465ffd-da2f-4194-b142-bb0d3ed598e9" />

## Model Fit and Multicollinearity Check
The regression model fits the data well:
- The range of the actual dependent variable (**Total Price**) is **[786.41, 11396.8]**  
- The range of predicted values from the model is **[588.16, 12320.256]**  
There is no indication of **overfitting**, as the model achieved an **R² = 0.732**, which suggests a good fit while maintaining generalizability.

### Multicollinearity Check
We tested for multicollinearity using the **Variance Inflation Factor (VIF)**:

VIF = \frac{1}{1 - R^2} = \frac{1}{1 - 0.732} = 3.731

Since the VIF value is **less than 6**, there is no concern about multicollinearity among the independent variables.

