#!/usr/bin/env python3
"""


See EOF for license/metadata/notes as applicable
"""

##-- builtin imports
from __future__ import annotations

# import abc
import datetime
import enum
import functools as ftz
import itertools as itz
import logging as logmod
import pathlib as pl
import re
import time
import types
import weakref
# from copy import deepcopy
# from dataclasses import InitVar, dataclass, field
from typing import (TYPE_CHECKING, Any, Callable, ClassVar, Final, Generic,
                    Iterable, Iterator, Mapping, Match, MutableMapping,
                    Protocol, Sequence, Tuple, TypeAlias, TypeGuard, TypeVar,
                    cast, final, overload, runtime_checkable, Generator)
from uuid import UUID, uuid1

##-- end builtin imports

##-- lib imports
import more_itertools as mitz
##-- end lib imports

##-- logging
logging = logmod.getLogger(__name__)
##-- end logging

printer = logmod.getLogger("doot._printer")
from doot.task.dir_walker import _WalkControl as globc
from doot.enums import ActionResponseEnum as ActRE

def caller(spec, state):
    """
      Calls the function in the state key going from spec.kwargs.fn
      ie:
      state[spec.kwargs.fn](spec, state)
    """
    printer.info("Using: %s", spec.kwargs.fn)
    state[spec.kwargs.fn](spec, state)

def simple(spec, state):
    """
      the simplest possible local action.
    """
    printer.info("blah")

def glob_filter(target:pl.Path) -> bool | _GlobControl:
    if target.is_dir():
        return globc.noBut
    if target.stem in ["1567", "1700", "1733"]:
        return globc.yes
    return globc.no

def skip_fn(spec, state):
    pass


"""


"""
