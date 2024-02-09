import statistics

def analyze_data(data):
    """Perform basic data analysis."""
    mean_value = statistics.mean(data)
    median_value = statistics.median(data)
    stdev_value = statistics.stdev(data)

    print(f"Data: {data}")
    print(f"Mean: {mean_value:.2f}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {stdev_value:.2f}")

def main():
    print("Analytical Skills Example:")
    
    # Input data for analysis
    data = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11]

    # Analyze the data
    analyze_data(data)

if __name__ == "__main__":
    main()