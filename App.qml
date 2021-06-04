import QtQuick.Controls 2.1

ApplicationWindow {
    id: fullScreenUI
    width: 1280
    height: 720
    visible: true
    // visibility: "FullScreen"

    property var iniITEM: "LedGui.qml"

    StackView {
        id: stack
        initialItem: iniITEM
    }
}