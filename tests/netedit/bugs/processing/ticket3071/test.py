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
# @date    2016-11-25

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

# rebuild network
netedit.rebuildNetwork()

# go to select mode
netedit.selectMode()

# select node 1
netedit.leftClick(referencePosition, 175, 220)

# select node 2
netedit.leftClick(referencePosition, 315, 220)

# select node 2
netedit.leftClick(referencePosition, 465, 220)

# join selected junctions
netedit.joinSelectedJunctions()

# rebuild network
netedit.rebuildNetwork()

# Undo joining
netedit.undo(referencePosition, 1)

# rebuild network
netedit.rebuildNetwork()

# go to select mode
netedit.selectMode()

# unselect node 2
netedit.leftClick(referencePosition, 315, 220)

# join selected junctions
netedit.joinSelectedJunctions()

# abort joining
netedit.waitQuestion('n')

# join selected junctions
netedit.joinSelectedJunctions()

# allow joining
netedit.waitQuestion('y')

# rebuild network
netedit.rebuildNetwork()

# Undo joining
netedit.undo(referencePosition, 1)

# rebuild network
netedit.rebuildNetwork()

# redo joining
netedit.redo(referencePosition, 1)

# rebuild network
netedit.rebuildNetwork()

# save additionals
netedit.saveAdditionals(referencePosition)

# save network
netedit.saveNetwork(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
