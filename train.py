# Imports
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss
import xgboost as xgb
import mlflow
import mlflow.xgboost

def main():
    # Loading iris dataset to prepare test and train
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=25)
    # enable auto logging in MLflow
    mlflow.xgboost.autolog()
    dtrain = xgb.DMatrix(X_train, label=Y_train)
    dtest = xgb.DMatrix(X_test, label=Y_test)
    with mlflow.start_run():
        # train the XGBoost model
        params = {
            "objective": "multi:softprob",
            "num_class": 3,
            "learning_rate": 0.15,
            "eval_metric": "merror",
            "seed": 42,
        }
        model = xgb.train(params, dtrain, evals=[(dtrain, "train")])
        # evaluate model
        Y_prob = model.predict(dtest)
        Y_pred = Y_prob.argmax(axis=1)
        loss = log_loss(Y_test, Y_prob)
        acc = accuracy_score(Y_test, Y_pred)
        # log metrics
        mlflow.log_metrics({"log_loss": loss, "accuracy": acc})
if __name__ == "__main__":
    main()