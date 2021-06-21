"""
Author: Sandro Dinklang

Netflix movies
"""
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Make sure everything is displayed
    pd.set_option('display.max_rows', None)

    # Read from CSV file
    netflix_data = pd.read_csv("Netflix_Dataset_Movie.csv")

    # value_counts(): reads the number of movies analyzed for each year
    data = netflix_data["Year"].value_counts()
    data = data.rename_axis('Year').reset_index(name='Count') # Formatting

    # Display
    print("Year and number of movies analyzed for that year on the "
    + "'Netflix prize open competition'")
    print(data.to_string(index=False))

    user_input = input("Press enter to continue")

    # Second question: Graph for Year and Count
    data.to_csv("data", index=False)

    graph_data = pd.read_csv("data")
    graph_data.plot(subplots=True, figsize=(6, 6))
    plt.show()

    user_input = input("Press enter to continue")
    plt.close("all")

    # Third question: X vs Y
    graph_data = graph_data.sort_values(by=["Year"])
    graph_data.plot(x="Year", y="Count")
    plt.show()
    
if __name__ == '__main__':
    main()