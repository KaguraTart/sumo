#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2008-2023 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    runner.py
# @author  Robert Hilbrich
# @date    2019-11-10

from __future__ import absolute_import
from __future__ import print_function

import os
import subprocess
import sys
toolDir = os.path.join(
    os.path.dirname(__file__), '..', '..', '..', '..', "tools")
sys.path.append(toolDir)
import sumolib  # noqa

sumoBinary = sumolib.checkBinary('sumo')

# Set the example environment variable
os.environ["NETFILENAME"] = "input_net"
os.environ["HOME"] = os.path.abspath(os.curdir)

# write config
subprocess.call([sumoBinary, "-c", "sumo.sumocfg", "--no-step-log", "-C", "config.sumocfg",
                 "--collision-output", "~/collision.xml",
                 "--tripinfo", "${PID}.trips.xml", "--summary", "sum${UTC}.xml", "--log", "log${LOCALTIME}.log"])

# file output direct
subprocess.call([sumoBinary, "-c", "config.sumocfg"])

files = list(sorted(os.listdir()))
print("uncheck:", files, os.curdir)
assert(files[0].endswith(".trips.xml"))
assert(int(files[0][:-10]) > 0)
assert("collision.xml" in files)
assert(len(files) == 11)
