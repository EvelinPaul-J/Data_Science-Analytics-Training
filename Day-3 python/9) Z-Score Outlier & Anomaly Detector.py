import numpy as np
def detect_outliers_zscore(values, threshold=2.0):
    values = np.array(values)
    mean = np.mean(values)
    std = np.std(values)
    z_score = abs((values - mean) / std)
    return values[z_score > threshold].tolist()
metrics = [10.0, 12.0, 12.0, 13.0, 12.0, 11.0, 14.0, 100.0, 12.0]
outliers = detect_outliers_zscore(metrics, 2.0)
print(outliers)