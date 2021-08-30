class Model:
    def __init__(self, checkpoint_path=None):
        self.checkpoint = checkpoint_path
        self.my_model = None

    def train(self, data, checkpoint=None):
        # Train on fully cleaned data ready for training
        print(f"Model: Finished training")
        pass

    def evaluate(self, data, checkpoint=None):
        # Run code that prints evaluation for the model (accuracy, scores, errors, etc)
        print(f"Model: Finished evaluating")
        pass

    def predict(self, data_to_predict):
        # load model if needed
        if not self.my_model:
            self._load_model()

        # run model prediction on received data
        print(f"Model: Ran prediction for data")

    def _load_model(self):
        # load model from the checkpoint and assign in to self.my_model
        print(f"Model loaded")
