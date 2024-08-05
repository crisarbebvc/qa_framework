import subprocess
import os

def execute_jar(jar_file):
    try:
        p = subprocess.check_output(["java", "-jar", jar_file])
        return p.replace(b"\r\n", b"\n").decode("utf-8")
    except Exception as e:
        return str(e)

def file_exists(file_name):
    try:
        if os.path.exists(file_name):
            return True
        else:
            return False
    except Exception as e:
        return str(e)
    
def content_file(file_name):
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return str(e)