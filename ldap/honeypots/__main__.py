#!/usr/bin/env python

from warnings import filterwarnings
filterwarnings(action='ignore', module='.*OpenSSL.*')
filterwarnings('ignore', category=RuntimeWarning, module='runpy')

from ldap_server import QLDAPServer
from argparse import ArgumentParser, SUPPRESS
from time import sleep

def main_logic():
    ARG_PARSER = ArgumentParser(description='Qeeqbox/honeypots LDAP honeypot', usage=SUPPRESS)
    ARG_PARSER_SETUP = ARG_PARSER.add_argument_group('Arguments')
    ARG_PARSER_SETUP.add_argument('--setup', help='target honeypot E.g. ldap', metavar='', default='')
    ARG_PARSER_SETUP.add_argument('--ip', help='Override the IP', metavar='', default='')
    ARG_PARSER_SETUP.add_argument('--port', help='Override the Port', metavar='', default='')
    ARG_PARSER_SETUP.add_argument('--username', help='Override the username', metavar='', default='')
    ARG_PARSER_SETUP.add_argument('--password', help='Override the password', metavar='', default='')
    ARGV = ARG_PARSER.parse_args()
    PARSED_ARG_PARSER_OPTIONAL = {action.dest: getattr(ARGV, action.dest, '') for action in ARG_PARSER_SETUP._group_actions}

    print("[!] For updates, check https://github.com/qeeqbox/honeypots")

    if ARGV.setup == 'ldap':
        x = QLDAPServer(**PARSED_ARG_PARSER_OPTIONAL)
        status = x.run_server(process=True)
        if status:
            print("[x] LDAP server running..")
            try:
                while True:
                    sleep(10)
            except KeyboardInterrupt:
                pass
            finally:
                x.kill_server()
                print("[x] LDAP server stopped.")
        else:
            print("[x] Failed to start LDAP server.")

if __name__ == '__main__':
    main_logic()

