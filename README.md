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


