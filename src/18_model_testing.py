import click
import pandas as pd
import os
import pickle

from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.metrics import accuracy_score

from great_tables import GT

@click.command()
@click.option(
    "--x-test",
    default="src/objects/X_test.csv",
    help="Feature test dataset CSV file",
)
@click.option(
    "--y-test",
    default="src/objects/y_test.csv",
    help="Response test dataset CSV file",
)
def model_testing(x_test, y_test, out_dir="results/models"):
    """This function cross validates.
        1. number of record bar chart by classes ("plot_class.png")
        2. numeric features' boxplot by classes ("plot_numeric_box.png")
        3. binary features' bar chart by classes ("plot_binary_bar.png")
        4. ordinal features' bar chart by classes ("plot_ordinal_bar.png")

    Args:
        test_file (string): the path to the test data set Defaults to "objects/test_df.csv".
        out_dir (str, optional): the folder to save the plots. Defaults to "../results/figures".
    """

    # ============================ read in test data
    X_test = pd.read_csv(x_test)
    y_test = pd.read_csv(y_test)

    # ============================ read in models
    with open(os.path.join(out_dir, "trained_lr_pipe.pkl"), "rb") as f:
        lr_pipe = pickle.load(f)

    with open(os.path.join(out_dir, "trained_linear_svc_pipe.pkl"), "rb") as f:
        linear_svc_pipe = pickle.load(f)

    # ============================ Test Models
    prediction_lr = lr_pipe.predict(X_test)
    accuracy_lr = accuracy_score(y_test, prediction_lr)

    prediction_svc = linear_svc_pipe.predict(X_test)
    accuracy_svc = accuracy_score(y_test, prediction_svc)

    # ============================ Make table
    test_results = {"Logistic Regression": accuracy_lr, "Linear SVC": accuracy_svc}

    test_results = pd.DataFrame([test_results], index=['Accuracy'])

    # ============================ Export Great Table
    great_table2 = (
        GT(test_results.rename(columns={"index": "Metric"}))
        .tab_header(
            title="Accuracy Score on Test Set for Candidate Models"
        )
        .fmt_number(columns=["Logistic Regression", "Linear SVC"], decimals=4)
        .opt_stylize(style=3, color="blue")
    )

    great_table2.save(os.path.join(out_dir, "model_testing"), scale=2)

    # ============================ Export Models

    click.echo("Models tested")

if __name__ == "__main__":
    model_testing()
