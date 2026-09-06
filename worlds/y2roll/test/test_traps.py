from worlds.y2roll.test.bases import Y2ROLLTestBase

from .. import options


class TestY2ROLLTraps(Y2ROLLTestBase):
    options = {
        "trap_weights": options.TrapWeights.default,
        "trap_percentage": 100,
    }

    def test_trap_weights(self) -> None:
        weights = self.world.output_trap_weights()
        keys = self.world.options.trap_weights.keys()
        for trap in keys:
            with self.subTest("Trap present", trap=trap):
                self.assertIn(trap, weights.keys())
