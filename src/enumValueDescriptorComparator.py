from google.protobuf.descriptor import EnumValueDescriptor

class EnumValueDescriptorComparator:
    def __init__ (
        self, 
        enumValueDescriptor_original: EnumValueDescriptor, 
        enumValueDescriptor_update: EnumValueDescriptor) -> str:
            self.enumValueDescriptor_original = enumValueDescriptor_original
            self.enumValueDescriptor_update = enumValueDescriptor_update

    def compare(self):
        # 1. If original EnumValue is None, then a new EnumValue is added.
       if self.enumValueDescriptor_original is None:
           print('A new EnumValue {} is added.'.format(self.enumValueDescriptor_update.name))
           return 'Minor change detected'
        # 2. If updated EnumValue is None, then the original EnumValue is removed.
       if self.enumValueDescriptor_update is None:
           print('BREAKING CHANGES! An EnumValue {} is removed'.format(self.enumValueDescriptor_original.name))
           return 'Major change detected'
        # 3. If both EnumValueDescriptors are existing, check if the name is changed.
       if (self.enumValueDescriptor_original.name != self.enumValueDescriptor_update.name):
           print('BREAKING CHANGES! Name of the EnumValue is changed, the original is {}, but the updated is {}'.format(self.enumValueDescriptor_original.name, self.enumValueDescriptor_update.name))
           return 'Major change detected'
        # 4. If both EnumValueDescriptors have the same name, check if the value is changed.
       if (self.enumValueDescriptor_original.number != self.enumValueDescriptor_update.number):
           print('BREAKING CHANGES! Value of the EnumValue is changed, the original is {}, but the updated is {}'.format(self.enumValueDescriptor_original.number, self.enumValueDescriptor_update.number))
           return 'Major change detected'
       return 'No API change'

            