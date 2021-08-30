class DataProcessor:

    def __init__(self, df):
        self.df = df

    def process_data_for_analysis(self):
        self.clean_data()
        self.fill_missing()

    def process_data_for_model(self):
        self.process_data_for_analysis()
        self.normalize()

    def clean_data(self):
        # code that looks for bad values in data and cleans them out
        print(f"DataProcessor: Data cleaned")

    def fill_missing(self):
        # code that fills up missing values in the data
        print(f"DataProcessor: Filled up missing values")

    def normalize(self):
        # code that normalizes data (z-score, maybe turning string categories to numbers, etc...)
        print(f"DataProcessor: Normalized data")
