import logging

from src import Executor, parse_args

logging.basicConfig(level=logging.INFO, format='%(message)s')

if __name__ == '__main__':
    args = parse_args()
    executor = Executor(args.url, args.commit, args.argument)
    executor.run()
