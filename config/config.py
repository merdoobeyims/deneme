import os 
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("session_name", "AQHFv60AKe827yNmjHb5EIRoM4zUImFd9X-ldQNFc18YdKl5NVpSUWZ24pKeQvc6tX2KXath_s47r7-BQPz12o6wAmlbzGR_YK8odpnz70PGeo5OdBfeneGD8uV-K653ZxrD3O5QbHolQ-1AJQ0Tuo-dTjbEI7AEEoTVtJBGZakJtoV6flN-2BswCc65lVst3JCNMRuhjyTXUK96NRua9svQufe_0WIXAhBFdaMyE82mXFr_t7OokuEz7Vu-1ZG17LClBx_WB7v0QfgHnAtWV0LSRrJ8doEzweDgXuSKZkbn8GkB8zXjen289M6k9jOneg8JK_Vl6VuS_m-03n42IPEvvakRVQAAAAGO8SGEAA")
API_ID = int(getenv("api_id", "29736877"))
API_HASH = getenv("api_hash", "6238bdbf7f4a191a71e7e768dcfccc97")
CHANNEL_ID = getenv("channel_id", "-1002350735231")
last_messages_amount = 90
