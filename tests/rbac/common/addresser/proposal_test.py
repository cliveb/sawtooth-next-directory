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
from rbac.common.addresser.proposal import ProposalAddress
from tests.rbac.common.addresser.address_assertions import AddressAssertions

LOGGER = logging.getLogger(__name__)


@pytest.mark.addressing
@pytest.mark.unit
class TestProposalAddresser(AddressAssertions):
    def test_import(self):
        self.assertIsInstance(addresser.proposal, ProposalAddress)
        self.assertIsAddressClass(addresser.proposal)

    def test_address(self):
        object_id = addresser.proposal.unique_id()
        target_id = addresser.proposal.unique_id()
        proposal_address = addresser.proposal.address(
            object_id=object_id, target_id=target_id
        )
        self.assertIsAddress(proposal_address)
        self.assertEqual(
            addresser.address_is(proposal_address), addresser.AddressSpace.PROPOSALS
        )

    def test_address_deterministic(self):
        object_id = addresser.proposal.unique_id()
        target_id = addresser.proposal.unique_id()
        proposal_address1 = addresser.proposal.address(
            object_id=object_id, target_id=target_id
        )
        proposal_address2 = addresser.proposal.address(
            object_id=object_id, target_id=target_id
        )
        self.assertIsAddress(proposal_address1)
        self.assertIsAddress(proposal_address2)
        self.assertEqual(proposal_address1, proposal_address2)
        self.assertEqual(
            addresser.address_is(proposal_address1), addresser.AddressSpace.PROPOSALS
        )

    def test_address_random(self):
        object_id1 = addresser.proposal.unique_id()
        target_id1 = addresser.proposal.unique_id()
        object_id2 = addresser.proposal.unique_id()
        target_id2 = addresser.proposal.unique_id()
        proposal_address1 = addresser.proposal.address(
            object_id=object_id1, target_id=target_id1
        )
        proposal_address2 = addresser.proposal.address(
            object_id=object_id2, target_id=target_id2
        )
        self.assertIsAddress(proposal_address1)
        self.assertIsAddress(proposal_address2)
        self.assertNotEqual(proposal_address1, proposal_address2)
        self.assertEqual(
            addresser.address_is(proposal_address1), addresser.AddressSpace.PROPOSALS
        )
        self.assertEqual(
            addresser.address_is(proposal_address2), addresser.AddressSpace.PROPOSALS
        )

    def test_address_static(self):
        object_id = "cb048d507eec42a5845e20eed982d5d2"
        target_id = "f1e916b663164211a9ac34516324681a"
        expected_address = "9f4448e3b874e90b2bcf58e65e0727\
91ea499543ee52fc9d0449fc1e41f77d4d4f926e"
        proposal_address = addresser.proposal.address(
            object_id=object_id, target_id=target_id
        )
        self.assertIsAddress(proposal_address)
        self.assertEqual(proposal_address, expected_address)
        self.assertEqual(
            addresser.address_is(proposal_address), addresser.AddressSpace.PROPOSALS
        )
