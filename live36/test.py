from argparse import ArgumentParser

parser = ArgumentParser(prog='ShellTests',
                        usage='ShellTests [arg]',
                        description='Para usar isso, faça isso',
                        epilog='Done???',
                        fromfile_prefix_chars='@')


# parser.add_argument('y')
# parser.add_argument('x')
# parser.add_argument('-bar', '-b', '--bar', action='store')
# parser.add_argument('-bar', '-b', '--bar', action='append', dest='xpto')
parser.add_argument('-foo', '-f', '--foo', type=float, action='append', dest='xpto')
parser.add_argument('-s', const='str', action='append_const', dest='xpto')
parser.add_argument('-i', const='int', action='append_const', dest='xpto')
parser.add_argument('-v', action='count', default=0)
parser.add_argument('-xpto2', default=0, type=int, choices=[1, 2, 3], required=True,
                    help='xpto, a arte pythonica', metavar='XPTO')

args = parser.parse_args()
print(args)