class SuccessResponse:
    created = {'message': 'User added'}


class Errors:
    user_exists = {'message': 'User already exists'}
    empty_field = {'message': 'Fill all fields'}
    user_not_found = {'message': 'User not found'}
    incorrect_fields = {'message': 'Check the fields'}
    user_deleted = {'message': 'User deleted'}
    failed_to_create = {'message': 'Failed to create user'}
    failed_to_login = {'message': 'You should log in before you make this request'}

