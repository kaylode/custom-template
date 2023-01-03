import matplotlib.pyplot as plt

from theseus.base.utilities.analyzer import Analyzer
from theseus.base.utilities.loggers import LoggerObserver
from theseus.tabular.base.utilities.pprint import pretty_print_df

LOGGER = LoggerObserver.getLogger("main")


def check_nan(df):
    missing = df.isna().mean() * 100
    return missing.sort_values(ascending=False, inplace=False)


def check_duplicate(df):
    num_duplicates = df.duplicated().sum()
    LOGGER.text(
        f"Number of duplicate rows: {num_duplicates}",
        level=LoggerObserver.INFO,
    )


class DataFrameAnalyzer(Analyzer):
    def __init__(self, **kwargs):
        super().__init__()

    def init_dict(self):
        self.instance_dict["id"] = []
        self.instance_dict["class"] = []

    def update_item(self, item):
        label = item["target"]["labels"][0]
        self.instance_dict["id"].append(len(self.instance_dict["id"]) + 1)
        self.instance_dict["class"].append(label)

    def analyze(self, figsize=(8, 8)):
        # missing_df = check_nan(df)
        # pretty_print_df(missing_df)
        # check_duplicate(df)
        fig, axs = plt.subplots(1, 1, figsize=figsize)
        self.class_dist(axs)
        return fig