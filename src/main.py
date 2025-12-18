# Initial start script. 

# This imports shouldn't fail if PyInstaller bundled everything correctly
import sys
import qt_adv_vars as a
if '--version' in sys.argv or '-v' in sys.argv:
    from ver import ver
    print(f'nameCheck version: {ver}')
    input('Press enter to close the program...')
    quit()
if '--debug' in sys.argv or '-d' in sys.argv:
    a.debug = 1
if '--help' in sys.argv or '-help' in sys.argv:
    from qt_adv_vars import helptxt
    print(helptxt)
    input('Press enter to exit the program')
    quit()

if len(sys.argv) > 1 and sys.argv[1] == 'cli':
    import cli_init
    cli_init.cli_init()
    if '--batch' not in sys.argv: input('Press enter to exit...')
else:
    import gui_init
    gui_init.run()