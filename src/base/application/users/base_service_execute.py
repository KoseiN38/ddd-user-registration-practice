from abc import ABC, abstractmethod


class BaseUserApplication(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        """ツールの初期化."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """アプリケーション実行."""
