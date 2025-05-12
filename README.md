## What is the goal?
Attempt at making both `pytest-playwright`  and `pytest-playwright-asyncio` cooperate.

## How to
Couple of steps:
- disable de plugins globally through `pyetst.ini`
- define separete sync and async tests folders
- import the relevant fixtures at each folder's `conftest.py`
- delete `pytest_addoption` on both lower level `conftest.py`
- enable `pytest_addopton` on a higher level `conftest.py`

## Test
Run:
```shell
pytest
```
