import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button {
    id: button

    // Custom Properites
    property color colorDefault: "#4891d9"
    property color colorOnFocus: "#55AAFF"
    property color colorMouseOver: "#3F7EBD"
    width: 200
    height: 40

    QtObject{
        id: internal

        property var dynamicColor: if(button.down){
                                       button.down ? colorOnFocus : colorDefault
                                   }else{
                                       button.hovered ? colorMouseOver : colorDefault
                                   }
    }


    text: qsTr("Button")
    flat: false
    contentItem: Item {
        id: item1
        Text {
            id: name
            text: button.text
            font: button.font
            color: "#ffffff"
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    background: Rectangle{
        color: internal.dynamicColor
        radius: 10
    }

}

/*##^##
Designer {
    D{i:0;formeditorZoom:4}
}
##^##*/
