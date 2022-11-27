##############################################################################
#
#  File:
#  AEexampleTemplate.py
#
#  Description Name:
#  Example Attribute Editor template using python and PySide/PyQt widgets.
#
#  Author:
#  David De Juan
#
##############################################################################

from PySide2 import QtGui, QtWidgets
import shiboken2

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as mui


##########################
#   ATTRIBUTE TEMPLATE   #
##########################
class AttributesTemplateUI(QtWidgets.QWidget):

    def __init__(self, layout, node):

        super(AttributesTemplateUI, self).__init__()
        self._node = node
        
        #Parent Qt widget to Maya window to avoid the widget be destroyed
        mayaMainWindowPtr = mui.MQtUtil.mainWindow()
        mayaMainWindow = shiboken2.wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)
        self.setParent(mayaMainWindow)

        #Layout from the attribute editor
        layoutPtr = mui.MQtUtil.findLayout(layout)
        layoutPtr = shiboken2.wrapInstance(long(layoutPtr), QtWidgets.QWidget)
        parentLayout = layoutObj.findChild(QtWidgets.QBoxLayout)

        #Remove ani widget from the layout
        for index in reversed(range(parentLayout.count())):
            parentLayout.itemAt(index).widget().deleteLater()

        #Create main widget
        self.mainWidget = QtWidgets.QWidget()
        self.mainWidget.setMinimumWidth(5)
        parentLayout.insertWidget(0, self.mainWidget)


    def refresh(self):
        #Refresh attribute editor, in case this was done in a floating window
        mel.eval('AEbuildControls;')



###############
#   EXAMPLE   #
###############
class ExampleAttributesUI(AttributesTemplateUI):

    def __init__(self, layout, node):
        super(ExampleAttributesUI, self).__init__(layout, node)

        exampleBtn = QtWidgets.QPushButton("Example Button")
        exampleBtn.clicked.connect(self.btnClicked)

        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addStretch()
        mainLayout.addWidget(exampleBtn)
        mainLayout.addStretch()
        self.mainWidget.setLayout(mainLayout)


    def btnClicked(self):
        print("Do stuff")