from pyspark.ml.evaluation import RegressionEvaluator

# Initialize the evaluator with RMSE metric
evaluator = RegressionEvaluator(
    metricName="rmse", 
    labelCol="rating", 
    predictionCol="prediction"
)

# Evaluate the model on the test data
rmse = evaluator.evaluate(predictions)
print(f"Root-mean-square error (RMSE) = {rmse:.2f}")
