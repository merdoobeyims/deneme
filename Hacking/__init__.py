# Ne olmasını bekliyordun ki :) 
import logging 

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

app = Client("Timed", api_hash=API_HASH, api_id=API_ID, session_name=SESSION_NAME)
