import datetime
import logging
from logging import FileHandler, StreamHandler
from pathlib import Path


class CustomLogger:
    def __init__(self, name, is_log=False, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # logs/フォルダーを作成（存在しない場合）
        logs_dir = Path("logs")
        logs_dir.mkdir(exist_ok=True)

        # コンソール出力用のハンドラーを追加
        console_handler = StreamHandler()
        console_handler.setLevel(level)
        console_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_format)
        self.logger.addHandler(console_handler)

        # ファイル出力用のハンドラーを追加（is_logがTrueの場合）
        if is_log:
            log_file = self.generate_unique_log_file(logs_dir)
            file_handler = FileHandler(log_file)
            file_handler.setLevel(level)
            file_format = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(file_format)
            self.logger.addHandler(file_handler)

    def generate_unique_log_file(self, logs_dir):
        # ユニークなファイル名を生成
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_file = f"log_{timestamp}.log"
        return logs_dir / unique_file

    def get_logger(self):
        return self.logger


logger = CustomLogger(name="MyLogger", is_log=True, level=logging.DEBUG).get_logger()
