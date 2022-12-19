from theseus.opt import Config
from theseus.base.pipeline import BasePipeline
from theseus.base.utilities.loggers import LoggerObserver
from theseus.base.utilities.loggers import LoggerObserver, FileLogger, ImageWriter
from theseus.tabular.classification.callbacks import CALLBACKS_REGISTRY
from theseus.tabular.base.preprocessors import TRANSFORM_REGISTRY

class TabularPipeline(BasePipeline):
    """docstring for Pipeline."""

    def __init__(
        self,
        opt: Config
    ):
        super(TabularPipeline, self).__init__(opt)
        self.opt = opt

    def init_registry(self):
        super().init_registry()
        self.callbacks_registry = CALLBACKS_REGISTRY
        self.transform_registry = TRANSFORM_REGISTRY
        self.logger.text(
            "Overidding registry in pipeline...", LoggerObserver.INFO
        )
