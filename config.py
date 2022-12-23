#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "3635a0dc-fc77-4b50-a491-63b8d083c99d")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "BOn8Q~PcB~zX5pT1pmS-tt4p~W31pQT54MQHIa.p")
