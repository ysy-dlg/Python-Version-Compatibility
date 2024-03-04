def on_header_sectionClicked(self, index):
    ...
    #FIXME: position the menu correctly
    headerPos = self.view.mapToGlobal(self.header.pos())        
    posY = headerPos.y() + self.header.height()
    posX = headerPos.x() + self.header.sectionViewportPosition(self.col_index)        
    menu.exec_(QPoint(posX, posY))
