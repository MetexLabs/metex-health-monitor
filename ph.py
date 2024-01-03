# git clone https://github.com/petals-infra/health.petals.dev
# cd health.petals.dev

from pprint import pprint
import hivemind
from petals.constants import PUBLIC_INITIAL_PEERS
from health import fetch_health_state

dht = hivemind.DHT(initial_peers=PUBLIC_INITIAL_PEERS, client_mode=True, start=True)
pprint(fetch_health_state(dht))