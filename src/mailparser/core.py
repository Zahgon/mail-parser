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

import base64
import email
import ipaddress
import json
import logging
import os

from mailparser.const import ADDRESSES_HEADERS, EPILOGUE_DEFECTS, REGXIP, REGXIP6
from mailparser.utils import (
    convert_mail_date,
    decode_header_part,
    find_between,
    get_addresses,
    get_header,
    get_mail_keys,
    get_to_domains,
    msgconvert,
    ported_open,
    ported_string,
    random_string,
    receiveds_parsing,
    write_attachments,
)

log = logging.getLogger(__name__)


def parse_from_file_obj(fp):
    """
    Parsing email from a file-like object.

    Args:
        fp (file-like object): file-like object of raw email

    Returns:
        Instance of MailParser with raw email parsed
    """
    pass


def parse_from_file(fp):
    """
    Parsing email from file.

    Args:
        fp (string): file path of raw email

    Returns:
        Instance of MailParser with raw email parsed
    """
    pass


def parse_from_file_msg(fp):
    """
    Parsing email from file Outlook msg.

    Args:
        fp (string): file path of raw Outlook email

    Returns:
        Instance of MailParser with raw email parsed
    """
    pass


def parse_from_string(s):
    """
    Parsing email from string.

    Args:
        s (string): raw email

    Returns:
        Instance of MailParser with raw email parsed
    """
    pass


def parse_from_bytes(bt):
    """
    Parsing email from bytes. Only for Python 3

    Args:
        bt (bytes-like object): raw email as bytes-like object

    Returns:
        Instance of MailParser with raw email parsed
    """
    pass


