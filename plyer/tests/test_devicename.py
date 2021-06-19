'''
TestDeviceName
============

Tested platforms:

* Windows
'''

import unittest
from mock import patch
from plyer.tests.common import PlatformTest, platform_import
import socket


class TestDeviceName(unittest.TestCase):
    '''
    TestCase for plyer.devicename.
    '''

    @PlatformTest('win')
    def test_devicename_win(self):
        '''
        Test Windows API for plyer.devicename.
        '''
        devicename = platform_import(platform='win',
                                     module_name='devicename'
                                     )
        devicename_instance = devicename.instance()

        with patch.object(socket,
                          'gethostname',
                          return_value='mocked_windows_hostname'
                          ) as mock_method:

            evaluated_device_name = devicename_instance._get_device_name()
            self.assertEqual(evaluated_device_name, 'mocked_windows_hostname')

    @PlatformTest('linux')
    def test_devicename_linux(self):
        '''
        Test Linux API for plyer.devicename.
        '''
        devicename = platform_import(platform='linux',
                                     module_name='devicename'
                                     )
        devicename_instance = devicename.instance()

        with patch.object(socket,
                          'gethostname',
                          return_value='mocked_linux_hostname'
                          ) as mock_method:

            evaluated_device_name = devicename_instance._get_device_name()
            self.assertEqual(evaluated_device_name, 'mocked_linux_hostname')


if __name__ == '__main__':
    unittest.main()
