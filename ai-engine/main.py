from fastapi import FastAPI
import requests

app = FastAPI()

# ✅ Correct URLs (FIXED reward-service version issue)
USER_URL = "https://ee109b02-dea5-436d-a8b8-e17df34b50b3-dev.e1-us-east-azure.choreoapis.dev/ai-api-orchestrator/user-service/v1.0/user"
REWARD_URL = "https://ee109b02-dea5-436d-a8b8-e17df34b50b3-dev.e1-us-east-azure.choreoapis.dev/ai-api-orchestrator/reward-service/v1.0/reward"

# 🔑 Use DIFFERENT keys
USER_HEADERS = {
    "Test-Key": "eyJraWQiOiJnYXRld2F5X2NlcnRpZmljYXRlX2FsaWFzIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJhMGQyOGJkYi04NTZkLTRlODktODcwOS03OTVjNGJmOTI5N2VAY2FyYm9uLnN1cGVyIiwiYXVkIjoiY2hvcmVvOmRlcGxveW1lbnQ6c2FuZGJveCIsIm9yZ2FuaXphdGlvbiI6eyJ1dWlkIjoiZWUxMDliMDItZGVhNS00MzZkLWE4YjgtZTE3ZGYzNGI1MGIzIn0sImlzcyI6Imh0dHBzOlwvXC9zdHMuY2hvcmVvLmRldjo0NDNcL2FwaVwvYW1cL3B1Ymxpc2hlclwvdjJcL2FwaXNcL2ludGVybmFsLWtleSIsImtleXR5cGUiOiJTQU5EQk9YIiwic3Vic2NyaWJlZEFQSXMiOlt7InN1YnNjcmliZXJUZW5hbnREb21haW4iOm51bGwsIm5hbWUiOiJ1c2VyLXNlcnZpY2UgLSBkZWZhdWx0LWVuZHBvaW50IiwiY29udGV4dCI6IlwvZWUxMDliMDItZGVhNS00MzZkLWE4YjgtZTE3ZGYzNGI1MGIzXC9haS1hcGktb3JjaGVzdHJhdG9yXC91c2VyLXNlcnZpY2VcL3YxLjAiLCJwdWJsaXNoZXIiOiJjaG9yZW9fcHJvZF9hcGltX2FkbWluIiwidmVyc2lvbiI6InYxLjAiLCJzdWJzY3JpcHRpb25UaWVyIjpudWxsfV0sImV4cCI6MTc3MzgyOTc4OCwidG9rZW5fdHlwZSI6IkludGVybmFsS2V5IiwiaWF0IjoxNzczODI5MTg4LCJqdGkiOiIyYWM2MGJkNi05M2ZjLTQ4ZDQtYjU1NC1jMjc4ZWFjNWQ1MWIifQ.aA5emMp28ZeIupkpTA3NrMOun96odx5Jlb-IIyH62a1CK2MI9nO81RMPpt6Iy24pLbCTkhdB6r2EOdsdjJ9YYzC6kJ8PHQGl0AanS5YKumasqk7BOiWi4bJY4MDsHr7ia12PG0ROXZTA0U6luseZofwnJM4j8LkboAa8XQdOZC68EFNTt5cRrS1TF7EqePBUKBcUG4Xt4u-0BlY2U3rQIizLGk3BBNcoLN5qLPeDhmGsQAFyiZt6gxsDA4vqmaUbR2OhcPg0klVSTL4E4woENBch3YDySxerTEq2ExNPXd7gOwZ6lIEXCQZBbiZFCeItuIrBMn-9vz3sTL6aej4KcImOAaskYxKJXLzMEvdQ1VIKPEAu8fmbduRQUPq0WvR1WEVNv6GzS7qEN7QL2JXta62bteVeOH_TQuJ4iMjB2Aqnaj6L0a5yu5c9viGCWCHp60MyizBwA0yoYIeTuAt18TxnV-ijV1ApEBhmgKWaaodElwm5n5D3Mn-XCQs7rSncQecsm1X-OyLBvS5GhzgJA_c62oe0qp8eZ3ZXYGQ9tixUbhRpnKZI_fZmm1rEGPIceshWenrzhQFDs5Qk0b1Mv8VuBx5heFequ9ggyQSZoR-dXzmr3hSltMsMFTnxKeXEo-sbeRbfGo30_OMChFYLxFNwSkmPLDWLsbhqKkKLuwE"
}