class MailParser:
    """
    MailParser package provides a standard parser that understands
    most email document structures like official email package.
    MailParser handles the encoding of email and split the raw email for you.

    Headers:
    https://www.iana.org/assignments/message-headers/message-headers.xhtml
    """

    def __init__(self, message=None):
        """
        Init a new object from a message object structure.
        """
        self._message = message
        if message is not None:
            log.debug("All headers of emails: {}".format(", ".join(message.keys())))
        self.parse()

    def __str__(self) -> str:
        if self.message:
            return str(self.subject)
        else:
            return str()

    @classmethod
    def from_file_obj(cls, fp):
        """
        Init a new object from a file-like object.
        Not for Outlook msg.

        Args:
            fp (file-like object): file-like object of raw email

        Returns:
            Instance of MailParser
        """
        pass

    @classmethod
    def from_file(cls, fp, is_outlook=False):
        """
        Init a new object from a file path.

        Args:
            fp (string): file path of raw email
            is_outlook (boolean): if True is an Outlook email

        Returns:
            Instance of MailParser
        """
        pass

    @classmethod
    def from_file_msg(cls, fp):
        """
        Init a new object from a Outlook message file,
        mime type: application/vnd.ms-outlook

        Args:
            fp (string): file path of raw Outlook email

        Returns:
            Instance of MailParser
        """
        pass

    @classmethod
    def from_string(cls, s):
        """
        Init a new object from a string.

        Args:
            s (string): raw email

        Returns:
            Instance of MailParser
        """
        pass

    @classmethod
    def from_bytes(cls, bt):
        """
        Init a new object from bytes.

        Args:
            bt (bytes-like object): raw email as bytes-like object

        Returns:
            Instance of MailParser
        """
        pass

    def _reset(self):
        """
        Reset the state of mail object.
        """
        pass

    def _append_defects(self, part, part_content_type):
        """
        Add new defects and defects categories to object attributes.

        The defects are a list of all the problems found
        when parsing this message.

        Args:
            part (string): mail part
            part_content_type (string): content type of part
        """
        pass

    def _make_mail(self, complete=True):
        """
        This method assigns the right values to all tokens of email.
        Returns a parsed object

        Keyword Arguments:
            complete {bool} -- If True returns all mails parts
                                (default: {True})

        Returns:
            dict -- Parsed email object
        """
        pass

    def parse(self):
        """
        This method parses the raw email and makes the tokens.

        Returns:
            Instance of MailParser with raw email parsed
        """
        pass

    def get_server_ipaddress(self, trust):
        """
        Return the ip address of sender

        Overview:
        Extract a reliable sender IP address heuristically for each message.
        Although the message format dictates a chain of relaying IP
        addresses in each message, a malicious relay can easily alter that.
        Therefore we cannot simply take the first IP in
        the chain. Instead, our method is as follows.
        First we trust the sender IP reported by our mail server in the
        Received headers, and if the previous relay IP address is on our trust
        list (e.g. other well-known mail services), we continue to
        follow the previous Received line, till we reach the first unrecognized
        IP address in the email header.

        From article Characterizing Botnets from Email Spam Records:
            Li Zhuang, J. D. Tygar

        In our case we trust only our mail server with the trust string.

        Args:
            trust (string): String that identify our mail server

        Returns:
            string with the ip address
        """
        pass

    def _extract_ip(self, received_header):
        """
        Extract the IP address from the received header if it is not private.
        Supports both IPv4 (RFC 791) and IPv6 (RFC 5952) addresses.

        Args:
            received_header (string): The received header string

        Returns:
            string with the ip address or None
        """
        pass

    def write_attachments(self, base_path):
        """This method writes the attachments of mail on disk

        Arguments:
            base_path {str} -- Base path where write the attachments
        """
        pass

    def __getattr__(self, name):
        name = name.strip("_").lower()
        name_header = name.replace("_", "-")

        # json headers
        if name.endswith("_json"):
            name = name[:-5]
            return json.dumps(getattr(self, name), ensure_ascii=False)

        # raw headers
        elif name.endswith("_raw"):
            name = name[:-4]
            raw = self.message.get_all(name) if self.message else None
            return json.dumps(raw, ensure_ascii=False)

        # object headers
        elif name_header in ADDRESSES_HEADERS:
            raw_header = self.message.get(name_header, "") if self.message else ""
            # Parse addresses. RFC 5322 Â§3.4 does not allow unquoted "@" in
            # display names, so a strict parser correctly rejects headers like
            #   From: alice@example.com <bob@example.com>
            # and returns ('', '').  mail-parser is a security/forensics tool,
            # not an MTA: hiding addresses from analysts is worse than accepting
            # non-conforming input.  get_addresses() applies a regex fallback
            # when strict parsing yields only empty results â€” see its docstring
            # in utils.py for the full rationale.
            parsed_addresses = get_addresses(raw_header)

            # decoded addresses â€” skip entries with no address (absent header)
            return [
                (
                    (
                        ""
                        if (decoded_name := decode_header_part(name)) == email_addr
                        else decoded_name
                    ),
                    email_addr,
                )
                for name, email_addr in parsed_addresses
                if email_addr
            ]

        # others headers
        else:
            return get_header(self.message, name_header)

    @property
    def attachments(self):
        """
        Return a list of all attachments in the mail
        """
        pass

    @property
    def received(self):
        """
        Return a list of all received headers parsed
        """
        pass

    @property
    def received_json(self):
        """
        Return a JSON of all received headers
        """
        pass

    @property
    def received_raw(self):
        """
        Return a list of all received headers in raw format
        """
        pass

    @property
    def body(self):
        """
        Return all text plain and text html parts of mail delimited from string
        "--- mail_boundary ---"
        """
        pass

    @property
    def headers(self) -> dict:
        """
        Return only the headers as Python object
        """
        pass

    @property
    def headers_json(self):
        """
        Return the JSON of headers
        """
        pass

    @property
    def text_plain(self):
        """
        Return a list of all text plain parts of email.
        """
        pass

    @property
    def text_html(self):
        """
        Return a list of all text html parts of email.
        """
        pass

    @property
    def text_not_managed(self):
        """
        Return a list of all text not managed of email.
        """
        pass

    @property
    def date(self):
        """
        Return the mail date in datetime.datetime format and UTC.
        """
        pass

    @property
    def timezone(self):
        """
        Return timezone. Offset from UTC.
        """
        pass

    @property
    def date_json(self):
        """
        Return the JSON of date
        """
        pass

    @property
    def mail(self):
        """
        Return the Python object of mail parsed
        """
        pass

    @property
    def mail_json(self):
        """
        Return the JSON of mail parsed
        """
        pass

    @property
    def mail_partial(self):
        """
        Return the Python object of mail parsed
        with only the mains headers
        """
        pass

    @property
    def mail_partial_json(self):
        """
        Return the JSON of mail parsed partial
        """
        pass

    @property
    def defects(self):
        """
        The defects property contains a list of
        all the problems found when parsing this message.
        """
        pass

    @property
    def defects_categories(self):
        """
        Return a set with only defects categories.
        """
        pass

    @property
    def has_defects(self):
        """
        Return a boolean: True if mail has defects.
        """
        pass

    @property
    def message(self):
        """
        email.message.Message class.
        """
        pass

    @property
    def message_as_string(self):
        """
        Return the entire message flattened as a string.
        """
        pass

    @property
    def to_domains(self):
        """
        Return all domain of 'to' and 'reply-to' email addresses
        """
        pass
