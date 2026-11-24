import shutil
from pathlib import Path


class FileManager:
    """Простой файловый менеджер, работающий внутри одной базовой папки."""

    def __init__(self, base_dir):
        self.base = Path(base_dir).resolve()
        self.base.mkdir(parents=True, exist_ok=True)

    def _safe(self, rel_path):
        """Не даёт выйти за пределы базовой папки (защита от ../)."""
        p = (self.base / rel_path).resolve()
        if self.base != p and self.base not in p.parents:
            raise PermissionError("Выход за пределы базовой папки запрещён")
        return p

    def list_dir(self, rel_path="."):
        return sorted(item.name for item in self._safe(rel_path).iterdir())

    def create_dir(self, rel_path):
        self._safe(rel_path).mkdir(parents=True, exist_ok=True)

    def write_file(self, rel_path, content):
        self._safe(rel_path).write_text(content, encoding="utf-8")

    def read_file(self, rel_path):
        return self._safe(rel_path).read_text(encoding="utf-8")

    def copy(self, src, dst):
        shutil.copy2(self._safe(src), self._safe(dst))

    def move(self, src, dst):
        shutil.move(str(self._safe(src)), str(self._safe(dst)))

    def delete(self, rel_path):
        p = self._safe(rel_path)
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()