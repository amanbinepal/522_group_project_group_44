import click
import pandas as pd
import os
import pickle

from sklearn.model_selection import cross_validate
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from great_tables import GT


@click.command()
@click.option(
    "--x-train",
    default="src/objects/X_train.csv",
    help="Feature Training dataset CSV file",
)
@click.option(
    "--y-train",
    default="src/objects/y_train.csv",
    help="Response Training dataset CSV file",
)
def model_training(x_train, y_train, out_dir="results/models"):
    """This function cross validates.
        1. number of record bar chart by classes ("plot_class.png")
        2. numeric features' boxplot by classes ("plot_numeric_box.png")
        3. binary features' bar chart by classes ("plot_binary_bar.png")
        4. ordinal features' bar chart by classes ("plot_ordinal_bar.png")

    Args:
        train_file (string): the path to the train data set Defaults to "objects/train_df.csv".
        out_dir (str, optional): the folder to save the plots. Defaults to "../results/figures".
    """

    # ============================ read in training and test data
    X_train = pd.read_csv(x_train)
    y_train = pd.read_csv(y_train)

    # ============================ Feature processing for model
    # features
    numeric_feats = ["GenHlth", "Education", "Income", "Age", "MentHlth", "PhysHlth", "BMI"]

    passthrough_feats = [
        "HighBP",
        "HighChol",
        "CholCheck",
        "Smoker",
        "Stroke",
        "HeartDiseaseorAttack",
        "PhysActivity",
        "Fruits",
        "Veggies",
        "HvyAlcoholConsump",
        "AnyHealthcare",
        "NoDocbcCost",
        "DiffWalk",
        "Sex"
    ]

    # ============================ Column transformer

    preprocessor = make_column_transformer(
        (StandardScaler(), numeric_feats), ("passthrough", passthrough_feats)
    )

    # ============================ Dummy classifier

    dummy_df = DummyClassifier(strategy="most_frequent", random_state=552)

    scores_dummy = pd.DataFrame(
        cross_validate(dummy_df, X_train, y_train, return_train_score=True)
    ).mean()

    # ============================ Logistic regression

    lr_pipe = make_pipeline(preprocessor, LogisticRegression(max_iter=1000))

    scores_logistic = pd.DataFrame(
        cross_validate(lr_pipe, X_train, y_train, return_train_score=True)
        ).mean()

    # ============================ Linear SVC
    linear_svc_pipe = make_pipeline(preprocessor, LinearSVC(max_iter=5000))

    scores_svc = pd.DataFrame(
        cross_validate(linear_svc_pipe, X_train, y_train, return_train_score=True)).mean()

    # ============================ Summary table
    results = {
        "Dummy": scores_dummy,
        "Logistic Regression": scores_logistic,
        "Linear SVC": scores_svc
    }

    results_table = pd.DataFrame(results)

    # ============================ Export Great Table
    great_table = (
        GT(results_table.rename(columns={"index": "Metrics"}))
        .tab_header(
            title="Comparison of Candidate Models to DummyClassifier",
            subtitle="Mean Cross-Validation Scores (CV=5)",
        )
        .fmt_number(columns=["Dummy", "Logistic Regression", "Linear SVC"], decimals=4)
        .opt_stylize(style=3, color="blue")
    )

    great_table.save(os.path.join(out_dir, "model_training"), scale=2)

    # ============================ Fit Models

    lr_pipe.fit(X_train, y_train)
    linear_svc_pipe.fit(X_train, y_train)

    # ============================ Export Models

    with open(os.path.join(out_dir, "trained_lr_pipe.pkl"), 'wb') as f:
        pickle.dump(lr_pipe, f)

    with open(os.path.join(out_dir, "trained_linear_svc_pipe.pkl"), 'wb') as f:
        pickle.dump(linear_svc_pipe, f)

    click.echo("Models trained and exported")

if __name__ == "__main__":
    model_training()
