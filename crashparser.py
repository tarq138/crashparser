import sys
import re
import json


def main(argv):
    try:
        LogFile = argv[0]
        JsonFile = argv[1]
        with open(LogFile, 'r') as filelog, open(JsonFile, 'w') as OutputFile:
            DataLog = re.search(r'({\s*)(.*)(})', filelog.read())
            if DataLog:
                json.dump(json.loads(DataLog.group(0)), OutputFile, indent=2, sort_keys=True)
            else:
                print("Incorrect log file")

    except IndexError:
        print("Please, input name log file and name output file")




if __name__ == '__main__':
    main(sys.argv[1:])
