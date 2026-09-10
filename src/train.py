"""Deterministic model training used by the ML CI quality gate."""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_and_evaluate(random_state=42):
    """Train an Iris classifier and return its holdout-set accuracy."""
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data,
        data.target,
        test_size=0.25,
        random_state=random_state,
        stratify=data.target,
    )

    model = LogisticRegression(max_iter=300)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    return accuracy_score(y_test, predictions)


if __name__ == "__main__":
    accuracy = train_and_evaluate()
    print(f"accuracy={accuracy:.4f}")
