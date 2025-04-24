import subprocess

# 실행할 .py 파일 목록
scripts = ["test01.py", "test02.py", "test03.py"]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script])




'''
Run
- py test.py
'''