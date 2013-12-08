# 
import platform as p

def main():
    print("platform.architecture: {}".format(p.architecture()));

    print("platform.machine: {}".format(p.machine()));

    print("platform.node: {}".format(p.node()));

    print("platform.processor: {}".format(p.processor()));

    print("platform.python_build: {}".format(p.python_build()));

    print("platform.python_compiler: {}".format(p.python_compiler()));

    print("platform.python_branch: {}".format(p.python_branch()));

    print("platform.python_implementation: {}".format(p.python_implementation()));

    print("platform.python_revision: {}".format(p.python_revision()));

    print("platform.python_version: {}".format(p.python_version()));

    print("platform.python_version_tuple: {}".format(p.python_version_tuple()));

    print("platform.release: {}".format(p.release()));

    print("platform.system: {}".format(p.system()));

    #print("platform.system_alias: {}".format(p.system_alias()));

    print("platform.version: {}".format(p.version()));

    print("platform.uname: {}".format(p.uname()));

    print("platform.win32_ver: {}".format(p.win32_ver()));

if __name__ == '__main__':
    main()
