import unittest
import doctest

from zope.testing import doctestunit
from zope.component import testing

# Test data - we put it here to allow proper dotted names in the test.

from zope.interface import Interface
from zope import schema

class IMailSettings(Interface):
    """Settings for email
    """
    
    sender = schema.TextLine(title=u"Mail sender", default=u"root@localhost")
    smtp_host = schema.URI(title=u"SMTP host server")

class IMailPreferences(Interface):
    """Settings for email
    """
    
    max_daily = schema.Int(title=u"Maximum number of emails per day", min=0, default=3)
    settings = schema.Object(title=u"Mail setings to use", schema=IMailSettings)

def test_suite():
    return unittest.TestSuite([
        doctestunit.DocFileSuite(
            'registry.txt', package='plone.registry',
            optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
            setUp=testing.setUp, tearDown=testing.tearDown),
        doctestunit.DocFileSuite(
            'field.txt', package='plone.registry',
            optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
            setUp=testing.setUp, tearDown=testing.tearDown),
        ])
