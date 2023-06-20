"""Base Lightning DataModule."""

from typing import Literal, final

import lightning.pytorch as pl
import torch
from torch.utils.data import DataLoader, Dataset


class BaseDataModule(pl.LightningDataModule):
    """The Base DataModule class.

    Subclasses should implement any of the following attributes that
    are to be utilized:

    - ``train_data`` (``torch.utils.data.Dataset``): Training dataset.

    - ``val_data`` (``torch.utils.data.Dataset``): Validation dataset.

    - ``test_data`` (``torch.utils.data.Dataset``): Testing dataset.

    - ``predict_data`` (``torch.utils.data.Dataset``): Prediction
    dataset.

    Attributes:
        data_dir (str): Path to the data directory.
        per_device_batch_size (int): Per-device number of samples to
            load per iteration.
        per_device_num_workers (int): Number of CPU processes to use
            for data loading (``0`` means that the data will be loaded
            by each main process)
        pin_memory (bool): Whether to copy tensors into device pinned
            memory before returning them (is set to ``True`` if using
            GPUs).
    """

    def __init__(
        self: "BaseDataModule",
        data_dir: str,
        per_device_batch_size: int = 1,
        per_device_num_workers: int = 0,
        device_type: Literal["cpu", "gpu"] = "gpu",
    ) -> None:
        """Constructor.

        Calls parent constructor and stores arguments.

        Args:
            data_dir: Path to the data directory.
            per_device_batch_size: Per-device number of samples to load
                per iteration.
            per_device_num_workers: Number of CPU processes to use for
                data loading (``0`` means that the data will be loaded
                by each main process)
            device_type: The compute device type to use (``cpu`` or
                ``gpu``).
        """
        super().__init__()

        self.data_dir = data_dir
        self.per_device_batch_size = per_device_batch_size
        self.per_device_num_workers = per_device_num_workers
        self.pin_memory = device_type == "gpu"

    @final
    def load_state_dict(
        self: "BaseDataModule",
        state_dict: dict[str, int],
    ) -> None:
        """Loads an existing ``state_dict``.

        Currently this is only used to load the
        ``per_device_batch_size``.

        Args:
            state_dict: The state dictionary to load.
        """
        self.per_device_batch_size = state_dict["per_device_batch_size"]

    @final
    def state_dict(self: "BaseDataModule") -> dict[str, int]:
        """Returns this datamodule's ``state_dict``.

        Currently this is only used to save the
        ``per_device_batch_size``.

        Returns:
            A copy of this datamodule's state dictionary.
        """
        return {"per_device_batch_size": self.per_device_batch_size}

    @final
    def train_dataloader(self: "BaseDataModule") -> DataLoader[torch.Tensor]:
        """Returns the train ``torch.utils.data.DataLoader`` object.

        Builds and returns a new ``torch.utils.data.DataLoader`` object
        using ``train_data`` and previously defined attributes.

        Returns:
            The training ``torch.utils.data.DataLoader`` object.

        Raises:
            AttributeError: If ``train_data`` is not defined.
        """
        if not hasattr(self, "train_data"):
            self.train_data = Dataset[torch.Tensor]()  # appeases mypy
            raise AttributeError(name="train_data")

        return DataLoader(
            dataset=self.train_data,
            batch_size=self.per_device_batch_size,
            shuffle=True,
            num_workers=self.per_device_num_workers,
            pin_memory=self.pin_memory,
        )

    @final
    def val_dataloader(self: "BaseDataModule") -> DataLoader[torch.Tensor]:
        """Returns the val ``torch.utils.data.DataLoader`` object.

        Builds and returns a new ``torch.utils.data.DataLoader`` object
        using ``val_data`` and previously defined attributes.

        Returns:
            The validation ``torch.utils.data.DataLoader`` object.

        Raises:
            AttributeError: If ``val_data`` is not defined.
        """
        if not hasattr(self, "val_data"):
            self.val_data = Dataset[torch.Tensor]()  # appeases mypy
            raise AttributeError(name="val_data")

        return DataLoader(
            dataset=self.val_data,
            batch_size=self.per_device_batch_size,
            shuffle=True,
            num_workers=self.per_device_num_workers,
            pin_memory=self.pin_memory,
        )

    @final
    def test_dataloader(self: "BaseDataModule") -> DataLoader[torch.Tensor]:
        """Returns the test ``torch.utils.data.DataLoader`` object.

        Builds and returns a new ``torch.utils.data.DataLoader`` object
        using ``test_data`` and previously defined attributes.

        Returns:
            The testing ``torch.utils.data.DataLoader`` object.

        Raises:
            AttributeError: If ``test_data`` is not defined.
        """
        if not hasattr(self, "test_data"):
            self.test_data = Dataset[torch.Tensor]()  # appeases mypy
            raise AttributeError(name="test_data")

        return DataLoader(
            dataset=self.test_data,
            batch_size=self.per_device_batch_size,
            shuffle=True,
            num_workers=self.per_device_num_workers,
            pin_memory=self.pin_memory,
        )

    @final
    def predict_dataloader(self: "BaseDataModule") -> DataLoader[torch.Tensor]:
        """Returns the predict ``torch.utils.data.DataLoader`` object.

        Builds and returns a new ``torch.utils.data.DataLoader`` object
        using ``predict_data`` and previously defined attributes.

        Returns:
            The prediction ``torch.utils.data.DataLoader`` object.

        Raises:
            AttributeError: If ``predict_data`` is not defined.
        """
        if not hasattr(self, "predict_data"):
            self.predict_data = Dataset[torch.Tensor]()  # appeases mypy
            raise AttributeError(name="predict_data")

        return DataLoader(
            dataset=self.predict_data,
            batch_size=self.per_device_batch_size,
            shuffle=False,
            num_workers=self.per_device_num_workers,
            pin_memory=self.pin_memory,
        )