from drl_models.dqn.embeddingchars import EmbeddingChars
from drl_models.dqn.mlp import MLP
from drl_models.dqn.sumchars import SumChars

_registry = {}


def register(ctor, name):
    _registry[name] = ctor


def construct(name, **kwargs):
    return _registry[name](**kwargs)


register(MLP, "MLP")
register(EmbeddingChars, "EmbeddingChars")
register(SumChars, "SumChars")
