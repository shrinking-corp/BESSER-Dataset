# Unique models (one per distinct BUML model)

Generated: 2026-10-18T19:24:53.111622+00:00

- **Input:** `S:\.school\Magister\shrinking\code\Dataset\BESSER-Dataset\BESSER-Dataset\reports\usable_models.txt`, 8336 models
- **Kept:** 5264 models
- **Removed as copies:** 3072 models in 1018 groups
- **Kept without comparison** (no BUML file / BUML doesn't parse): 0 / 0

Copies are identified from the original BUML sources, ignoring only set-item order, statement order, comments and the model's own random name (see the script's docstring). Statements that never reach the model (overwritten overloaded-method definitions) are dropped first; statement order was still kept for 0 models that assign a variable twice even after that, where order changes the model.

## Step 1: groups found in the BUML

### Group sizes

| Copies of one model | Groups |
|---:|---:|
| 2 | 740 |
| 3 | 128 |
| 4 | 55 |
| 5 | 28 |
| 6 | 8 |
| 7 | 5 |
| 8 | 5 |
| 9 | 3 |
| 10 | 10 |
| 11 | 2 |
| 12 | 4 |
| 13 | 2 |
| 14 | 2 |
| 15 | 3 |
| 18 | 3 |
| 19 | 1 |
| 20 | 1 |
| 21 | 1 |
| 22 | 1 |
| 24 | 1 |
| 25 | 1 |
| 27 | 3 |
| 29 | 1 |
| 31 | 1 |
| 33 | 1 |
| 41 | 1 |
| 68 | 1 |
| 81 | 1 |
| 158 | 1 |
| 164 | 1 |
| 185 | 1 |
| 191 | 1 |
| 200 | 1 |

### Largest groups

| Representative | Copies | Category |
|---|---:|---|
| model_10000002 | 200 | shopping |
| model_10000012 | 191 | dummy |
| model_10000013 | 185 | computerarchitecture |
| model_10000005 | 164 | restaurant |
| model_10000000 | 158 | shopping |
| model_10000029 | 81 | bank |
| model_10000015 | 68 | school |
| model_10000124 | 41 | computer-json |
| model_10000024 | 33 | health |
| model_10000188 | 31 | shopping |
| model_10000014 | 29 | employee |
| model_10000021 | 27 | employee |
| model_10000121 | 27 | course |
| model_100310 | 27 | database/sql |
| model_10000122 | 25 | smarthouse |
| model_49 | 24 | gpl |
| model_10000007 | 22 | clientsupport |
| model_10000081 | 21 | bank-transactions |
| model_10000001 | 20 | booking-room |
| model_10000027 | 19 | restaurant |

## Step 2: check against the generated PUML

**Agrees.** Distinct by PUML: 5264, by BUML: 5264.

- PUML groups spanning several BUML models (information missing from the PUML): 0
- BUML groups whose PUML differs (PUML generation not deterministic): 0

Every group with all its members: see the accompanying `.json`.
