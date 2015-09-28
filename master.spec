# -*- mode: python -*-
a = Analysis(['master.py'],
             pathex=['D:\\gav\\work\\python\\Serial2web'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          [('zmq\\libsodium.pyd', 'c:\\python27\\lib\\site-packages\\zmq\\libsodium.pyd', 'BINARY')] + a.binaries + [('zmq\\css1_and_bootstrap.html', 'css1_and_bootstrap.html', 'DATA'), ],
          a.zipfiles,
          a.datas,
          name='master.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
