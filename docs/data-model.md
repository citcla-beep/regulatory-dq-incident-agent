# Data model

This document defines the synthetic dataset produced by the generator: two
tables and a closed catalogue of data quality errors that are injected on
purpose.

The model is inspired by publicly available EU rules on the reporting of
cross-border payments. Field names and structure are original to this project
and do not reproduce any official or proprietary record layout.

## Scope

The dataset represents payments collected by payment service providers during
one calendar quarter. Downstream, payments are aggregated by payee and quarter
to identify payees that receive more than 25 cross-border payments in the
period.

A payment is cross-border when `payer_country` differs from the payee's
`payee_country`. This flag is not stored: it is derived in the transformation
layer.

## Payees

One row per payee.

| Field | Type | Required | Rule |
|---|---|---|---|
| payee_id | string | yes | unique, format `PAYEE-` followed by 6 digits |
| payee_name | string | yes | not empty |
| payee_country | string | yes | ISO 3166-1 alpha-2 country code |
| payee_account | string | yes | unique, IBAN-like identifier |

## Payments

One row per payment.

| Field | Type | Required | Rule |
|---|---|---|---|
| payment_id | string | yes | unique, format `PAY-` followed by 9 digits |
| payment_timestamp | timestamp (UTC) | yes | within the reporting quarter |
| amount | decimal(18,2) | yes | greater than zero |
| currency | string | yes | ISO 4217 code from the accepted list |
| payer_country | string | yes | ISO 3166-1 alpha-2 code of an EU member state |
| payee_id | string | yes | must exist in `payees` |
| payment_method | string | yes | one of `card`, `credit_transfer`, `direct_debit`, `e_money` |
| psp_id | string | yes | identifier of the reporting payment service provider |
| is_refund | boolean | yes | `true` or `false` |

## Error catalogue

Errors are injected only into `payments`. Each corrupted record carries exactly
one error, so that detection can be measured per error type.

| Error id | What is altered | Field | Detected by |
|---|---|---|---|
| E01_MISSING_PAYER_COUNTRY | value replaced with null | payer_country | not-null check |
| E02_INVALID_CURRENCY | value replaced with a code outside the accepted list | currency | accepted-values check |
| E03_NON_POSITIVE_AMOUNT | value replaced with zero or a negative number | amount | range check |
| E04_ORPHAN_PAYEE | value replaced with an id that is not in `payees` | payee_id | relationship check |
| E05_DUPLICATE_PAYMENT | the whole row is written twice | payment_id | uniqueness check |
| E06_TIMESTAMP_OUT_OF_PERIOD | value moved outside the reporting quarter | payment_timestamp | period range check |

## Ground truth

Every injected error is logged in a separate file, one row per corrupted
record.

| Field | Type | Description |
|---|---|---|
| payment_id | string | identifier of the corrupted payment |
| error_id | string | identifier from the error catalogue |
| field | string | name of the altered field |
| original_value | string | value before the injection, empty for duplicates |
| injected_value | string | value after the injection, empty for duplicates |

The ground truth is used only for evaluation. It is never loaded into the
transformation layer as an input to the checks.