import pytest
from starlette.testclient import TestClient


@pytest.mark.v1
@pytest.mark.wallet
class TestWallerRoute:
    def test_create_wallet(
            self,
            wallet_dict: dict,
            client: TestClient
    ):
        result = client.post('/api/v1/wallet')
        wallet_dict.update(result.json())
        assert True

    def test_get_wallet(
            self,
            wallet_dict: dict,
            client: TestClient
    ):
        wallet_id = wallet_dict['wallet_id']
        response = client.get(f"/api/v1/wallet/{wallet_id}")
        assert response.status_code == 200

    def test_deposit_wallet(
            self,
            wallet_dict: dict,
            client: TestClient
    ):
        wallet_id = wallet_dict['wallet_id']
        wallet_balance = wallet_dict['wallet_balance']
        amount_deposit: float = 1000.0
        body_json = {
            'amount': amount_deposit,
            'operation_type': 'DEPOSIT'
        }
        response = client.post(f"/api/v1/wallet/{wallet_id}/operations", json=body_json)
        if response.status_code != 200:
            assert False
        response_wallet = client.get(f"/api/v1/wallet/{wallet_id}")
        response_wallet_json = response_wallet.json()
        if response_wallet.status_code != 200:
            assert False
        result_test = (wallet_balance + amount_deposit) == response_wallet_json['wallet_balance']
        if not result_test:
            assert False
        wallet_dict['wallet_balance'] = response_wallet_json['wallet_balance']
        assert True

    def test_withdraw_wallet(
            self,
            wallet_dict: dict,
            client: TestClient
    ):
        wallet_id = wallet_dict['wallet_id']
        wallet_balance = wallet_dict['wallet_balance']
        amount_deposit: float = 1000.0
        body_json = {
            'amount': amount_deposit,
            'operation_type': 'WITHDRAW'
        }
        response = client.post(f"/api/v1/wallet/{wallet_id}/operations", json=body_json)
        if response.status_code != 200:
            assert False
        response_wallet = client.get(f"/api/v1/wallet/{wallet_id}")
        response_wallet_json = response_wallet.json()
        if response_wallet.status_code != 200:
            assert False
        result_test = (wallet_balance - amount_deposit) == response_wallet_json['wallet_balance']
        if not result_test:
            assert False
        wallet_dict['wallet_balance'] = response_wallet_json['wallet_balance']
        assert True

    def test_wallet_operations(
            self,
            wallet_dict: dict,
            client: TestClient
    ):
        wallet_id = wallet_dict['wallet_id']
        response = client.get(f"/api/v1/wallet/{wallet_id}/operations")
        if response.status_code != 200:
            assert False
        response_json = response.json()
        assert len(response_json) == 2
