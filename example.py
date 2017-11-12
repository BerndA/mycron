#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the MIT license.

"""

"""
from mycron import mycron

cronjob = mycron()

@cronjob(time_interval=60)
def minute():
    cronjob.logger.debug('minute job action')

@cronjob(time_interval=120)
def two_minute():
    cronjob.logger.debug('twominute job action')

@cronjob(time_interval=180)
def three_minute():
    cronjob.logger.debug('threeminute job action')

cronjob.run()
