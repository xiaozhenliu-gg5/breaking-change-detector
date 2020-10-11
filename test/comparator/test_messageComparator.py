import unittest
import test.testdata.original_pb2 as original_version
import test.testdata.update_pb2 as update_version
from src.comparator.messageComparator import DescriptorComparator
from src.findings.findingContainer import FindingContainer
from src.findings.utils import FindingCategory

class DescriptorComparatorTest(unittest.TestCase):
    def setUp(self):
        self.person_msg = original_version.DESCRIPTOR.message_types_by_name["Person"]
        self.person_msg_update = update_version.DESCRIPTOR.message_types_by_name["Person"]
        self.addressBook_msg = original_version.DESCRIPTOR.message_types_by_name["AddressBook"]
        self.addressBook_msg_update = update_version.DESCRIPTOR.message_types_by_name["AddressBook"]

    def tearDown(self):
        FindingContainer.reset()

    def test_messageRemoval(self):
        DescriptorComparator(self.person_msg, None).compare()
        finding = FindingContainer.getAllFindings()[0]
        self.assertEqual(finding.message, 'A message Person is removed')
        self.assertEqual(finding.category.name, 'MESSAGE_REMOVAL')

    def test_messageAddition(self):
        DescriptorComparator(None, self.addressBook_msg).compare()
        finding = FindingContainer.getAllFindings()[0]
        self.assertEqual(finding.message, 'A new message AddressBook is added.')
        self.assertEqual(finding.category.name, 'MESSAGE_ADDITION')  

    def test_fieldChange(self):
        DescriptorComparator(self.addressBook_msg, self.addressBook_msg_update).compare()
        finding = FindingContainer.getAllFindings()[0]
        self.assertEqual(finding.message, 'The Field deprecated is moved out of one-of')
        self.assertEqual(finding.category.name, 'FIELD_ONEOF_REMOVAL')  

    def test_nestedMessageChange(self):
        # Field `type` in nested message `PhoneNumber` is re-numbered. So it is taken as one field removed and one field added.
        DescriptorComparator(self.person_msg, self.person_msg_update).compare()
        findingLength = len(FindingContainer.getAllFindings())
        self.assertEqual(FindingContainer.getAllFindings()[findingLength - 1].category.name, 'FIELD_ADDITION')
        self.assertEqual(FindingContainer.getAllFindings()[findingLength - 2].category.name, 'FIELD_REMOVAL')

if __name__ == '__main__':
    unittest.main()