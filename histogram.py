import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import utils


def display_most_homogeneous(df):
    std_devs = {}
    for feature in df.columns:
        x = df[feature].to_list()
        if pd.api.types.is_numeric_dtype(df[feature]):
            x = df[feature].dropna()
            x = x.to_list()
            std_devs[feature] = utils.get_std(x)
    min_std_dev = utils.get_min(list(std_devs.values()))
    most_homogeneous_feature = ''
    for feature, std_dev in std_devs.items():
        if std_dev == min_std_dev:
            most_homogeneous_feature = feature
            print(f'The most homogeneous feature is {feature} with a standard deviation of {std_dev}')
    distinct_houses = df['Hogwarts House'].unique()

    # Set up plot
    plt.figure(figsize=(10, 6))

    # Iterate over each distinct value
    for i in range(0, len(distinct_houses)):
        house_data = df[df['Hogwarts House'] == distinct_houses[i]]
        plt.hist(house_data[most_homogeneous_feature].dropna(), bins=30, alpha=0.5, label=distinct_houses[i], color=plt.cm.tab10(i))

    # Add title and legend
    plt.title(most_homogeneous_feature)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend(title='Hogwarts Houses', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    plt.show()



def main():
    df = utils.load_data('dataset_train.csv')
    display_most_homogeneous(df)


if __name__ == '__main__':
    main()