#!/usr/bin/env python

"""
Copyright 2016 Fedele Mantuano (https://twitter.com/fedelemantuano)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import argparse
import logging
import sys

import mailparser
from mailparser.exceptions import MailParserOutlookError
from mailparser.utils import (
    custom_log,
    print_attachments,
    print_mail_fingerprints,
    safe_print,
    write_attachments,
)
from mailparser.version import __version__

log = logging.getLogger("mailparser")


def get_args():
    """
    Get arguments from command line.
    :return: argparse.ArgumentParser
    :rtype: argparse.ArgumentParser
    """
    pass


def main():
    """
    Main function.
    """
    pass


def get_parser(args):
    """
    Get the correct parser based on the input source.
    :param args: argparse.Namespace
    :type args: argparse.Namespace
    :return: MailParser
    :rtype: mailparser.core.MailParser
    """
    pass


def parse_file(args):
    """
    Parse the file based on the arguments provided.
    :param args: argparse.Namespace
    :type args: argparse.Namespace
    :return: MailParser
    :rtype: mailparser.core.MailParser
    """
    pass


def parse_stdin(args):
    """
    Parse the stdin based on the arguments provided.
    :param args: argparse.Namespace
    :type args: argparse.Namespace
    :return: MailParser
    :rtype: mailparser.core.MailParser
    """
    pass


def process_output(args, parser):
    """
    Process the output based on the arguments provided.
    :param args: argparse.Namespace
    :type args: argparse.Namespace
    :param parser: MailParser
    :type parser: mailparser.core.MailParser
    :param log: logger
    :type log: logging.Logger
    """
    pass


def print_defects(parser):
    """
    Print email defects.
    :param parser: MailParser
    :type parser: mailparser.core.MailParser
    """
    pass


def print_sender_ip(parser, args):
    """
    Print sender IP address.
    :param parser: MailParser
    :type parser: mailparser.core.MailParser
    :param args: argparse.Namespace
    :type args: argparse.Namespace
    """
    pass


def print_attachments_details(parser, args):
    """
    Print attachments details.
    :param parser: MailParser
    :type parser: mailparser.core.MailParser
    :param args: argparse.Namespace
    :type args: argparse.Namespace
    """
    pass


if __name__ == "__main__":  # pragma: no cover
    main()
