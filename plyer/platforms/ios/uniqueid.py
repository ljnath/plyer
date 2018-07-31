'''
Module of iOS API for plyer.uniqueid.
'''

from pyobjus import autoclass  # pylint: disable=import-error
from pyobjus.dylib_manager import load_framework  # pylint:disable=import-error
from plyer.facades import UniqueID

load_framework('/System/Library/Frameworks/UIKit.framework')
UIDEVICE = autoclass('UIDevice')


class IOSUniqueID(UniqueID):
    '''
    Implementation of iOS uniqueid API.
    '''

    def _get_uid(self):
        uuid = UIDEVICE.currentDevice().identifierForVendor.UUIDString()
        return uuid.UTF8String()


def instance():
    '''
    Instance for facade proxy.
    '''
    return IOSUniqueID()
