# eBay and CoinDesk Automation Project

## Project Structure
- `tests/`: Contains test scripts
  - `ui_tests/`: UI automation tests
  - `api_tests/`: API automation tests
- `pages/`: Page Object Model for web pages
- `utils/`: Utility functions and helpers

## Prerequisites
- Python 3.8+
- Chrome Browser

## Setup
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Tests
- UI Tests: `pytest tests/ui_tests/test_ebay_cart.py`
- API Tests: `pytest tests/api_tests/test_coindesk_api.py`

## Test Coverage
- eBay UI Test: Adding a book to cart
- CoinDesk API Test: Verifying price index information