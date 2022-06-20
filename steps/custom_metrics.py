from typing import Dict

import pandas as pd
from sklearn.metrics import mean_squared_error


def weighted_mean_squared_error(
    eval_df: pd.DataFrame, builtin_metrics: Dict[str, int]
) -> Dict[str, int]:  # pylint: disable=unused-argument
    """
    Computes the weighted mean squared error (MSE) metric.

    :param eval_df: A Pandas DataFrame containing the following columns:

                    - ``"prediction"``: Predictions produced by submitting input data to the model.
                    - ``"target"``: Ground truth values corresponding to the input data.

    :param builtin_metrics: A dictionary containing the built-in metrics that are calculated
                            automatically during model evaluation. The keys are the names of the
                            metrics and the values are the scalar values of the metrics. For more
                            information, see
                            https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.evaluate.
    :return: A single-entry dictionary containing the MSE metric. The key is the metric names and
             the value is the scalar metric value. Note that custom metric functions can return
             dictionaries with multiple metric entries as well.
    """
    return {
        "weighted_mean_squared_error": mean_squared_error(
            eval_df["prediction"],
            eval_df["target"],
            sample_weight=1 / eval_df["prediction"].values,
        )
    }
