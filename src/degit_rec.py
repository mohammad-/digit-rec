from os import listdir
import knn
from imagep import get_array_from_image


def make_matrix(data):
    data = map(lambda x: x.strip(), data)
    single_line = ''.join(data)
    row = map(lambda x: int(x), list(single_line))
    return row


def extract_features(file):
    feature = get_array_from_image(file, width=20, height=20)
    feature = make_matrix(feature)
    return feature


def build_features(training_data_path):
    training_files = filter(lambda f: 'png' in f, listdir(training_data_path))
    feature_list = []
    label_list = []
    for training_file in training_files:
        feature = extract_features(training_data_path+'/'+training_file)
        digit = training_file.split('.')[0]
        feature_list.append(feature)
        label_list.append(digit)

    return feature_list, label_list


def main():
    # Load training data and build feature matrix
    feature_list, label_list = build_features('../training_set')

    # Load test data
    feature_matrix = extract_features('../test_set/2_1.png')
    print knn.classify_with_knn(feature_list, label_list, feature_matrix)

    feature_matrix = extract_features('../test_set/3_1.png')
    print knn.classify_with_knn(feature_list, label_list, feature_matrix)

    feature_matrix = extract_features('../test_set/4_1.png')
    print knn.classify_with_knn(feature_list, label_list, feature_matrix)

    feature_matrix = extract_features('../test_set/5_1.png')
    print knn.classify_with_knn(feature_list, label_list, feature_matrix)

    feature_matrix = extract_features('../test_set/6_1.png')
    print knn.classify_with_knn(feature_list, label_list, feature_matrix)

    feature_matrix = extract_features('../test_set/7_1.png')
    print knn.classify_with_knn(feature_list, label_list, feature_matrix)

    feature_matrix = extract_features('../test_set/8_1.png')
    print knn.classify_with_knn(feature_list, label_list, feature_matrix)

    feature_matrix = extract_features('../test_set/9_1.png')
    print knn.classify_with_knn(feature_list, label_list, feature_matrix)


if __name__ == '__main__':
    main()