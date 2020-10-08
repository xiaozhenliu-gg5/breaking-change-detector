import unittest
import test.testdata.original_pb2 as original_version
import test.testdata.update_pb2 as update_version
from src.enumDescriptorComparator import EnumDescriptorComparator

class EnumDescriptorComparatorTest(unittest.TestCase):
    enum_original = original_version.DESCRIPTOR.message_types_by_name["Person"].fields_by_name['phones'].message_type.fields_by_name['type'].enum_type
    enum_update = update_version.DESCRIPTOR.message_types_by_name["Person"].fields_by_name['phones'].message_type.fields_by_name['type'].enum_type
    def test_enumRemoval(self):
        comparator = EnumDescriptorComparator(self.enum_original, None)
        self.assertEqual(comparator.compare(), 'Major change detected', "Removed the Enum {}".format(self.enum_original.name))

    def test_enumAddition(self):
        comparator = EnumDescriptorComparator(None, self.enum_update)
        self.assertEqual(comparator.compare(), 'Minor change detected', "Added the Enum {}".format(self.enum_update.name))
    
    def test_enumNameChange(self):
        comparator = EnumDescriptorComparator(self.enum_original, self.enum_update)
        self.assertEqual(comparator.compare(), 'Major change detected', "Renamed the name of EnumDescriptor")

            
    def test_noApiChange(self):
        comparator = EnumDescriptorComparator(self.enum_update, self.enum_update)
        self.assertEqual(comparator.compare(), 'No API change', "EnumDescriptor stays the same.")

if __name__ == '__main__':
    unittest.main()