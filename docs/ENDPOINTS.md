[Back to README](../README.md)

# API Endpoints

## Service Status

| Endpoint | Method | Path | Docs |
| --- | --- | --- | --- |
| ping (AWS API Gateway) | GET | `/ping` | [link](https://developer.japer.io#9f421994-c448-4664-a58a-4199751e9eee) |
| ping (AWS Lambda) | GET | `/v1/ping` | [link](https://developer.japer.io#13bc6fb4-082e-43a1-8851-44b5328491fd) |
| ping (JAPER Nexus) | GET | `/v1/x/nexus/status` | [link](https://developer.japer.io#13312f90-f840-45ac-941b-a9d399b424c5) |

## Device Management

| Endpoint | Method | Path | Docs |
| --- | --- | --- | --- |
| device/create | PUT | `/v1/x/device/create` | [link](https://developer.japer.io#602b2071-0c16-4884-841a-54b170f10934) |
| device/status | GET | `/v1/x/device/status` | [link](https://developer.japer.io#ff2a70b3-25a4-45a0-8b48-d7db6aa762af) |
| device/purge | DELETE | `/v1/x/device/purge` | [link](https://developer.japer.io#0284f306-b48f-4c4f-b22d-a501cb8294bf) |
| device/kill | DELETE | `/v1/x/device/kill` | [link](https://developer.japer.io#3b1eebef-ba40-4236-986d-b22f8f8ee804) |

## Customer Validation

| Endpoint | Method | Path | Docs |
| --- | --- | --- | --- |
| validation/attempt | PUT | `/v1/x/validate/attempt` | [link](https://developer.japer.io#1bd10f4b-10bc-4471-a2bb-a59fcbe2d657) |
| validate/domain | PUT | `/v1/x/validate/domain` | [link](https://developer.japer.io#32170320-6356-4b8b-aee2-3f8710f1f23e) |
| validate/email | GET | `/v1/x/validate/device/email` | [link](https://developer.japer.io#0deccebe-ff46-4113-8101-50842780f3ee) |
| validate/sms | GET | `/v1/x/validate/device/sms` | [link](https://developer.japer.io#16fa7e5f-251d-43c3-ae3e-ab5a80a6aadd) |
| validation/status | GET | `/v1/x/validation/status` | [link](https://developer.japer.io#8fed7e8d-5fbd-4613-ae97-246df653c115) |

## Data Encryption

| Endpoint | Method | Path | Docs |
| --- | --- | --- | --- |
| encrypt | POST | `/v1/x/encrypt` | [link](https://developer.japer.io#bd5a0746-7e44-444b-bafc-e092762fb577) |

## Data Decryption

| Endpoint | Method | Path | Docs |
| --- | --- | --- | --- |
| decrypt | POST | `/v1/x/decrypt` | [link](https://developer.japer.io#218739dc-adcf-4111-98bf-a6b850a90e4b) |
| lookup | POST | `/v1/x/lookup` | [link](https://developer.japer.io#e38e344b-ca93-41a9-992c-5647dcb78fbd) |
| execute | POST | `/v1/x/execute` | [link](https://developer.japer.io#f8f0f1d2-f8c9-4284-b641-b680ce64cfd4) |

