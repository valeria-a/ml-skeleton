import argparse

from data_processing.data_analyzer import DataAnalyzer
from data_processing.data_loader import DataLoader
from data_processing.data_processor import DataProcessor

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage my machine learning processing pipeline')

    parser.add_argument('action',
                        type=str,
                        choices=['reload_data_from_url', 'analyze_data',
                                 'train_model', 'evaluate_model', 'predict_model'],
                        help='Action to perform on the model (train/evaluate/predict)')

    parser.add_argument('--data-url',
                        type=str,
                        default=None,
                        help='url to load the data from')

    parser.add_argument('--target_path',
                        type=str,
                        default=None,
                        help='local path to store the output')

    parser.add_argument('--data-path',
                        type=str,
                        default=None,
                        help='url to load the data from')

    args = parser.parse_args()
    print('Parameters: {}'.format(args))

    if args.action == 'reload_data_from_url':
        if not args.data_url or not args.target_path:
            print('Missing arguments')
            exit(1)

        data_loader = DataLoader()
        data_loader.load_from_url(args.data_url, args.target_path)

    elif args.action == 'analyze_data':
        if not args.data_path or not args.target_path:
            print('Missing arguments')
            exit(1)

        data_loader = DataLoader()
        loaded_data = data_loader.load_local_csv(args.data_path)
        data_processor = DataProcessor(loaded_data)
        processed_data = data_processor.process_data_for_analysis()
        data_analyzer = DataAnalyzer(processed_data)
        data_analyzer.perform_full_analysis(args.target_path)
    else:
        pass
