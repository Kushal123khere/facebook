import pytest

from library.excel_lib import ReadExcel
from library.config import Config
from POM.watch_module import WatchModule


class TestWatchModule:
    read_xl = ReadExcel()
    data = read_xl.read_test_data(Config.WATCH_TESTDATA_SHEET)

    @pytest.mark.parametrize("username, pwd", data)
    def test_login(self, init_driver, username, pwd):
        driver = init_driver
        lp = WatchModule(driver)
        lp.user_name(username)
        lp.pass_word(pwd)
        lp.log_in()
        lp.watch_1()
        lp.setting_1()
        lp.not1_start()
        lp.cus_not2()
        lp.allow_not3()
        lp.new1_not4()
        lp.man_pag()
        lp.cro_butt()
        lp.liv_btn()
        lp.show_btn()

