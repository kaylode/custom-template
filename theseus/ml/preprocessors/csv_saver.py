from theseus.base.utilities.loggers.observer import LoggerObserver

from .base import Preprocessor

LOGGER = LoggerObserver.getLogger("main")


class CSVSaver(Preprocessor):
    def __init__(self, out_path, **kwargs):
        super().__init__(**kwargs)
        self.out_path = out_path

    def run(self, df):
        df.to_csv(self.out_path, index=False)
        self.log(f"Saved to {self.out_path}")
        return df
