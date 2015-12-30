#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Starting a task, then canceling it
"""
#end_pymotw_header

import asyncio
import functools
import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
    stream=sys.stderr,
)
LOG = logging.getLogger('')


async def task_func():
    LOG.debug('in task_func')
    return 'the result'


event_loop = asyncio.get_event_loop()

LOG.debug('creating task')
task = event_loop.create_task(task_func())

LOG.debug('canceling task')
task.cancel()

try:
    LOG.debug('entering event loop')
    event_loop.run_until_complete(task)
    LOG.debug('task: %r' % (task,))
except asyncio.CancelledError:
    LOG.debug('caught error from canceled task')
else:
    LOG.debug('task result: %r' % (task.result(),))
finally:
    LOG.debug('closing event loop')
    event_loop.close()