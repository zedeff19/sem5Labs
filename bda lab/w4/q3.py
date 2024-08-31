from pyspark.ml.recommendation import ALS

# Initialize the ALS model
als = ALS(
    maxIter=10, 
    regParam=0.1, 
    userCol="userId", 
    itemCol="movieId", 
    ratingCol="rating", 
    coldStartStrategy="drop"
)

# Train the model on the training data
als_model = als.fit(train_data)

# Predict on the test data
predictions = als_model.transform(test_data)

# Display predictions
predictions.show(5)
