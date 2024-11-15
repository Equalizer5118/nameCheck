try:
    from PySide6.QtWidgets import QApplication, QWidget
    from PySide6.QtCore import QSize
    from qt_mainwindow import DefWindow
    import nameCheck
    import spreadsheetms
    import qt_univerr
    import debugprint
    import configcreate
    import sys
    nameCheck.echo()
    qt_univerr.echo()
    debugprint.echo()
    configcreate.echo()
    spreadsheetms.echo()
    app = QApplication(sys.argv)

    window = DefWindow()
    window.show()
    #window.setFixedSize(QSize(165, 250))

    app.exec()

except Exception as e:
    try:
        qt_univerr.funcerror(f'Program failed to initialize! \n Error: {e}')
    except:
        print(f'There was a critical error, likely to do with QT failing to initialize. Here is the full trace:')
        print(e.__traceback__)
        print(e)
        input('Press enter key to close...')