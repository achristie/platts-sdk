# Platts Python SDK

Consuming the Platts API in Python

## Installation

`pip install platts-sdk`

## Getting Started

```python
import platts_sdk as platts

tc = platts.TokenClient("username", "password", "apikey")
mdd = platts.MarketData(tc)

sym = ["PCAAS00", "PCAAT00"]
cur_df = mdd.get_current_assessments(sym)
print(cur_df)

mdc = "ET"
mdc_df = mdd.get_current_assessments_by_mdc(mdc)
print(mdc_df)
```
