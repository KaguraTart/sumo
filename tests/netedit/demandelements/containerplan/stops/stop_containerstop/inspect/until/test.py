#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2023 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2019-07-16

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# force save additionals
netedit.forceSaveAdditionals()

# go to demand mode
netedit.supermodeDemand()

# go to container mode
netedit.containerMode()

# change container plan
netedit.changeContainerPlan("tranship: edge->edge", False)

# create route using two one
netedit.leftClick(referencePosition, 274, 400)
netedit.leftClick(referencePosition, 280, 60)

# press enter to create route
netedit.typeEnter()

# go to containerStopContainerStop mode
netedit.containerPlanMode()

# select container
netedit.leftClick(referencePosition, 85, 412)

# go to containerStopContainerStop mode
netedit.changeContainerPlanMode("stopContainer: containerStop")

# create containerStopContainerStop
netedit.leftClick(referencePosition, 170, 40)

# press enter to create route
netedit.typeEnter()

# go to inspect mode
netedit.inspectMode()

# inspect containerStopContainerStop
netedit.leftClick(referencePosition, 119, 14)

# change depart with an invalid value
netedit.modifyBoolAttribute(netedit.attrs.containerStopContainerStop.inspect.untilEnable, False)

# change depart with an invalid value
netedit.modifyAttribute(netedit.attrs.containerStopContainerStop.inspect.until, "dummy", False)

# change depart with an invalid value
netedit.modifyAttribute(netedit.attrs.containerStopContainerStop.inspect.until, "-7.3", False)

# change depart with an invalid value
netedit.modifyAttribute(netedit.attrs.containerStopContainerStop.inspect.until, "6.7", False)

# Check undo redo
netedit.undo(referencePosition, 3)
netedit.redo(referencePosition, 3)

# save routes
netedit.saveRoutes(referencePosition)

# save additionals
netedit.saveAdditionals(referencePosition)

# save network
netedit.saveNetwork(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
