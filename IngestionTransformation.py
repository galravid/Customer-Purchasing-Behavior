import pandas as pd
import math
from tqdm import tqdm
import warnings
import statistics
import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)

print_debug = False  #לשנות לTRUE בשביל לראות איפה הערכים חסרים


# --------------------- Ingestion Phase ------------------------------------ #

def create_overall_data_dictionary():
    overall_data = get_data_from_file()
    chack_for_non_flot(overall_data)
    complete_avg_for_missing_cont_data(overall_data)
    overall_tagged_data = tag_simulation_data(overall_data=overall_data)
    return overall_tagged_data


def get_data_from_file():
    path_string = rf"Electronic_sales_Sep2023-Sep2024.csv"
    simulation_data = pd.read_csv(path_string, encoding="ISO-8859-1")
    return simulation_data


def chack_for_non_flot(Data):
    for index in range(len(Data)):
        # בדיקה לעמודת TotalPrice (עמודה 9)
        total_price_value = Data.at[index, Data.columns[9]]
        if not isinstance(total_price_value, (int, float)):
            try:
                Data.at[index, Data.columns[9]] = float(total_price_value)
            except (ValueError, TypeError):
                Data.at[index, Data.columns[9]] = np.nan

        # בדיקה לעמודת AddOnTotal (עמודה 15)
        addon_total_value = Data.at[index, Data.columns[15]]
        if not isinstance(addon_total_value, (int, float)):
            try:
                Data.at[index, Data.columns[15]] = float(addon_total_value)
            except (ValueError, TypeError):
                Data.at[index, Data.columns[15]] = np.nan


def tag_simulation_data(overall_data):
    number = 1
    size_of_data = len(overall_data)
    overall_tagged_data = []
    rows_removed = 0

    for index, data_frame_item in tqdm(overall_data.iterrows(), total=overall_data.shape[0], desc="Loading Data",
                                       ncols=100):
        data_tuple = create_data_list(data_frame_item=data_frame_item, number=number)

        _, CustomerID, Age, Gender, LoyaltyMember, Rating, ProductType, PaymentMethod, _, Quantity, _ = data_tuple

        if not check_if_volt_nan(
                customer_id=CustomerID,
                age=Age,
                gender=Gender,
                loyalty_member=LoyaltyMember,
                product_type=ProductType,
                rating=Rating,
                payment_method=PaymentMethod,
                quantity=Quantity,
                row_number=number
        ):
            overall_tagged_data.append(data_tuple)
        else:
            rows_removed += 1

        number += 1

    removed_percent = round(100 * rows_removed / size_of_data, 2)

    print(f"\n Data Upload Completed.")
    print(f" Rows removed                 : {rows_removed}")
    print(f" Percentage removed           : {removed_percent}%\n")

    return overall_tagged_data


# --------------------- Transformation Phase ------------------------------------ #

def create_data_list(data_frame_item, number):
    number = number
    CustomerID = check_if_nan(data_frame_item[0], column_name="CustomerID", row_number=number)
    Age = check_if_nan(data_frame_item[1], column_name="Age", row_number=number)
    Gender = encode_gender(data_frame_item[2])  # {0- Female, 1- Male}
    LoyaltyMember = encode_LoyaltyMember(data_frame_item[3])  # {0- No, 1- Yes}
    ProductType = encode_ProductType(data_frame_item[4])  # {1- Headphones, 2- Tablet, 3- Smartphones, 4- Laptop,
    # 5- Smartphone}
    Rating = check_if_nan(data_frame_item[6], column_name="Rating", row_number=number)
    PaymentMethod = encode_PaymentMethod(data_frame_item[8])  # {1- Cash, 2- Debit Card, 3- PayPal, 4- Credit Card,
    # 5- Bank Transfer}
    TotalPrice = check_if_nan(data_frame_item[9])
    Quantity = check_if_nan(data_frame_item[11], column_name="Quantity", row_number=number)
    AddOnTotal = check_if_nan(data_frame_item[15])

    data_list = [number, CustomerID, Age, Gender, LoyaltyMember, Rating, ProductType, PaymentMethod, TotalPrice,
                 Quantity, AddOnTotal]

    return data_list


# --------------------- Transformation Phase - Tagging Data Methods --------------------------- #

def encode_gender(gender_value):
    if isinstance(gender_value, str):
        gender_value = gender_value.strip().lower()

        if gender_value == "male":
            return 1
        elif gender_value == "female":
            return 0

    return np.nan


