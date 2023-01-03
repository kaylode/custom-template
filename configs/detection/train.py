import matplotlib as mpl

mpl.use("Agg")
from theseus.cv.detection.pipeline import Pipeline
from theseus.opt import Opts

if __name__ == "__main__":
    opts = Opts().parse_args()
    train_pipeline = Pipeline(opts)
    train_pipeline.fit()
