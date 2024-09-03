#!/usr/bin/env python3
# -*-coding:UTF-8 -*

import os
import sys

sys.path.append(os.environ['AIL_BIN'])
##################################
# Import Project packages
##################################
from lib import ail_orgs
from lib import ail_users

if __name__ == "__main__":

    user_id = 'admin@admin.test'
    password = ail_users.gen_password()

    # create role_list
    ail_users._create_roles_list()

    if not ail_users.exists_user(user_id):
        # Create Default Org
        org = ail_orgs.create_default_org()
        ail_users.create_user(user_id, password=password, admin_id='admin@admin.test', org_uuid=org.get_uuid(), role='admin')
    # EDIT Password
    else:
        ail_users.edit_user('admin@admin.test', user_id, password=password, chg_passwd=True)

    token = ail_users.get_default_admin_token()

    default_passwd_file = os.path.join(os.environ['AIL_HOME'], 'DEFAULT_PASSWORD')
    to_write_str = '# Password Generated by default\n# This file is deleted after the first login\n#\nemail=admin@admin.test\npassword='
    to_write_str = f'{to_write_str}{password}\nAPI_Key={token}\n'
    with open(default_passwd_file, 'w') as f:
        f.write(to_write_str)

    print(f'new user created: {user_id}')
    print(f'password: {password}')
    print(f'token: {token}')
