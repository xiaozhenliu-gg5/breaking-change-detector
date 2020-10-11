import unittest
import test.testdata.original_pb2 as original_version

from src.comparator.enumValueComparator import EnumValueComparator
from src.findings.findingContainer import FindingContainer
from src.findings.utils import FindingCategory

class EnumValueComparatorTest(unittest.TestCase):
    def setUp(self):
        enum_type_values = original_version.DESCRIPTOR.message_types_by_name["Person"].fields_by_name['phones'].message_type.fields_by_name['type'].enum_type.values
        self.enumValue_mobile = enum_type_values[0]
        self.enumValue_home = enum_type_values[1]

    def tearDown(self):
        FindingContainer.reset()

    def test_enumValueRemoval(self):
        comparator = EnumValueComparator(self.enumValue_mobile, None).compare()
        finding = FindingContainer.getAllFindings()[0]
        self.assertEqual(finding.message, 'An EnumValue MOBILE is removed')
        self.assertEqual(finding.category.name, 'ENUM_VALUE_REMOVAL')


    def test_enumValueAddition(self):
        comparator = EnumValueComparator(None, self.enumValue_home).compare()
        finding = FindingContainer.getAllFindings()[0]
        self.assertEqual(finding.message, 'A new EnumValue HOME is added.')
        self.assertEqual(finding.category.name, 'ENUM_VALUE_ADDITION')

    def test_enumValueNameChange(self):
        comparator = EnumValueComparator(self.enumValue_mobile, self.enumValue_home).compare()
        finding = FindingContainer.getAllFindings()[0]
        self.assertEqual(finding.message, 'Name of the EnumValue is changed, the original is MOBILE, but the updated is HOME')
        self.assertEqual(finding.category.name, 'ENUM_VALUE_NAME_CHANGE')

    def test_noApiChange(self):
        comparator = EnumValueComparator(self.enumValue_mobile, self.enumValue_mobile).compare()
        self.assertEqual(len(FindingContainer.getAllFindings()), 0)

if __name__ == '__main__':
    unittest.main()