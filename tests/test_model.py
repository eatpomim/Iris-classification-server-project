import pytest

@pytest.fixture
def sample():
    return Sample(5.1, 3.5, 1.4, 0.2)

@pytest.fixture
def known_sample():
    return KnownSample(5.1, 3.5, 1.4, 0.2, "setosa")

@pytest.fixture
def testing_known_sample(known_sample):
    return TestingKnownSample(known_sample, "setosa")

@pytest.fixture
def training_known_sample(known_sample):
    return TrainingKnownSample(known_sample)

@pytest.fixture
def hyperparameter(training_data):
    return Hyperparameter(5, Distance.EUCLIDEAN, weakref.ref(training_data))

def test_sample(sample):
    assert sample.sepal_length == 5.1
    assert sample.sepal_width == 3.5
    assert sample.petal_length == 1.4
    assert sample.petal_width == 0.2

def test_known_sample(known_sample):
    assert known_sample.sepal_length == 5.1
    assert known_sample.sepal_width == 3.5
    assert known_sample.petal_length == 1.4
    assert known_sample.petal_width == 0.2
    assert known_sample.species == "setosa"

def test_testing_known_sample(testing_known_sample):
    assert testing_known_sample.Sample.sepal_length == 5.1
    assert testing_known_sample.Sample.sepal_width == 3.5
    assert testing_known_sample.Sample.petal_length == 1.4
    assert testing_known_sample.Sample.petal_width == 0.2
    assert testing_known_sample.Sample.species == "setosa"
    assert testing_known_sample.classification == "setosa"

def test_training_known_sample(training_known_sample):
    assert training_known_sample.Sample.sepal_length == 5.1
    assert training_known_sample.Sample.sepal_width == 3.5
    assert training_known_sample.Sample.petal_length == 1.4
    assert training_known_sample.Sample.petal_width == 0.2
    assert training_known_sample.Sample.species == "setosa"

def test_hyperparameter(hyperparameter, known_sample):
    classification = hyperparameter.classify(known_sample)
    assert isinstance(classification, str)

