import requests
import pytest


class TestCoinDeskAPI:
    COINDESK_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    def test_coindesk_api_response(self):
        """
        Test CoinDesk API response

        Verifies:
        1. Successful API call
        2. Presence of 3 BPIs (USD, GBP, EUR)
        3. GBP description
        """
        # Send GET request
        response = requests.get(self.COINDESK_URL)

        # Verify successful response
        assert response.status_code == 200, "API call failed"

        # Parse JSON response
        data = response.json()

        # Verify BPIs
        bpi = data.get('bpi', {})
        assert len(bpi) == 3, "Expected 3 BPIs"

        # Verify specific BPI keys exist
        expected_bpi_keys = ['USD', 'GBP', 'EUR']
        for key in expected_bpi_keys:
            assert key in bpi, f"{key} BPI missing"

        # Verify GBP description
        gbp_description = bpi['GBP'].get('description')
        assert gbp_description == 'British Pound Sterling', \
            "GBP description does not match expected"