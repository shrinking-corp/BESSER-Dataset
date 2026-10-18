# Self-test of the duplicate detector and the PUML verifier

Generated: 2026-10-18T20:34:57.700552+00:00 · sample 332 models, seed 42

**Verdict: PASS** (fingerprint fooled 0×, verifier fooled 0×, verifier false alarms 0, bad test cases 0, groupings identical: True)

Never exercised: none. Models added for rare constructs: 32.

## 1. Fingerprint: real changes must change it, noise must not

`ok` = behaved correctly · `FINGERPRINT_FOOLED` = failed · `bad_test_case` = besser says the operation didn't do what it claims (not counted either way) · `invalid_model` = the mutated file no longer loads.

| Operation | Outcomes |
|---|---|
| change attribute type | invalid_model: 1, ok: 330 |
| change model's random name | ok: 332 |
| change multiplicity | ok: 302 |
| edit OCL expression | ok: 31 |
| edit description | ok: 332 |
| edit project name | ok: 332 |
| edit project owner | ok: 332 |
| flip abstract | ok: 332 |
| flip composite | invalid_model: 51, ok: 251 |
| flip navigable | ok: 302 |
| reformat / drop comments | ok: 332 |
| remove association | ok: 296 |
| remove attribute | ok: 331 |
| remove generalization | ok: 167 |
| remove type | ok: 327 |
| rename association | ok: 302 |
| rename attribute/role | ok: 332 |
| rename class | ok: 332 |
| rename enum literal | ok: 84 |
| rename enumeration | ok: 112 |
| rename method | ok: 46 |
| rename parameter | ok: 34 |
| reorder independent statements | ok: 332 |
| shuffle set items | ok: 329 |

## 2. Verifier: corrupted PUML must be reported, the real PUML must pass

| Corruption | Outcomes |
|---|---|
| add bogus class | ok: 332 |
| change attribute type | ok: 331 |
| change model name | ok: 332 |
| change multiplicity | ok: 302 |
| change parameter | ok: 34 |
| change role name | ok: 302 |
| delete association | ok: 302 |
| delete attribute | ok: 331 |
| delete constraint | ok: 31 |
| delete enum literal | ok: 84 |
| delete generalization | ok: 175 |
| delete method | ok: 46 |
| delete project header | ok: 332 |
| drop {not navigable} | ok: 1 |
| flip abstract | ok: 332 |
| flip composition | ok: 302 |
| unmodified PUML | ok: 332 |

## 3. Independent grouping (besser-built model vs. AST fingerprint)

- Models: 8336 (errors: 0)
- Groups by fingerprint: 5264 · by besser-built model: 5264
- Fingerprint merged models besser builds differently: 0
- Fingerprint split models besser builds identically: 0

Full detail: see the accompanying `.json`.
