import torch
import torch.nn as nn


weight = [0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, 0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, 0.70, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, 0.52, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00, 0.28, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.90, -0.70, -0.52, -0.28, 0.00]
bias = [65.45, 64.86, 64.15, 63.35, 62.45, 61.55, 60.65, 59.75, 58.85, 57.95, 57.05, 56.15, 55.25, 54.35, 53.45, 52.55, 51.65, 50.75, 49.85, 48.95, 48.05, 47.15, 46.25, 45.35, 44.45, 43.55, 42.65, 41.75, 40.85, 39.95, 39.05, 38.15, 37.25, 36.35, 35.45, 34.55, 33.65, 32.75, 31.85, 30.95, 30.05, 29.15, 28.25, 27.35, 26.45, 25.55, 24.65, 23.75, 22.85, 21.95, 21.05, 20.15, 19.25, 18.35, 17.45, 16.55, 15.65, 14.75, 13.85, 12.95, 12.05, 11.15, 10.25, 9.35, 8.45, 7.55, 6.65, 5.85, 5.14, 4.55]


ts_weight = torch.Tensor(weight).float().view(70, 70)
ts_bias = torch.Tensor(bias).float().view(70)

layer = nn.Linear(70, 70, bias = True)
layer.weight.data = ts_weight
layer.bias.data = ts_bias