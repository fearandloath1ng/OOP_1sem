class GeometricPrimitive:
    def __init__(self, color: str, visible: bool):
        self.color = color
        self.visible = visible

    def toggle_visibility(self):
        self.visible = not self.visible

    def __str__(self):
        return f"GeometricPrimitive(Color: {self.color}, Visible: {self.visible})"
