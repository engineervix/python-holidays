#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import BANK, PUBLIC, SCHOOL, WORKDAY
from holidays.countries.laos import Laos, LA, LAO
from tests.common import CommonCountryTests


class TestLaos(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Laos, years=range(1976, 2050), years_non_observed=range(2018, 2050))

    def test_country_aliases(self):
        self.assertAliases(Laos, LA, LAO)

    def test_no_holidays(self):
        self.assertNoHolidays(Laos(categories=(BANK, PUBLIC, SCHOOL, WORKDAY), years=1975))

    def test_special_bank_holiday(self):
        self.assertHoliday(
            Laos(categories=BANK),
            "2015-01-02",
        )
        self.assertNoNonObservedHoliday(
            Laos(categories=BANK, observed=False),
            "2012-10-08",
            "2017-10-09",
            "2018-10-08",
            "2023-10-09",
        )

    def test_special_public_holiday(self):
        dt = ("2015-04-17",)
        dt_observed = (
            "2011-04-13",
            "2020-04-17",
        )
        self.assertHoliday(dt, dt_observed)
        self.assertNoNonObservedHoliday(dt_observed)

    def test_special_workday(self):
        self.assertHoliday(
            Laos(categories=WORKDAY),
            "2019-07-22",
        )
        self.assertNoNonObservedHoliday(
            Laos(categories=WORKDAY, observed=False),
            "2019-07-22",
        )

    def test_2022_public_holiday(self):
        self.assertHolidays(
            Laos(categories=PUBLIC, years=2022),
            ("2022-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2022-01-03", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2022-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2022-04-14", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2022-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2022-05-02", "ພັກຊົດເຊີຍວັນກຳມະກອນສາກົນ"),
            ("2022-12-02", "ວັນຊາດ"),
        )

    def test_2023_public_holiday(self):
        self.assertHolidays(
            Laos(categories=PUBLIC, years=2023),
            ("2023-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2023-01-02", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2023-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2023-04-14", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-17", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2023-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2023-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2023-12-02", "ວັນຊາດ"),
            ("2023-12-04", "ພັກຊົດເຊີຍວັນຊາດ"),
        )

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1976, 2050))

        self.assertNoNonObservedHoliday(
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )

    def test_international_women_rights_day(self):
        self.assertHoliday(f"{year}-03-08" for year in range(1976, 2050))

        self.assertNoNonObservedHoliday(
            "2015-03-09",
            "2020-03-09",
        )

    def test_laos_new_year_day(self):
        songkran_years_apr_13_15 = {2012, 2017}
        songkran_years_apr_13_16 = {2016, 2020, 2024}
        for year in range(1976, 2050):
            if year in songkran_years_apr_13_15:
                self.assertHoliday(f"{year}-04-13", f"{year}-04-14", f"{year}-04-15")
            elif year in songkran_years_apr_13_16:
                self.assertHoliday(
                    f"{year}-04-13",
                    f"{year}-04-14",
                    f"{year}-04-15",
                    f"{year}-04-16",
                )
            else:
                self.assertHoliday(f"{year}-04-14", f"{year}-04-15", f"{year}-04-16")

        self.assertNoNonObservedHoliday(
            "2012-04-16",
            "2012-04-17",
            "2013-04-17",
            "2016-04-18",
            "2017-04-17",
            "2018-04-17",
            "2018-04-18",
            "2019-04-17",
            "2022-04-18",
            "2023-04-17",
            "2023-04-18",
            "2024-04-17",
            "2024-04-18",
        )

    def test_labor_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1976, 2050))

        self.assertNoNonObservedHoliday(
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
        )

    def test_international_children_day_public(self):
        self.assertHoliday(f"{year}-06-01" for year in range(1990, 2018))

    def test_lao_national_day(self):
        self.assertHoliday(f"{year}-12-02" for year in range(1976, 2050))

        self.assertNoNonObservedHoliday(
            "2012-12-03",
            "2017-12-04",
            "2018-12-03",
            "2023-12-04",
        )

    def test_2014_bank_holidays(self):
        # Dec 31 is Wednesday.
        self.assertHolidays(
            Laos(categories=BANK, years=2014),
            ("2014-10-07", "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2014-12-29", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2014-12-30", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2014-12-31", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_2018_bank_holidays(self):
        # Dec 31 is Monday.
        self.assertHolidays(
            Laos(categories=BANK, years=2018),
            ("2018-10-07", "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2018-10-08", "ພັກຊົດເຊີຍວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2018-12-27", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2018-12-28", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2018-12-31", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_2019_bank_holidays(self):
        # Dec 31 is Tuesday.
        self.assertHolidays(
            Laos(categories=BANK, years=2019),
            ("2019-10-07", "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2019-12-27", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2019-12-30", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2019-12-31", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_2020_bank_holidays(self):
        # Dec 31 is Thursday.
        self.assertHolidays(
            Laos(categories=BANK, years=2020),
            ("2020-10-07", "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2020-12-29", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2020-12-30", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2020-12-31", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_2021_bank_holidays(self):
        # Dec 31 is Friday.
        self.assertHolidays(
            Laos(categories=BANK, years=2021),
            ("2021-10-07", "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2021-12-29", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2021-12-30", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2021-12-31", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_2022_bank_holidays(self):
        # Dec 31 is Saturday.
        self.assertHolidays(
            Laos(categories=BANK, years=2022),
            ("2022-10-07", "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2022-12-28", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2022-12-29", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2022-12-30", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_2023_bank_holidays(self):
        # Dec 31 is Sunday.
        self.assertHolidays(
            Laos(categories=BANK, years=2023),
            ("2023-10-07", "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2023-10-09", "ພັກຊົດເຊີຍວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2023-12-27", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2023-12-28", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2023-12-29", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_1993_school_holidays(self):
        # Prior to Adoption of National Teacher Day
        self.assertHolidays(
            Laos(categories=SCHOOL, years=1993),
            ("1993-02-06", "ວັນບຸນມາຂະບູຊາ"),
            ("1993-05-05", "ວັນບຸນວິສາຂະບູຊາ"),
            ("1993-07-03", "ວັນບຸນເຂົ້າພັນສາ"),
            ("1993-08-16", "ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"),
            ("1993-08-31", "ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"),
            ("1993-09-30", "ວັນບຸນອອກພັນສາ"),
            ("1993-10-01", "ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"),
            ("1993-10-29", "ວັນບຸນທາດຫລວງ"),
        )

    def test_2022_school_holidays(self):
        self.assertHolidays(
            Laos(categories=SCHOOL, years=2022),
            ("2022-02-16", "ວັນບຸນມາຂະບູຊາ"),
            ("2022-05-15", "ວັນບຸນວິສາຂະບູຊາ"),
            ("2022-07-13", "ວັນບຸນເຂົ້າພັນສາ"),
            ("2022-08-26", "ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"),
            ("2022-09-10", "ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"),
            ("2022-10-07", "ວັນຄູແຫ່ງຊາດ"),
            ("2022-10-10", "ວັນບຸນອອກພັນສາ"),
            ("2022-10-11", "ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"),
            ("2022-11-08", "ວັນບຸນທາດຫລວງ"),
        )

    def test_2023_school_holidays(self):
        self.assertHolidays(
            Laos(categories=SCHOOL, years=2023),
            ("2023-02-05", "ວັນບຸນມາຂະບູຊາ"),
            ("2023-05-04", "ວັນບຸນວິສາຂະບູຊາ"),
            ("2023-08-01", "ວັນບຸນເຂົ້າພັນສາ"),
            ("2023-09-14", "ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"),
            ("2023-09-29", "ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"),
            ("2023-10-07", "ວັນຄູແຫ່ງຊາດ"),
            ("2023-10-29", "ວັນບຸນອອກພັນສາ"),
            ("2023-10-30", "ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"),
            ("2023-11-27", "ວັນບຸນທາດຫລວງ"),
        )

    def test_1988_workdays(self):
        # Prior to National Arbor Day creation in 1989.
        self.assertHolidays(
            Laos(categories=WORKDAY, years=1988),
            ("1988-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("1988-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("1988-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("1988-04-14", "ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("1988-07-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ"),
            ("1988-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("1988-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("1988-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("1988-10-12", "ວັນປະກາດເອກະລາດ"),
        )

    def test_1990_workdays(self):
        # Prior to Kaysone Phomvihane's Presidency and 1991 Constitution Adoption.
        self.assertHolidays(
            Laos(categories=WORKDAY, years=1990),
            ("1990-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("1990-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("1990-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("1990-04-14", "ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("1990-06-01", "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ"),
            ("1990-07-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ"),
            ("1990-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("1990-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("1990-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("1990-10-12", "ວັນປະກາດເອກະລາດ"),
        )

    def test_1996_workdays(self):
        # Prior to 1997's Lao Wildlife Conservation Day Designation.
        self.assertHolidays(
            Laos(categories=WORKDAY, years=1996),
            ("1996-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("1996-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("1996-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("1996-04-14", "ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("1996-06-01", "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ"),
            ("1996-07-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ"),
            ("1996-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("1996-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("1996-08-15", "ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ"),
            ("1996-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("1996-10-12", "ວັນປະກາດເອກະລາດ"),
            ("1996-12-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ"),
        )

    def test_2017_workdays(self):
        # Prior to 2018 International Children's Day is in `PUBLIC` category
        self.assertHolidays(
            Laos(categories=WORKDAY, years=2017),
            ("2017-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("2017-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("2017-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("2017-04-14", "ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("2017-06-01", "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ"),
            ("2017-07-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ; ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ"),
            ("2017-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("2017-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("2017-08-15", "ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ"),
            ("2017-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("2017-10-12", "ວັນປະກາດເອກະລາດ"),
            ("2017-12-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ"),
        )

    def test_2022_workdays(self):
        self.assertHolidays(
            Laos(categories=WORKDAY, years=2022),
            ("2022-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("2022-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("2022-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("2022-04-14", "ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("2022-06-01", "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ; ວັນເດັກສາກົນ"),
            ("2022-07-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ; ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ"),
            ("2022-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("2022-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("2022-08-15", "ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ"),
            ("2022-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("2022-10-12", "ວັນປະກາດເອກະລາດ"),
            ("2022-12-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2022-01-03", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2022-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("2022-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("2022-02-16", "ວັນບຸນມາຂະບູຊາ"),
            ("2022-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2022-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("2022-04-14", "ບຸນປີໃໝ່ລາວ; ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("2022-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2022-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2022-05-02", "ພັກຊົດເຊີຍວັນກຳມະກອນສາກົນ"),
            ("2022-05-15", "ວັນບຸນວິສາຂະບູຊາ"),
            ("2022-06-01", "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ; ວັນເດັກສາກົນ"),
            (
                "2022-07-13",
                ("ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ; ວັນບຸນເຂົ້າພັນສາ; ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ"),
            ),
            ("2022-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("2022-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("2022-08-15", "ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ"),
            ("2022-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("2022-08-26", "ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"),
            ("2022-09-10", "ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"),
            ("2022-10-07", "ວັນຄູແຫ່ງຊາດ; ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2022-10-10", "ວັນບຸນອອກພັນສາ"),
            ("2022-10-11", "ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"),
            ("2022-10-12", "ວັນປະກາດເອກະລາດ"),
            ("2022-11-08", "ວັນບຸນທາດຫລວງ"),
            ("2022-12-02", "ວັນຊາດ"),
            ("2022-12-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ"),
            ("2022-12-28", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2022-12-29", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2022-12-30", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (in lieu)"),
            ("2022-01-20", "Lao People's Armed Force Day"),
            ("2022-02-01", "Lao Federation of Trade Union's Day"),
            ("2022-02-16", "Makha Bousa Festival"),
            ("2022-03-08", "International Women's Rights Day"),
            ("2022-03-22", "Establishment Day of the Lao People's Revolutionary Party"),
            ("2022-04-14", "Lao New Year's Day; Lao People's Revolutionary Youth Union Day"),
            ("2022-04-15", "Lao New Year's Day"),
            ("2022-04-16", "Lao New Year's Day"),
            ("2022-04-18", "Lao New Year's Day (in lieu)"),
            ("2022-05-01", "International Labor Day"),
            ("2022-05-02", "International Labor Day (in lieu)"),
            ("2022-05-15", "Visakha Bousa Festival"),
            ("2022-06-01", "International Children's Day; National Arbor Day"),
            (
                "2022-07-13",
                (
                    "Begin of Buddhist Lent; President Souphanouvong's Birthday; "
                    "The National Day for Wildlife and Aquatic Animal Conservation"
                ),
            ),
            ("2022-07-20", "Establishment Day of the Lao Women's Union"),
            ("2022-08-13", "Lao National Mass Media and Publishing Day"),
            ("2022-08-15", "Lao National Constitution Day"),
            ("2022-08-23", "National Uprising Day"),
            ("2022-08-26", "Boun Haw Khao Padapdin"),
            ("2022-09-10", "Boun Haw Khao Salark"),
            ("2022-10-07", "Establishment Day of the BOL; National Teacher Day"),
            ("2022-10-10", "End of Buddhist Lent"),
            ("2022-10-11", "Vientiane Boat Racing Festival"),
            ("2022-10-12", "Indepedence Declaration Day"),
            ("2022-11-08", "Boun That Luang Festival"),
            ("2022-12-02", "Lao National Day"),
            ("2022-12-13", "President Kaysone Phomvihane's Birthday"),
            ("2022-12-28", "Lao Year-End Bank Holiday"),
            ("2022-12-29", "Lao Year-End Bank Holiday"),
            ("2022-12-30", "Lao Year-End Bank Holiday"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันปีใหม่สากล"),
            ("2022-01-03", "ชดเชยวันปีใหม่สากล"),
            ("2022-01-20", "วันก่อตั้งกองทัพประชาชนลาว"),
            ("2022-02-01", "วันก่อตั้งสหพันธ์กำมะบานลาว"),
            ("2022-02-16", "วันมาฆบูชา"),
            ("2022-03-08", "วันสตรีสากล"),
            ("2022-03-22", "วันก่อตั้งพรรคประชาชนปฏิวัติลาว"),
            ("2022-04-14", "วันก่อตั้งศูนย์ซาวหนุ่มประชาชนปฏิวัติลาว; วันปีใหม่ลาว"),
            ("2022-04-15", "วันปีใหม่ลาว"),
            ("2022-04-16", "วันปีใหม่ลาว"),
            ("2022-04-18", "ชดเชยวันปีใหม่ลาว"),
            ("2022-05-01", "วันแรงงานสากล"),
            ("2022-05-02", "ชดเชยวันแรงงานสากล"),
            ("2022-05-15", "วันวิสาขบูชา"),
            ("2022-06-01", "วันปลูกต้นไม้แห่งชาติ; วันเด็กสากล"),
            (
                "2022-07-13",
                ("วันคล้ายวันเกิดท่านประธานสุภานุวงศ์; วันอนุรักษ์สัตว์น้ำ สัตว์ป่า และวันปล่อยปลาแห่งชาติ; วันเข้าพรรษา"),
            ),
            ("2022-07-20", "วันก่อตั้งสหภาพแม่หญิงลาว"),
            ("2022-08-13", "วันสื่อสารมวลชนและการพิมพ์แห่งชาติ"),
            ("2022-08-15", "วันรัฐธรรมนูญแห่งชาติ"),
            ("2022-08-23", "วันยึดอำนาจทั่วประเทศ"),
            ("2022-08-26", "วันบุญข้าวประดับดิน"),
            ("2022-09-10", "วันข้าวบุญข้าวสาก"),
            ("2022-10-07", "วันก่อตั้งธนาคารแห่ง สปป. ลาว; วันครูแห่งชาติ"),
            ("2022-10-10", "วันออกพรรษา"),
            ("2022-10-11", "วันงานบุญแข่งเรือ นครหลวงเวียงจันทน์"),
            ("2022-10-12", "วันประกาศเอกราช"),
            ("2022-11-08", "วันงานพระธาตุหลวง"),
            ("2022-12-02", "วันชาติ สปป. ลาว"),
            ("2022-12-13", "วันคล้ายวันเกิดท่านประธานไกสอน พมวิหาน"),
            ("2022-12-28", "วันหยุดสิ้นปีของสถาบันการเงิน"),
            ("2022-12-29", "วันหยุดสิ้นปีของสถาบันการเงิน"),
            ("2022-12-30", "วันหยุดสิ้นปีของสถาบันการเงิน"),
        )
