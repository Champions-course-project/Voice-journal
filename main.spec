# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/khmel/Рабочий стол/voice_journal/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/khmel/Рабочий стол/voice_journal/students_list.json', '.'), ('C:/Users/khmel/Рабочий стол/voice_journal/data.json', '.'), ('C:/Users/khmel/Рабочий стол/voice_journal/autorization.py', '.'), ('C:/Users/khmel/Рабочий стол/voice_journal/autorization_prev.py', '.'), ('C:/Users/khmel/Рабочий стол/voice_journal/icons.py', '.'), ('C:/Users/khmel/Рабочий стол/voice_journal/login_class.py', '.'), ('C:/Users/khmel/Рабочий стол/voice_journal/table.py', '.'), ('C:/Users/khmel/Рабочий стол/voice_journal/SR', 'SR/'), ('C:/Users/khmel/Рабочий стол/voice_journal/ProgrammIcon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ProgrammIcon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
