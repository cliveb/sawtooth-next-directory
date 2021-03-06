# Copyright 2018 Contributors to Hyperledger Sawtooth
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

import logging
import pytest

from rbac.common import addresser
from rbac.common.addresser.task import TaskAddress
from rbac.common.addresser.task import TaskAdminAddress
from tests.rbac.common.addresser.address_assertions import AddressAssertions

LOGGER = logging.getLogger(__name__)


@pytest.mark.addressing
@pytest.mark.unit
class TestTaskAdminAddresser(AddressAssertions):
    def test_import(self):
        self.assertIsInstance(addresser.task, TaskAddress)
        self.assertIsInstance(addresser.task.admin, TaskAdminAddress)
        self.assertIsAddressClass(addresser.task.admin)

    def test_address(self):
        task_id = addresser.task.admin.unique_id()
        user_id = addresser.user.unique_id()
        rel_address = addresser.task.admin.address(object_id=task_id, target_id=user_id)
        self.assertIsAddress(rel_address)
        self.assertEqual(
            addresser.address_is(rel_address), addresser.AddressSpace.TASKS_ADMINS
        )

    def test_address_deterministic(self):
        task_id = addresser.task.admin.unique_id()
        user_id = addresser.user.unique_id()
        rel_address1 = addresser.task.admin.address(
            object_id=task_id, target_id=user_id
        )
        rel_address2 = addresser.task.admin.address(
            object_id=task_id, target_id=user_id
        )
        self.assertIsAddress(rel_address1)
        self.assertIsAddress(rel_address2)
        self.assertEqual(rel_address1, rel_address2)
        self.assertEqual(
            addresser.address_is(rel_address1), addresser.AddressSpace.TASKS_ADMINS
        )

    @pytest.mark.skip("hash collision on legacy addressing scheme can cause match")
    def test_address_random(self):
        task_id1 = addresser.task.admin.unique_id()
        user_id1 = addresser.user.unique_id()
        task_id2 = addresser.task.admin.unique_id()
        user_id2 = addresser.user.unique_id()
        rel_address1 = addresser.task.admin.address(
            object_id=task_id1, target_id=user_id1
        )
        rel_address2 = addresser.task.admin.address(
            object_id=task_id2, target_id=user_id2
        )
        self.assertIsAddress(rel_address1)
        self.assertIsAddress(rel_address2)
        self.assertNotEqual(rel_address1, rel_address2)
        self.assertEqual(
            addresser.address_is(rel_address1), addresser.AddressSpace.TASKS_ADMINS
        )
        self.assertEqual(
            addresser.address_is(rel_address2), addresser.AddressSpace.TASKS_ADMINS
        )

    def test_address_static(self):
        task_id = "99968acb8f1a48b3a4bc21e2cd252e67"
        user_id = "966ab67317234df489adb4bc1f517b88"
        expected_address = "9f44481e326a1713a905b26359fc8d\
a2817c1a5f67de6f464701f0c10042da345d2848"
        rel_address = addresser.task.admin.address(object_id=task_id, target_id=user_id)
        self.assertIsAddress(rel_address)
        self.assertEqual(rel_address, expected_address)
        self.assertEqual(
            addresser.address_is(rel_address), addresser.AddressSpace.TASKS_ADMINS
        )
