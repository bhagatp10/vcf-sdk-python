#!/usr/bin/env python

# Copyright (c) 2023-2026 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.
# The term "Broadcom" refers to Broadcom Inc.
# SPDX-License-Identifier: Apache-2.0

import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client_config", action="store", required=True, help="Server configuration json file")

    return parser.parse_args()
