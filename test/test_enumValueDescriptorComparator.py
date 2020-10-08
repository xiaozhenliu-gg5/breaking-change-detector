import unittest
import test.testdata.original_pb2 as original_version

from src.enumValueDescriptorComparator import EnumValueDescriptorComparator

class EnumValueDescriptorComparatorTest(unittest.TestCase):
    enum_type_values = original_version.DESCRIPTOR.message_types_by_name["Person"].fields_by_name['phones'].message_type.fields_by_name['type'].enum_type.values
    enumValue_mobile = enum_type_values[0]
    enumValue_home = enum_type_values[1]
    def test_enumValueRemoval(self):
        comparator = EnumValueDescriptorComparator(self.enumValue_mobile, None)
        self.assertEqual(comparator.compare(), 'Major change detected', "Removed the EnumValue {}".format(self.enumValue_mobile.name))

    def test_enumValueAddition(self):
        comparator = EnumValueDescriptorComparator(None, self.enumValue_home)
        self.assertEqual(comparator.compare(), 'Minor change detected', "Added the EnumValue {}".format(self.enumValue_home.name))
    
    def test_enumValueNameChange(self):
        comparator = EnumValueDescriptorComparator(self.enumValue_mobile, self.enumValue_home)
        self.assertEqual(comparator.compare(), 'Major change detected', "Renamed the name of EnumValueDescriptor")

    def test_noApiChange(self):
        comparator = EnumValueDescriptorComparator(self.enumValue_mobile, self.enumValue_mobile)
        self.assertEqual(comparator.compare(), 'No API change', "EnumValue stays the same.")

if __name__ == '__main__':
    unittest.main()