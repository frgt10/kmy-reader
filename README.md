# kmy-reader

A small Python package for reading [KMyMoney](https://kmymoney.org/) data files (`.kmy`).

## Requirements

- Python 3.9+

## Installation

From source:

```bash
git clone https://github.com/frgt10/kmy-reader.git
cd kmy-reader
pip install -e .
```

For development (includes test dependencies):

```bash
pip install -e ".[dev]"
pytest
```

## Usage

```python
from kmy import Kmy

mm = Kmy.from_kmy_file("/path/to/your-money.kmy")
```

Both compressed and uncompressed `.kmy` files are supported — gzip is detected
automatically.

Then use the parsed data as you wish:

```python
print("User:", mm.user.name, mm.user.email)
print("File info:", mm.fileInfo.creationDate, mm.fileInfo.lastModifiedDate)

print("Institutions:", len(mm.institutions))
print("Accounts:", len(mm.accounts))
print("Transactions:", len(mm.transactions))
print("Tags:", len(mm.tags))
print("Payees:", len(mm.payees))
print("Cost centers:", len(mm.costCenters))
print("Price pairs:", len(mm.pricePairs))
print("Securities:", len(mm.securities))
```

### Transactions and splits

```python
for transaction in mm.transactions:
    print(transaction.postDate, transaction.commodity, transaction.memo)
    for split in transaction.splits:
        print("  ", split.account, split.value, split.reconcileDate)
```

### Data types

- **Amounts** (`Split.shares`, `Split.price`, `Split.value`, `Price.price`,
  `Security.onlineFactor`) are `decimal.Decimal`. KMyMoney stores them as
  rational strings such as `"12345/100"`, which are converted exactly.
- **Dates** (`Transaction.postDate`, `Transaction.entryDate`,
  `Account.lastModified`, `Account.opened`, `Account.lastReconciled`,
  `Split.reconcileDate`, `Price.date`, `FileInfo.creationDate`,
  `FileInfo.lastModifiedDate`) are `datetime.date`, or `None` when the value is
  empty.
- **Strings** default to `""` when the corresponding attribute is missing.

All model classes are frozen dataclasses, so parsed objects are immutable and
hashable.

## Model overview

`Kmy` exposes the following attributes:

| Attribute | Content |
| --- | --- |
| `fileInfo` | `FileInfo` |
| `user` | `User` |
| `institutions` | `list[Institution]` |
| `payees` | `list[Payee]` |
| `costCenters` | `list[CostCenter]` |
| `tags` | `list[Tag]` |
| `accounts` | `list[Account]` |
| `transactions` | `list[Transaction]` |
| `pricePairs` | `list[Pricepair]` |
| `securities` | `list[Security]` |
| `keyValuePairs` | `dict[str, str]` |

Schedules, budgets, reports, currencies and online jobs are not parsed yet.

## Contributing

Issues and pull requests are welcome:
<https://github.com/frgt10/kmy-reader/issues>

## License

MIT — see [LICENSE](LICENSE).
