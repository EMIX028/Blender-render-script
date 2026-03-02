class Settings:
    def __init__(self, engine="BLENDER_EEVEE_NEXT",format="PNG"):
        self._engine = engine
        self._format = format

    def get_engine(self):
        return self._engine

    def get_format(self):
        return self._format
