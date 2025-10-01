# Customer Purchasing Behavior Analysis

## Data Preparation

In this project, we built a structured dataset to analyze customer purchasing behavior.  
The preprocessing steps included:

- **Dataset creation**: Defined the dependent variable (**Total Price**) and nine independent variables including continuous, categorical, and binary features (at least one of each type).  
- **Filtering**: Removed rows with `"cancelled"` values in the `Order status` column, which represent transactions that were not completed. After filtering, the dataset contained **13,432 rows**.  
- **Handling missing values**: Removed rows containing missing data (as required for this assignment).  
- **Data transformation**: Converted textual values into numerical representations.  
- **Sampling**: Selected **10,000 records** using the `RAND` method in Excel to ensure a representative dataset.  

