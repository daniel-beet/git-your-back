# -*- mode: python -*-
a = Analysis(['gyb.py'],
             pathex=['C:\\Users\\jlee\\Documents\\GitHub\\got-your-back'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gyb.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )