#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the MIT license.

"""
minimal cron implementation based on python event loop
"""

import asyncio
import logging
from functools import wraps

class mycron:
    '''
    '''

    def __init__(self):
        '''
        init logging, event loop and a list of jobs
        '''
        self.cronjoblist = {}
        logging.basicConfig(filename='mycron.log', level=logging.DEBUG)
        self.logger = logging.getLogger("mycron")
        self.loop = asyncio.get_event_loop()

    def __call__(self, time_interval):
        '''
        provides decorator for cronjob functions
        '''
        def job_decorator(func):
            self.logger.debug('decorator for ' + func.__name__ + ' called')
            @wraps(func)
            def real_job(*args, **kwargs):
                self.logger.debug('calling ' + func.__name__)
                try:
                    func()
                except Exception as inst:
                    self.logger.error('during {0}'.format(func.__name__) + inst)
                    raise
                self.loop.call_at(self.loop.time() + time_interval, real_job)

            self.cronjoblist[func.__name__] = real_job
            return real_job
        return job_decorator

    def run(self):
        ''' 
        run all jobs for the first time
        and start event loop afterwards
        '''
        for f in self.cronjoblist.values():
            f()
        try:
            self.logger.debug('starting loop')
            self.loop.run_forever()
        finally:
            self.loop.close()

