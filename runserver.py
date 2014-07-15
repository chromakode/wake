#!/usr/bin/env python
import argparse

from wake import app


parser = argparse.ArgumentParser()
parser.add_argument(
    '--host',
    default='127.0.0.1',
    help='hostname to listen on',
)
parser.add_argument(
    '--port',
    type=int,
    default=5000,
    help='port to listen on',
)
parser.add_argument(
    '--debug',
    type=bool,
    default=True,
    help='toggle tracebacks and debugger',
)
args = parser.parse_args()

app.run(host=args.host, port=args.port, debug=args.debug)
