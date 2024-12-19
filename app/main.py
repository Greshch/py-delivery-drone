class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

class BaseRobot:
    def __init__(self, name: str, weight: int, coords = None):
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = [coord for coord in coords]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords = None):
        super().__init__(name, weight, coords)
        if coords is None:
            self.coords.append(0)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step

class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords,
            max_load_weight : int,
            current_load: Cargo = None

    ) -> None:
        super().__init__(name, weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        self.hook_load(current_load)

    def hook_load(self, cargo: Cargo):
        if not self.current_load is None:
            return
        if cargo is None:
            return
        if self.max_load_weight < cargo.weight:
            return
        self.current_load = cargo

    def unhook_load(self):
        self.current_load = None