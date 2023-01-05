from theseus.base.callbacks import CALLBACKS_REGISTRY

from .explainer import *
from .logging_callbacks import MLLoggerCallbacks

CALLBACKS_REGISTRY.register(MLLoggerCallbacks)
CALLBACKS_REGISTRY.register(ShapValueExplainer)
CALLBACKS_REGISTRY.register(PermutationImportance)
CALLBACKS_REGISTRY.register(PartialDependencePlots)
CALLBACKS_REGISTRY.register(LIMEExplainer)
