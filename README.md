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


