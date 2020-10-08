from google.protobuf.descriptor import EnumDescriptor
from src.enumValueDescriptorComparator import EnumValueDescriptorComparator

class EnumDescriptorComparator:
    def __init__ (
        self, 
        enumDescriptor_original: EnumDescriptor, 
        enumDescriptor_update: EnumDescriptor) -> str:
            self.enumDescriptor_original = enumDescriptor_original
            self.enumDescriptor_update = enumDescriptor_update

    def compare(self):
        # 1. If original EnumDescriptor is None, then a new EnumDescriptor is added.
        if self.enumDescriptor_original is None:
           print('A new Enum {} is added.'.format(self.enumDescriptor_update.name))
           return 'Minor change detected'
        # 2. If updated EnumDescriptor is None, then the original EnumDescriptor is removed.
        if self.enumDescriptor_update is None:
           print('BREAKING CHANGES! An Enum {} is removed'.format(self.enumDescriptor_original.name))
           return 'Major change detected'
        # 3. If both EnumDescriptors are existing, check if the name is changed.
        if (self.enumDescriptor_original.name != self.enumDescriptor_update.name):
           print('BREAKING CHANGES! Name of the Enum is changed, the original is {}, but the updated is {}'.format(self.enumDescriptor_original.name, self.enumDescriptor_update.name))
           return 'Major change detected'
        # 4. If the EnumDescriptors have the same name, check the values of them stay the same.
        enum_values_original = self.enumDescriptor_original.values
        enum_values_update = self.enumDescriptor_update.values
        i = 0
        max_len = max(len(enum_values_original), len(enum_values_update))
        while i < max_len:
            if i >= len(enum_values_update):
                return EnumValueDescriptorComparator(enum_values_original[i], None).compare()
            if i >= len(enum_values_original):
                return EnumValueDescriptorComparator(None, enum_values_update[i]).compare()
            return EnumValueDescriptorComparator(enum_values_original[i], enum_values_update[i]).compare()
         