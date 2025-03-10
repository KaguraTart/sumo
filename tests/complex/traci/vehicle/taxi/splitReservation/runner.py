#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
# @author  Jakob Erdmann
# @date    2017-01-23


from __future__ import print_function
from __future__ import absolute_import
import os
import sys

if "SUMO_HOME" in os.environ:
    sys.path.append(os.path.join(os.environ["SUMO_HOME"], "tools"))

import traci  # noqa
import sumolib  # noqa
import traci.constants as tc  # noqa


sumoBinary = sumolib.checkBinary('sumo')
traci.start([sumoBinary,
             "-n", "input_net4.net.xml",
             "-r", "input_routes.rou.xml",
             "--no-step-log",
             "--vehroute-output", "vehroutes.xml",
             "--tripinfo-output", "tripinfo.xml",
             "--device.taxi.dispatch-algorithm", "traci",
             ] + sys.argv[1:])


traci.simulationStep()
fleet = traci.vehicle.getTaxiFleet(0)
print("taxiFleet", fleet)
reservations = traci.person.getTaxiReservations(0)
print("reservations", reservations)
res0 = reservations[0]
res1ID = traci.person.splitTaxiReservation(res0.id, res0.persons[:2])
reservations2 = traci.person.getTaxiReservations(0)
print("reservations2", reservations2)
traci.vehicle.dispatchTaxi(fleet[0], [res0.id])
traci.vehicle.dispatchTaxi(fleet[1], [res1ID])
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

traci.close()
