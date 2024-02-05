from petals.constants import PUBLIC_INITIAL_PEERS

from data_structures import ModelInfo

INITIAL_PEERS = INITIAL_PEERS = ['/ip4/45.79.153.218/tcp/31337/p2p/QmXfANcrDYnt5LTXKwtBP5nsTMLQdgxJHbK3L1hZdFN8km',]

MODELS = [

    ModelInfo(
        dht_prefix="StableBeluga2-hf",
        repository="https://huggingface.co/petals-team/StableBeluga2",
        num_blocks=80,
        ),
        
     ModelInfo(
        dht_prefix="deepseek-coder-33b-instruct",
        repository="https://huggingface.co/deepseek-ai/deepseek-coder-33b-instruct",
        num_blocks=80,
        ),
]

UPDATE_PERIOD = 5
