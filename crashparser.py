import json
import sys

Errors = ["Error", "Exit", "Key", "Stop", "Exception:"]

def main(argv):
    try:
        LogFile = argv[0]
        JsonFile = argv[1]
        Exception = False
        with open(LogFile, 'r') as filelog, open(JsonFile, 'w') as OutputFile:
            ans = '{"filename" : "' + LogFile + '", "exceptions" : ['
            findstr = ''
            for line in filelog:
                if 'Traceback' in line:
                    findstr = 'line'
                elif (findstr in line) & (findstr == 'line'):
                    i = int(line.find(findstr)+5)
                    if Exception:
                        ans += ','
                    ans += '{"line" : '
                    while line[i] != ',':
                        ans += line[i]
                        i += 1
                    ans += ', "type" : "'
                    findstr = 'errors'
                elif findstr == 'errors':
                    for Error in Errors:
                        if Error in line:
                            i = int(line.find(':')-1)
                            j = i + 3
                            typeerror = ''
                            while (i >= 0) | (line[i] == ' '):
                                typeerror = line[i] + typeerror
                                i -= 1
                            ans = ans + typeerror + '", "message" : "' + line[j:len(line)-1] + '"}'
                            Exception = True
                            findstr = ''
            ans += ']}'
            json.dump(json.loads(ans), OutputFile, indent=4, sort_keys=True)
    except IndexError:
        print("Please, input name log file and name output file")

if __name__ == '__main__':
    main(sys.argv[1:])
