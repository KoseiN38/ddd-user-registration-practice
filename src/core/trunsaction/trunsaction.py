from functools import wraps

def transactional(func):
    """トランザクション処理を行うデコレーター"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            self.user_repository.commit()
            return result
        except Exception as e:
            self.user_repository.rollback()
            print(f"エラーが発生しました。トランザクションをロールバックします: {str(e)}")
            return None
    return wrapper
