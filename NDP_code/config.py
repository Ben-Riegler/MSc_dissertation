from dataclasses import dataclass



@dataclass
class DiffusionConfig:
    schedule: str = "cosine"
    beta_start: float = 3e-4
    beta_end: float = 0.5
    timesteps: int = 600


@dataclass
class OptimizerConfig:
    num_warmup_epochs: int = 20
    num_decay_epochs: int = 200
    init_lr: float = 2e-5
    peak_lr: float = 1e-3
    end_lr: float = 1e-5
    ema_rate: float = 0.995  # 0.999


@dataclass
class NetworkConfig:
    n_layers: int = 4
    hidden_dim: int = 64
    num_heads: int = 8
    sparse_attention: bool = False


@dataclass
class EvalConfig:
    batch_size: int = 4
    num_samples: int = 128
    float64: bool = False



@dataclass
class Config:
    seed: int = 42
    dataset: str = "swirl"
    input_dim: int = 2
    output_dim: int = 2
    batch_size: int = 32 # 32
    num_epochs: int = 250
    samples_per_epoch: int = int(2**14)
    loss_type: str = "l1"
    
    eval: EvalConfig = EvalConfig()
    network: NetworkConfig = NetworkConfig()
    schedule: DiffusionConfig = DiffusionConfig()
    diffusion: DiffusionConfig = DiffusionConfig()
    optimizer: OptimizerConfig = OptimizerConfig()

    restore: str = ""

    @property
    def steps_per_epoch(self) -> int:
        return self.samples_per_epoch // self.batch_size

    @property
    def total_steps(self) -> int:
        return self.steps_per_epoch * self.num_epochs


