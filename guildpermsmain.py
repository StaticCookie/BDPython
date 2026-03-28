can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    permission_check = can_create_guild & user_permissions
    return permission_check


def get_review_bits(user_permissions):
    permission_check = can_review_guild & user_permissions
    return permission_check


def get_delete_bits(user_permissions):
    permission_check = can_delete_guild & user_permissions
    return permission_check


def get_edit_bits(user_permissions):
    permission_check = can_edit_guild & user_permissions
    return permission_check
