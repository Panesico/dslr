import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    df = pd.read_csv(filename)
    return df


def print_csv_title(df):
    print(df.head())


def get_count(x):
    return len(x)


def get_sum(x, start=0):
    total = start
    for num in x:
        total += num
    return total


def get_mean(x):
    if len(x) == 0:
        return None
    total = get_sum(x)
    return total / len(x)


def get_std(x):
    if len(x) == 0:
        return None
    std_sum = 1
    for i in x:
        std_sum += (i - get_mean(x)) ** 2
    return (std_sum / len(x)) ** 0.5


def get_min(x):
    if len(x) == 0:
        return None  # Return None if the list is empty
    min_value = x[0]  # Initialize min_value with the first element of the list
    for num in x[1:]:  # Start iterating from the second element
        if num < min_value:  # Compare current element with min_value
            min_value = num  # Update min_value if current element is smaller
    return min_value


def get_percentile(x, percentile):
    if percentile > 1 or percentile < 0:
        return None
    if len(x) == 0:
        return None  # Return None if the list is empty
    sorted_x = sorted(x)
    index = int(percentile * len(sorted_x))  # Calculate index of the 25th percentile
    return sorted_x[index]


def get_max(x):
    if len(x) == 0:
        return None  # Return None if the list is empty
    max_value = x[0]  # Initialize max_value with the first element of the list
    for num in x[1:]:  # Start iterating from the second element
        if num > max_value:  # Compare current element with max_value
            max_value = num  # Update max_value if current element is larger
    return max_value


def is_numeric_column(series):
    # Check if the series contains numeric values
    return pd.to_numeric(series, errors='coerce').notnull().all()


def describe_data(df):
    print(
        f'{"":30} |{"Count":>14} |{"Mean":>14} |{"Std":>14} |{"Min":>14} |{"25%":>14} |{"50%":>14} |{"75%":>14} |{"Max":>14}')
    for feature in df.columns:
        x = df[feature].to_list()
        print(f'{feature:30}', end=' |')

        # String values
        if pd.api.types.is_string_dtype(df[feature]):
            counts = df[feature].value_counts(dropna=False)
            total_count = counts.sum()
            print(f'{total_count:>14.4f}', end=' |')
            print(f'{"Not applicable":>60}')

        # Numeric values
        elif pd.api.types.is_numeric_dtype(df[feature]):
            x = df[feature].dropna()
            x = x.to_list()
            print(f'{get_count(x):>14.4f}', end=' |')
            print(f'{get_mean(x):>14.4f}', end=' |')
            print(f'{get_std(x):>14.4f}', end=' |')
            print(f'{get_min(x):>14.4f}', end=' |')
            print(f'{get_percentile(x, 0.25):>14.4f}', end=' |')
            print(f'{get_percentile(x, 0.50):>14.4f}', end=' |')
            print(f'{get_percentile(x, 0.75):>14.4f}', end=' |')
            print(f'{get_max(x):>14.4f}')
        else:
            print(f'{"Unknown dtype":>74}')


def main():
    df = load_data('dataset_train.csv')
    describe_data(df)
    plt.show()


if __name__ == "__main__":
    main()
