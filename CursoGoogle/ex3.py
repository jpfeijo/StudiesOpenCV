from sklearn import metrics, model_selection
import tensorflow as tf
import tensorflow_datasets as tfds

def main(unused_argv):
    ds = tfds.load('iris')
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(
        ds.data, ds.target, test_size=0.2, random_state=42)
    
    classifier = learn.DNNClassifier(hidden_units=[10, 20, 10], n_classes=3)

    classifier.fit(x_train, y_train, steps=200)
    score = metrics.accuracy_score(y_test, classifier.predict(x_test))
    print('Accuracy: {0.f}'.format(score))

