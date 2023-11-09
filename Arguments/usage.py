import argparse


def usage():
    parser = argparse.ArgumentParser(description="Process performance monitoring program.", add_help=False)

    help = parser.add_argument_group(title="Help")
    obligatory = parser.add_argument_group(title="Mandatory arguments")
    optional = parser.add_argument_group(title="Optional arguments")

    # Help
    help.add_argument('-h', '--help',
                      action='help',
                      help='Print this help message and exit',
                      default=False)
    help.add_argument('-v', '--verbose',
                      action='store_true',
                      help='Activates verbose mode',
                      default=False)

    # Obligatory
    obligatory.add_argument('-p', '--pid',
                            help='PID of the process to be inspected',
                            type=int,
                            required=True,
                            dest='PID',
                            default=0)

    # Optional
    optional.add_argument('-cpu', '--cpu',
                          help='Displays CPU usage',
                          action='store_true',
                          dest='CPU',
                          default=False)
    optional.add_argument('-mem', '--memory',
                          help='Displays memory usage',
                          action='store_true',
                          dest='MEM',
                          default=False)
    optional.add_argument('-pow', '--power',
                          help='Displays energy consumption',
                          action='store_true',
                          dest='POWER',
                          default=False)
    optional.add_argument('-a', '--all',
                          help='Displays all information',
                          action='store_true',
                          dest='ALL',
                          default=False)
    optional.add_argument('-f', '--frequency',
                          help='Number of points per second wanted',
                          type=int,
                          dest='Frequency',
                          default=10)
    optional.add_argument('-i', '--interval',
                          help='Time of inspection (in seconds) default: infinite',
                          type=float,
                          dest='Interval',
                          default=float('inf'))
    optional.add_argument('-plot', '--plot',
                          help='Display graphics',
                          action='store_true',
                          dest='Plot',
                          default=False)
    optional.add_argument('-s', '--save',
                          help='Writes all data to files',
                          type=str,
                          dest='Save')
    args = parser.parse_args()

    return args
