import kleis.src.generated.permission_pb2 as permission_pb2
import kleis.src.generated.response_pb2 as response_pb2
from google.protobuf.json_format import MessageToJson


def make_permission(name: str, permission_flag: bool) -> response_pb2.PermissionResponse():
    check_groups = response_pb2.CheckedGroup()
    check_groups.name = 'sample_group'
    check_groups.permission = True
    return check_groups


permission = response_pb2.PermissionResponse()
for i in range(10):
    check_groups = make_permission(f"sample_group_{i}", True)
    permission.checked_groups.extend([check_groups])


print(MessageToJson(permission))


"""
Example to create protobuf to python code

Don't forget to export
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python 
"""

# mkdir src/generated
# protoc src/interfaces/person_info.proto --python_out src/ --proto_path generated=./src/interfaces/
# protoc src/interfaces/person.proto --python_out src/ --proto_path generated=./src/interfaces/