from multiprocessing.process import Process
import itertools
import sys
import time

class ProgressIndicatorOnConsole(Process):
    ''' This class is useful when you have a long running process(es) and you want some indication
    to not be bored.
    
    This cannot be connect to the process(es) runing background, this is just a "counter"
    
    For example:
        (Please consider it as a joke)
    
    indicator = ProgressIndicatorOnConsole()
    indicator.start()

    with open('names.json', 'r') as fi:
        names = json.load(fi)

    pool = Pool()
    result = pool.map(brute_force_attack, names)
    
    if (indicator.is_alive()):
        indicator.terminate()
    '''

    def run(self):
        c = 0
        watch = itertools.cycle('-\\|/')
        while(True):
            sys.stdout.write('\r' + watch.next())
            sys.stdout.flush()
            time.sleep(1)
            c += 1
            if not c % 45:
                print '\n\n***\t', c / 60.0, 'min(s)'
