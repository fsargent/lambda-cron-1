# Copyright (C) 2016 MediaMath <http://www.mediamath.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os


def resources_directory_path():
    return os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources'))


def valid_cong_file_path():
    return os.path.join(resources_directory_path(), 'config.yml')


def valid_cong_file_path_only_prod_env():
    return os.path.join(resources_directory_path(), 'config_only_prod.yml')


def invalid_config_file_path():
    return '/tmp/no_existing_config.yml'


def get_test_task_path(task_file_name):
    return os.path.join(resources_directory_path(), 'tasks', task_file_name)
