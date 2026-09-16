"""Model training loop."""

import structlog
import torch
import torch.nn as nn
import torch.optim as optim

logger = structlog.get_logger()


def train_model(epochs: int = 5) -> None:
    """Execute simple training loop."""
    logger.info("training_started", epochs=epochs)
    model = nn.Linear(10, 1)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(1, epochs + 1):
        x = torch.randn(32, 10)
        y = torch.randn(32, 1)

        optimizer.zero_grad()
        output = model(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()

        logger.info("epoch_completed", epoch=epoch, loss=float(loss.item()))

    logger.info("training_finished")


if __name__ == "__main__":
    train_model()
