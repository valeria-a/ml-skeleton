class FeatureExtractor:
    def __init__(self, data):
        self.data = data

    def extract_features(self, features_list):
        # work on data to extract needed features
        if 'feature1' in features_list:
            self._extract_feature1()
        if 'feature2' in features_list:
            self._extract_feature2()
        print(f"FeatureExtractor: extracted features {features_list}")

    def _extract_feature1(self):
        # do some stuff to get feature1
        print(f"FeatureExtractor: extracted feature 1")

    def _extract_feature2(self):
        # do some stuff to get feature2
        print(f"FeatureExtractor: extracted feature 2")
