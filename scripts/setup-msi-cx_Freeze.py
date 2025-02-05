import cx_Freeze
import os
import sys

sys.path.append(os.path.realpath(sys.path[0] + '\\..\\src'))

shortcut_table = [
  (
    'StartupShortcut',        # Shortcut
    'StartupFolder',          # Directory
    'WinSwitcher',           # Name
    'TARGETDIR',              # Component
    '[TARGETDIR]WinSwitcher.exe',# Target
    None,                     # Arguments
    None,                     # Description
    None,                     # Hotkey
    None,                     # Icon
    None,                     # IconIndex
    None,                     # ShowCmd
    'TARGETDIR'               # WkDir
  ),
  (
    'DesktopShortcut',        # Shortcut
    'DesktopFolder',          # Directory
    'WinSwitcher',           # Name
    'TARGETDIR',              # Component
    '[TARGETDIR]WinSwitcher.exe',# Target
    None,                     # Arguments
    None,                     # Description
    None,                     # Hotkey
    None,                     # Icon
    None,                     # IconIndex
    None,                     # ShowCmd
    'TARGETDIR'               # WkDir
  ),
]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}

options = {
  'include_files': ['..\\src\\locales'],
  # 'build_exe': '..\\build\\WinSwitcher',
}
executables = [cx_Freeze.Executable('..\\src\\WinSwitcher.py',
  base = 'Win32GUI',
  targetName = 'WinSwitcher.exe'
  )]

cx_Freeze.setup(
  name = 'WinSwitcher' ,
  version = '0.1' ,
  description = 'Utility which brings easier application and windows switching to Microsoft Windows.',
  options = {
    'bdist_msi': bdist_msi_options,
    'build_exe': options,
    },
  executables = executables
  )
