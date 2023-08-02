from calc import rm

import mock
import unittest


class RmTestCase(unittest.TestCase):

    @mock.patch('calc.os.path')
    @mock.patch('calc.os')
    def test_rm(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False
        #parent calling function #WikiBuilder
        rm("any path")

        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_path.isfile.return_value = True

        rm("any path")

        mock_os.remove.assert_called_with("any path")