# Split the data into training (80%) and test (20%) sets
train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)

# Display counts of each dataset
print(f"Training Data Count: {train_data.count()}")
print(f"Test Data Count: {test_data.count()}")
