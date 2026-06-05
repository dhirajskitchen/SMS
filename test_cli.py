import subprocess

cases = {
    'student': '1\n1\n1\n6\n6\n',
    'teacher': '2\n6\n6\n',
    'principal': '3\n4\n6\n',
    'applicant': '4\n3\n6\n',
    'parent': '5\n1\n1\n5\n6\n',
}

for name, data in cases.items():
    r = subprocess.run(['python', 'main.py'], input=data, text=True, capture_output=True, cwd=r'z:\2 VGTS\SMS')
    print('===', name, 'RC=', r.returncode, '===')
    out = (r.stdout or '') + (r.stderr or '')
    print(out[:4000])
    if r.returncode != 0:
        print('FAILED')
