import sys
import yaml

def do_yaml_load(file_name):
    with open(file_name) as f:
        print yaml.load(f)

def do_yaml_dump(file_name):
    data = {"First": "First Name"}
    print yaml.dump(data)
    
def show_usage(app_name):
    print app_name + " [load|dump] config.yaml"

def main(argvs):
    if len(argvs) == 3:
        if cmp(argvs[1], "load") == 0:
            do_yaml_load(argvs[2])
        elif cmp(argvs[1], "dump") == 0:
            do_yaml_dump(argvs[2])
        else:
            show_usage(argvs[0])
    else:
        show_usage(argvs[0])

if __name__ == "__main__":
    main(sys.argv)
