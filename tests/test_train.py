from src.train import train_and_evaluate


def test_model_accuracy_is_acceptable():
    accuracy = train_and_evaluate(random_state=42)

    assert accuracy >= 0.90, f"Model accuracy too low: {accuracy:.3f}"
