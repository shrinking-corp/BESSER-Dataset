# Test Suite Validation Report

Generated: 2026-09-01T15:30:26.762845+00:00

- **Total models checked:** 9082
- **Models with fully passing test suite:** 8027
- **Models with a failing/broken test suite:** 1055
- **Model pass rate:** 88.38%

- **Total individual tests collected:** 1298863
- **Total individual tests passed:** 1285708
- **Total individual tests failed:** 13079
- **Total individual tests errored:** 76

## Breakdown by status

| Status | Count |
|---|---|
| pass | 8027 |
| test_failures | 961 |
| collection_error | 76 |
| timeout | 16 |
| missing_file | 1 |
| no_tests_collected | 1 |

## Failing models by error type

| Error type | Count |
|---|---|
| AssertionError | 919 |
| SyntaxError | 64 |
| TypeError | 27 |
| TimeoutExpired | 16 |
| hypothesis.errors.FailedHealthCheck | 12 |
| IndentationError | 6 |
| NameError | 5 |
| ImportError | 2 |
| hypothesis.errors.InvalidArgument | 1 |
| AttributeError | 1 |

Full per-model detail: see `test_validation_report.json` and each model's `code_metadata.json`.
