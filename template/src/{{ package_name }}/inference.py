"""Machine learning model inference script."""

import structlog
import torch

logger = structlog.get_logger()


def predict(input_tensor: torch.Tensor) -> torch.Tensor:
    """Run model inference."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info("running_inference", device=device, shape=list(input_tensor.shape))
    tensor_dev = input_tensor.to(device)
    # Sample linear transformation demo
    weights = torch.randn(tensor_dev.shape[-1], 1, device=device)
    output = torch.matmul(tensor_dev, weights)
    return output


if __name__ == "__main__":
    dummy_input = torch.randn(4, 8)
    preds = predict(dummy_input)
    print("Inference output:", preds)
