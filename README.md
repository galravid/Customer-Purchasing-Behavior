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

| Dependent / Independent | First Distribution | Missing Values | Range / Categories | Type                  | Representation / Description                          | Variable Name   |
|--------------------------|--------------------|----------------|--------------------|-----------------------|-------------------------------------------------------|-----------------|
| **Dependent**           | <img width="151" height="91" alt="image" src="https://github.com/user-attachments/assets/2e21747a-516d-41cf-9179-c7b4cbdd2652" />
 | No             | [20.75, 11,396.8]  | Continuous            | Total price of purchase                                | Total Price     |
| Independent             | NR                 | No             | [1, 10,000]        | Categorical           | Customer unique ID                                     | Customer ID     |
| Independent             | <img width="153" height="92" alt="image" src="https://github.com/user-attachments/assets/58e2eb83-cddf-47be-a04e-af4178c11cf4" />
 | No             | [18, 80]        | Discrete Continuous  | Customer age                                           | Age             |
| Independent             | NR                 | No             | [1,0] (1=Male, 0=Female) | Binary       | Gender of the customer                                | Gender          |
| Independent             | NR                 | No             | [1,0] (1=Yes, 0=No) | Binary              | Is the customer part of loyalty program               | Loyalty Member  |
| Independent             | <img width="181" height="108" alt="image" src="https://github.com/user-attachments/assets/eacf1b37-840d-40c6-b311-8a87a4ebe88e" />
 | No | {headphones, smartwatch, tablet, smartphone, laptop} | Categorical | Product purchased | Product Type    |
| Independent             | ![Rating Distribution](images/rating.png) | No | [1,5]          | Categorical           | Rating given by the customer                          | Rating          |
| Independent             | ![Payment Method Distribution](images/payment_method.png) | No | {cash, PayPal, credit card, debit card, bank transfer} | Categorical | Payment method used | Payment Method  |
| Independent             | ![Quantity Distribution](images/quantity.png) | No | [1,10]        | Discrete              | Number of units purchased                             | Quantity        |
| Independent             | ![Purchase Date Distribution](images/purchase_date.png) | No | Sep 2023 – Sep 2024 | Date                | Date of the purchase (YYYY-MM-DD)                     | Purchase Date   |

> **Note**: For variables marked with `NR`, no distribution chart is required. For others, include the generated plots in the `images/` folder and reference them as shown above.  
 

