class IntrospectionInfo:
    def __init__(self, obj):
        self.obj = obj

    def type_info(self):
        return type(self.obj)

    def attributes_info(self):
        return dir(self.obj)

    def methods_info(self):
        methods = []
        for attr in self.attributes_info():
            if attr[0] != '_':
                methods.append(attr)
        return methods

    def module_info(self):
        module = self.obj.__class__.__module__
        if module == 'builtins':
            module = '__main__'
        return module


def introspection_info(obj):
    helper = IntrospectionInfo(obj)
    info = {
        'type': helper.type_info(),
        'attributes': helper.attributes_info(),
        'methods': helper.methods_info(),
        'module': helper.module_info()}
    return info


number_info = introspection_info(42)
print(number_info)
