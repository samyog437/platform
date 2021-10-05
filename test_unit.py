from unittest import TestCase


class Test(TestCase):
    def test_draw(self):
        self.assertTrue(1, 2)


class Test(TestCase):
    def test_main_window(self):
        self.assertTrue(640, 480)


class Test(TestCase):
    def test_new_window(self):
        self.assertTrue(540, 380)


class Test(TestCase):
    def test_login_form(self):
        self.assertTrue(35,5)
class Test(TestCase):
    def test_horizontal_collision(self):
        self.assertTrue(1,0)
class Test(TestCase):
    def test_game_background(self):
        self.assertTrue(1, 2)


class TestLevel(TestCase):
    def test_level_setup(self):
        self.assertTrue(3, 4)


class TestPlayer(TestCase):
    def test_animate(self):
        True


class TestLevel(TestCase):
    def test_run(self):
        self.assertTrue(x,y)