REWARD_HEADERS = {
    "Test-Key": "eyJraWQiOiJnYXRld2F5X2NlcnRpZmljYXRlX2FsaWFzIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJhMGQyOGJkYi04NTZkLTRlODktODcwOS03OTVjNGJmOTI5N2VAY2FyYm9uLnN1cGVyIiwiYXVkIjoiY2hvcmVvOmRlcGxveW1lbnQ6c2FuZGJveCIsIm9yZ2FuaXphdGlvbiI6eyJ1dWlkIjoiZWUxMDliMDItZGVhNS00MzZkLWE4YjgtZTE3ZGYzNGI1MGIzIn0sImlzcyI6Imh0dHBzOlwvXC9zdHMuY2hvcmVvLmRldjo0NDNcL2FwaVwvYW1cL3B1Ymxpc2hlclwvdjJcL2FwaXNcL2ludGVybmFsLWtleSIsImtleXR5cGUiOiJTQU5EQk9YIiwic3Vic2NyaWJlZEFQSXMiOlt7InN1YnNjcmliZXJUZW5hbnREb21haW4iOm51bGwsIm5hbWUiOiJyZXdhcmQtc2VydmljZSAtIGRlZmF1bHQtZW5kcG9pbnQiLCJjb250ZXh0IjoiXC9lZTEwOWIwMi1kZWE1LTQzNmQtYThiOC1lMTdkZjM0YjUwYjNcL2FpLWFwaS1vcmNoZXN0cmF0b3JcL3Jld2FyZC1zZXJ2aWNlXC92MS4wIiwicHVibGlzaGVyIjoiY2hvcmVvX3Byb2RfYXBpbV9hZG1pbiIsInZlcnNpb24iOiJ2MS4wIiwic3Vic2NyaXB0aW9uVGllciI6bnVsbH1dLCJleHAiOjE3NzM4Mjk3NTYsInRva2VuX3R5cGUiOiJJbnRlcm5hbEtleSIsImlhdCI6MTc3MzgyOTE1NiwianRpIjoiOTQ4OTkyOWMtOTU3MC00MjdhLTlmNzctMjdlYjhiYzMyN2YxIn0.FFI8snZ2GY1V3ZbHyycRwtVJ4rX0i-jeVc6qm9ClhM8m4Tp1a36GMTem5RmEizkEuWRc5WRXtb48H6cRX5No3v-YDKLtWSaxAMZFJO42ymuPJ3_K5rBApyBPnWAICITqR-kKZI2o8rThFCiPL6f2mPnJu85NsUiRAgIJ82kZeRx3YxpJ7BWXeHtPHT_UHDZpm4Ep8ZG0pdsg_dBuX3ShJfcFAooTBZ8HH4Kv8EQbBMrWlmXJtsG_0jN47DpirVFcEhZVtabn2g4n0hpMVZ2l5fX_yq7modW8PNlwbcoYQcT4TEtcJrtkt4kslgfG66U6kbEEW0RxtyuxYMSoiSdeEp4_BqhTT4NuaVHMZuZHrrSvfX_VuLFAMzt-q6HTZSfvpmKDIOHxQ1Zf9jj8hwHrAQWMg9c04FgRD7f7JZTHB2O8irnuT6iT5u3jNGlThfYi_QIsnbNgK8lSUVu5dZWJNvLLxy8a-uijUaB7z6hWE5xJ5gJAmKwL1JUGQVM6Y7Vn0xfYLQq5YXdpZwuKaBg17b_jKiRg6qeKe3gc5sY62ft3BsNSGQvv3edC31w0frvL3DnKRB5l3YZYD5_NCh-DL6LHZpwDus8QddtESDom8QQM_Ci4dNfSM0ll3bO6m6zNri8rkPXqqrigifcnvpyEZ7kB8h6oW_U2pY90sROh_fw"
}


@app.get("/analyze")
def analyze():
    try:
        # 🔹 Call user-service
        user_response = requests.get(USER_URL, headers=USER_HEADERS)
        print("USER STATUS:", user_response.status_code, user_response.text)

        # 🔹 Call reward-service
        reward_response = requests.get(REWARD_URL, headers=REWARD_HEADERS)
        print("REWARD STATUS:", reward_response.status_code, reward_response.text)

        # 🔹 Safe JSON parsing
        try:
            user_data = user_response.json()
        except:
            user_data = {"error": user_response.text}

        try:
            reward_data = reward_response.json()
        except:
            reward_data = {"error": reward_response.text}

        return {
            "user": user_data,
            "reward": reward_data,
            "decision": "User is eligible for reward"
        }

    except Exception as e:
        return {
            "error": str(e)
        }