class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def perform_full_analysis(self, target_path):
        self.perform_distribution_analysis(target_path)
        self.perform_distribution_analysis(target_path)
        print(f"DataAnalyzer: performed full analysis")

    def perform_correlation_analysis(self, target_path):
        # do some stuff here, work on correlations etc
        # maybe store results to a file
        print(f"DataAnalyzer: performed correlation analysis")

    def perform_distribution_analysis(self, target_path):
        # work on distributions etc
        # maybe store graphs to a file
        print(f"DataAnalyzer: performed distribution analysis")
