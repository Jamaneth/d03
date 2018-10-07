import sys
import antigravity

def terminal_arguments():

    term_args = sys.argv[1:]

    if len(term_args) != 3:
        raise Exception('Three arguments only (latitude, longitude, today\'s Dow opening)')

    try:
        term_args[0], term_args[1] = float(term_args[0]), float(term_args[1])
        int(term_args[2])
        term_args[2] = term_args[2].encode('utf-8')
    except:
        raise ValueError('Wrong type of argument.')

    return term_args

if __name__ == '__main__':

    geo_args = terminal_arguments()
    print(antigravity.geohash(geo_args[0], geo_args[1], geo_args[2]))
