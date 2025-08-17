#!/usr/bin/env python3
"""

See EOF for license/metadata/notes as applicable
"""

##-- builtin imports
from __future__ import annotations

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
from typing import (TYPE_CHECKING, Any, Callable, ClassVar, Final, Generic,
                    Iterable, Iterator, Mapping, Match, MutableMapping,
                    Protocol, Sequence, Tuple, TypeAlias, TypeGuard, TypeVar,
                    cast, final, overload, runtime_checkable, Generator)
from uuid import UUID, uuid1

##-- end builtin imports

import sys

import doot
import doot.errors
from doot.workflow import ActionSpec, DootTask
from doot.util.dkey import DootKeyed as DKeyed

##-- logging
logging = logmod.getLogger(__name__)
##-- end logging

@DKeyed.args
@DKeyed.redirects("update_")
def simple(spec, state, _args, _update) -> None:
    doot.report.wf.act(info="", msg="This is a simple custom action", level=logmod.WARNING)

@DKeyed.args
@DKeyed.redirects("update_")
def with_args(spec, state, _args, _update) -> None:
    doot.report.wf.act(info="", msg="This is a custom action with args:", level=logmod.WARNING)
    for i,arg in enumerate(_args):
        doot.report.wf.act(info="", msg=f"Arg {i}: {arg}", level=logmod.WARNING)
