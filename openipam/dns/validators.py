from django.core.exceptions import ValidationError

import re


FQDN = "([0-9A-Za-z]+\.[0-9A-Za-z]+|[0-9A-Za-z]+[\-0-9A-Za-z\.]*[0-9A-Za-z])"

def validate_fqdn(value):
    '''
    Returns true if argument is syntactically a fully qualified domain name, false otherwise
    Doesn't actually validate TLDs, mostly allows periods past hostnames
    '''
    re_fqdn = re.compile("^"+FQDN+"$")
    if not re_fqdn.search(value):
        raise ValidationError('Invalid Name: %s' % value)


def validate_srv_content(value):
    '''
    Validate an srv record's content field
    Assumes priority has already been stripped out
    '''

    re_srv = re.compile('^(\d+ \d+ %s)$' % FQDN)
    if not re_srv.search(value):
        raise ValidationError('Invalid SRV Content: %s' % value)


def validate_soa_content(value):
    '''Validate an soa record's content field'''

    re_soa = re.compile('^%s [A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4} \d+ \d+ \d+ \d+ \d+$' % FQDN)
    if not re_soa.search(value):
        raise ValidationError('Invalid SOA Content: %s' % value)


def validate_sshfp_content(value):

    if not re.match('^[12] 1 [0-9A-F]{40}', value):
        raise ValidationError("Invalid SSHFP content: %s" % value)