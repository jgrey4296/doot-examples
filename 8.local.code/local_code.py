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
import os

import doot
import doot.errors
from doot.workflow import ActionSpec, DootTask
from doot.util.dkey import DootKeyed as DKeyed

##-- logging
logging = logmod.getLogger(__name__)
##-- end logging

env = os.environ

@DKeyed.redirects("update_")
def simple(spec, state, _update):
    logging.user("Running simple external action")

class SimpleTaskExample(DootTask):
    """
      A Simple example task that uses a mixin, and adds its own default actions
    """

    def __init__(self, spec, *, job=None, action_ctor=None, **kwargs):
        super().__init__(spec, job=job, **kwargs)
        self._extra_actions = []
        self._extra_actions.append(ActionSpec(fun=self._head))
        self._extra_actions.append(ActionSpec(fun=self._tail))

    @property
    def actions(self):
        """ yield spec actions, plus a head and tail """
        yield self._extra_actions[0]
        yield from iter(self.spec.actions)
        yield self._extra_actions[1]

    def _head(self, spec, state):
        logging.user("A Big number: %s", 1_000_000)

    def _tail(self, spec, state):
        logging.user("Another Big Number: %s", 50_234_235)
