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

# go to demand mode
netedit.supermodeDemand()

# force save additionals
netedit.forceSaveAdditionals()

# go to person mode
netedit.personMode()

# change Container
netedit.changeElement("personFlow")

# change person plan
netedit.changePersonPlan("walk: edge->busStop", True)

# set invalid arrival pos
netedit.changeDefaultValue(netedit.attrs.personFlow.create.terminate, "dummyTerminate")

# try to create flow with embedded route
netedit.leftClick(referencePosition, 274, 400)
netedit.leftClick(referencePosition, 270, 43)

# press enter to create flow with embedded route
netedit.typeEnter()

# set invalid arrival pos
netedit.changeDefaultValue(netedit.attrs.personFlow.create.terminate, "end-number")

# press enter to create flow with embedded route
netedit.typeEnter()

# set valid arrival pos
netedit.changeDefaultValue(netedit.attrs.personFlow.create.end, "dummy")

# create flow with embedded route
netedit.leftClick(referencePosition, 274, 400)
netedit.leftClick(referencePosition, 270, 43)

# press enter to create flow with embedded route
netedit.typeEnter()

# set valid arrival pos
netedit.changeDefaultValue(netedit.attrs.personFlow.create.end, "-30")

# press enter to create flow with embedded route
netedit.typeEnter()

# set valid arrival pos
netedit.changeDefaultValue(netedit.attrs.personFlow.create.end, "20.5")

# create flow with embedded route
netedit.leftClick(referencePosition, 274, 400)
netedit.leftClick(referencePosition, 270, 43)

# press enter to create flow with embedded route
netedit.typeEnter()

# set valid arrival pos
netedit.changeDefaultValue(netedit.attrs.personFlow.create.number, "dummy")

# create flow with embedded route
netedit.leftClick(referencePosition, 274, 400)
netedit.leftClick(referencePosition, 270, 43)

# press enter to create flow with embedded route
netedit.typeEnter()

# set valid arrival pos
netedit.changeDefaultValue(netedit.attrs.personFlow.create.number, "-30")

# press enter to create flow with embedded route
netedit.typeEnter()

# set valid arrival pos
netedit.changeDefaultValue(netedit.attrs.personFlow.create.number, "20.5")

# create flow with embedded route
netedit.leftClick(referencePosition, 274, 400)
netedit.leftClick(referencePosition, 270, 43)

# press enter to create flow with embedded route
netedit.typeEnter()

# set valid arrival pos
netedit.changeDefaultValue(netedit.attrs.personFlow.create.number, "51")

# create flow with embedded route
netedit.leftClick(referencePosition, 274, 400)
netedit.leftClick(referencePosition, 270, 43)

# press enter to create flow with embedded route
netedit.typeEnter()

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
