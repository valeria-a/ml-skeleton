import numpy as np
import pandas as pd


class DataLoader:

    def load_local_csv(self, local_file):
        # here add some logic that loads the data (from local file / cloud storage / url / etc)
        # inheritance can be handy here
        df = pd.DataFrame(np.random.randn(152, 18)) # lets say it was loaded from local csv
        print(f"Loaded data from {local_file}")

        return df

    def load_from_url(self, url, target_path=None):
        # reload data from the internet and store it locally
        df = pd.DataFrame(np.random.randn(50, 7)) # simulating data loading
        if target_path:
            # store data in target_path after loading
            pass

        print(f"DataLoader: Loaded data from {url} and stored it to {target_path}")
        return df

