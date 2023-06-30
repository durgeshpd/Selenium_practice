import pytest
import pandas as pd


@pytest.fixture
def data():
    # Load the test data from the Excel file
    test_data = pd.read_excel('test_data.xlsx')
    return test_data


def test_case_1(data):
    # Extract the test case data from the 'TC_001' row
    test_case_data = data.loc[data['Test Case'] == 'TC_001', 'Data'].item()
    print(f"Test Case 1: {test_case_data}")


def test_case_2(data):
    # Extract the test case data from the 'TC_002' row
    test_case_data = data.loc[data['Test Case'] == 'TC_002', 'Data'].item()
    print(f"Test Case 2: {test_case_data}")


def test_case_3(data):
    # Extract the test case data from the 'TC_003' row
    test_case_data = data.loc[data['Test Case'] == 'TC_003', 'Data'].item()
    print(f"Test Case 3: {test_case_data}")