def encode_LoyaltyMember(value):
    if isinstance(value, str):
        value = value.strip().lower()

        if value == "yes":
            return 1
        elif value == "no":
            return 0

    return np.nan


def encode_ProductType(value):
    if isinstance(value, str):
        value = value.strip().lower()

        if value == "headphones":
            return 1
        elif value == "tablet":
            return 2
        elif value == "smartphone":
            return 3
        elif value == "laptop":
            return 4
        elif value == "smartwatch":
            return 5

    return np.nan


def encode_PaymentMethod(value):
    if isinstance(value, str):
        value = value.strip().lower()

        if value == "cash":
            return 1
        elif value == "debit card":
            return 2
        elif value == "paypal":
            return 3
        elif value == "credit card":
            return 4
        elif value == "bank transfer":
            return 5
    return np.nan


def complete_avg_for_missing_cont_data(data):
    # חישוב ממוצע TotalPrice (עמודה 9)
    total_price_values = [row[9] for row in data.itertuples(index=False) if not math.isnan(row[9])]
    avg_total_price = statistics.mean(total_price_values)

    # חישוב ממוצע AddOnTotal (עמודה 15)
    addon_total_values = [row[15] for row in data.itertuples(index=False) if not math.isnan(row[15])]
    avg_addon_total = statistics.mean(addon_total_values)

    # עדכון הערכים החסרים
    for index in range(len(data)):
        row_number = index + 1

        if math.isnan(data.at[index, data.columns[9]]):  # TotalPrice
            print(f"Row {row_number} missing TotalPrice")
            data.at[index, data.columns[9]] = avg_total_price

        if math.isnan(data.at[index, data.columns[15]]):  # AddOnTotal
            print(f"Row {row_number} missing AddOnTotal")
            data.at[index, data.columns[15]] = avg_addon_total


# --------------------- Transformation Phase - Supporting Methods --------------------------- #

def check_if_volt_nan(customer_id, age, gender, loyalty_member, product_type, rating,
                      payment_method, quantity, row_number=None):
    if (math.isnan(customer_id)
            or math.isnan(age)
            or pd.isna(gender)
            or pd.isna(loyalty_member)
            or pd.isna(product_type)
            or math.isnan(rating)
            or pd.isna(payment_method)
            or math.isnan(quantity)):
        if math.isnan(customer_id):
            print(f"Row {row_number} missing CustomerID")
        if math.isnan(age):
            print(f"Row {row_number} missing Age")
        if pd.isna(gender):
            print(f"Row {row_number} missing Gender")
        if pd.isna(loyalty_member):
            print(f"Row {row_number} missing LoyaltyMember")
        if pd.isna(product_type):
            print(f"Row {row_number} missing ProductType")
        if math.isnan(rating):
            print(f"Row {row_number} missing Rating")
        if pd.isna(payment_method):
            print(f"Row {row_number} missing PaymentMethod")
        if math.isnan(quantity):
            print(f"Row {row_number} missing Quantity")
        return True  # יש להסיר את השורה
    return False  # השורה תקינה


def check_if_nan(data_frame_item, column_name=None, row_number=None):
    if isinstance(data_frame_item, str):
        try:
            return float(data_frame_item)
        except ValueError:
            if print_debug and column_name is not None and row_number is not None:
                print(
                    f"Error in data in row {row_number} in '{column_name}': unexpected string value '{data_frame_item}'")
            return np.nan
    if pd.isna(data_frame_item) or math.isnan(data_frame_item):
        return np.nan
    return data_frame_item


def check_for_nan_in_ready_data(data):
    for data_list in data:

        for item in data_list:

            if math.isnan(item):
                print("Bug - Problem in data")

    print("QA Test Completed - No Problem in data was identified.")


# --------------------- Prepare Data --------------------------- #

def create_training_and_validation_sets(data, ratio):
    training_set = []
    validation_set = []
    size_of_data = len(data)

    for data_list in data:

        current_ratio = data_list[0] / size_of_data

        if current_ratio <= ratio:

            training_set.append(data_list)

        else:

            validation_set.append(data_list)

    return training_set, validation_set


# --------------------- Main --------------------------- #

data = create_overall_data_dictionary()
check_for_nan_in_ready_data(data)
print("All Finished")

training_set, validation_set = create_training_and_validation_sets(data=data, ratio=0.8)

