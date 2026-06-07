import unittest

from platform_motion import advance_bouncing_axis


class AdvanceBouncingAxisTests(unittest.TestCase):
    def test_advances_without_reaching_a_bound(self):
        position, velocity = advance_bouncing_axis(0, 2, -4, 4, 0.5)

        self.assertEqual(position, 1)
        self.assertEqual(velocity, 2)

    def test_reflects_at_upper_bound_without_resetting(self):
        position, velocity = advance_bouncing_axis(3.5, 2, -4, 4, 0.5)

        self.assertEqual(position, 3.5)
        self.assertEqual(velocity, -2)

    def test_reflects_at_lower_bound_without_resetting(self):
        position, velocity = advance_bouncing_axis(-3.5, -2, -4, 4, 0.5)

        self.assertEqual(position, -3.5)
        self.assertEqual(velocity, 2)

    def test_preserves_multiple_reflections_during_a_long_frame(self):
        position, velocity = advance_bouncing_axis(0, 10, -2, 2, 1)

        self.assertEqual(position, 2)
        self.assertEqual(velocity, -10)

    def test_stationary_axis_stays_in_place(self):
        position, velocity = advance_bouncing_axis(7, 0, 7, 7, 1)

        self.assertEqual(position, 7)
        self.assertEqual(velocity, 0)


if __name__ == "__main__":
    unittest.main()
