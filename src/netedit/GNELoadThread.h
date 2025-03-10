/****************************************************************************/
// Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
// Copyright (C) 2001-2023 German Aerospace Center (DLR) and others.
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// https://www.eclipse.org/legal/epl-2.0/
// This Source Code may also be made available under the following Secondary
// Licenses when the conditions for such availability set forth in the Eclipse
// Public License 2.0 are satisfied: GNU General Public License, version 2
// or later which is available at
// https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
// SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later
/****************************************************************************/
/// @file    GNELoadThread.h
/// @author  Jakob Erdmann
/// @date    Feb 2011
///
// The thread that performs the loading of a Netedit-net (adapted from
// GUILoadThread)
/****************************************************************************/
#pragma once
#include <config.h>

#include <utils/common/MsgHandler.h>
#include <utils/foxtools/MFXSingleEventThread.h>
#include <utils/foxtools/MFXSynchQue.h>
#include <utils/foxtools/MFXInterThreadEventClient.h>


// ===========================================================================
// class declarations
// ===========================================================================
class GNENet;
class GUIEvent;
class GNEApplicationWindow;

// ===========================================================================
// class definitions
// ===========================================================================
/**
 * @class GNELoadThread
 */
class GNELoadThread : public MFXSingleEventThread {

public:
    /// @brief constructor
    GNELoadThread(GNEApplicationWindow* applicationWindow, MFXSynchQue<GUIEvent*>& eq, FXEX::MFXThreadEvent& ev);

    /// @brief destructor
    virtual ~GNELoadThread();

    /// @brief starts the thread. The thread ends after the net has been loaded
    FXint run();

    /// @brief clear files in options (used before loading files)
    void resetFileOptions();

    /// @brief begins the creation of an empty network
    void createNewNetwork();

    /// @brief begins the loading of an existent network
    void loadNetwork();

    /// @brief begins the loading of an existent configuration (netconvert, netedit or sumo config)
    void loadConfig();

    /// @brief Retrieves messages from the loading module
    void retrieveMessage(const MsgHandler::MsgType type, const std::string& msg);

    /// @brief clears and initializes the OptionsCont
    static void fillOptions(OptionsCont& neteditOptions);

    /// @brief sets required options for proper functioning
    static void setDefaultOptions(OptionsCont& neteditOptions);

private:
    /// @brief reset options (used for loading single networks or netconvert configs)
    bool resetOptions(const std::string& file, const bool configuration);

    /**@brief Closes the loading process
     *
     * This method is called both on success and failure.
     * All message callbacks to this instance are removed and the parent
     * application is informed about the loading
     */
    void submitEndAndCleanup(GNENet* net, const std::string& loadedFile, const std::string& guiSettingsFile = "", const bool viewportFromRegistry = false);

    /// @brief NETEDIT application windows
    GNEApplicationWindow* myApplicationWindow;

    /// @brief @brief The instances of message retriever encapsulations Needed to be deleted from the handler later on
    OutputDevice* myErrorRetriever, *myMessageRetriever, *myWarningRetriever, *myDebugRetriever, *myGLDebugRetriever;

    /// @brief event Queue
    MFXSynchQue<GUIEvent*>& myEventQueue;

    /// @brief event throw
    FXEX::MFXThreadEvent& myEventThrow;

    /// @brief Information whether only the network shall be loaded
    bool myLoadNet = false;

    /// @brief if true, a new net is created
    bool myNewNet = false;
};
