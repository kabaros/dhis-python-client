from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RelativePeriods")


@_attrs_define
class RelativePeriods:
    """
    Attributes:
        bi_months_this_year (Union[Unset, bool]):
        last_10_financial_years (Union[Unset, bool]):
        last_10_years (Union[Unset, bool]):
        last_12_months (Union[Unset, bool]):
        last_12_weeks (Union[Unset, bool]):
        last_14_days (Union[Unset, bool]):
        last_180_days (Union[Unset, bool]):
        last_2_six_months (Union[Unset, bool]):
        last_30_days (Union[Unset, bool]):
        last_3_days (Union[Unset, bool]):
        last_3_months (Union[Unset, bool]):
        last_4_bi_weeks (Union[Unset, bool]):
        last_4_quarters (Union[Unset, bool]):
        last_4_weeks (Union[Unset, bool]):
        last_52_weeks (Union[Unset, bool]):
        last_5_financial_years (Union[Unset, bool]):
        last_5_years (Union[Unset, bool]):
        last_60_days (Union[Unset, bool]):
        last_6_bi_months (Union[Unset, bool]):
        last_6_months (Union[Unset, bool]):
        last_7_days (Union[Unset, bool]):
        last_90_days (Union[Unset, bool]):
        last_bi_week (Union[Unset, bool]):
        last_bimonth (Union[Unset, bool]):
        last_financial_year (Union[Unset, bool]):
        last_month (Union[Unset, bool]):
        last_quarter (Union[Unset, bool]):
        last_six_month (Union[Unset, bool]):
        last_week (Union[Unset, bool]):
        last_year (Union[Unset, bool]):
        months_last_year (Union[Unset, bool]):
        months_this_year (Union[Unset, bool]):
        quarters_last_year (Union[Unset, bool]):
        quarters_this_year (Union[Unset, bool]):
        this_bi_week (Union[Unset, bool]):
        this_bimonth (Union[Unset, bool]):
        this_day (Union[Unset, bool]):
        this_financial_year (Union[Unset, bool]):
        this_month (Union[Unset, bool]):
        this_quarter (Union[Unset, bool]):
        this_six_month (Union[Unset, bool]):
        this_week (Union[Unset, bool]):
        this_year (Union[Unset, bool]):
        weeks_this_year (Union[Unset, bool]):
        yesterday (Union[Unset, bool]):
    """

    bi_months_this_year: Union[Unset, bool] = UNSET
    last_10_financial_years: Union[Unset, bool] = UNSET
    last_10_years: Union[Unset, bool] = UNSET
    last_12_months: Union[Unset, bool] = UNSET
    last_12_weeks: Union[Unset, bool] = UNSET
    last_14_days: Union[Unset, bool] = UNSET
    last_180_days: Union[Unset, bool] = UNSET
    last_2_six_months: Union[Unset, bool] = UNSET
    last_30_days: Union[Unset, bool] = UNSET
    last_3_days: Union[Unset, bool] = UNSET
    last_3_months: Union[Unset, bool] = UNSET
    last_4_bi_weeks: Union[Unset, bool] = UNSET
    last_4_quarters: Union[Unset, bool] = UNSET
    last_4_weeks: Union[Unset, bool] = UNSET
    last_52_weeks: Union[Unset, bool] = UNSET
    last_5_financial_years: Union[Unset, bool] = UNSET
    last_5_years: Union[Unset, bool] = UNSET
    last_60_days: Union[Unset, bool] = UNSET
    last_6_bi_months: Union[Unset, bool] = UNSET
    last_6_months: Union[Unset, bool] = UNSET
    last_7_days: Union[Unset, bool] = UNSET
    last_90_days: Union[Unset, bool] = UNSET
    last_bi_week: Union[Unset, bool] = UNSET
    last_bimonth: Union[Unset, bool] = UNSET
    last_financial_year: Union[Unset, bool] = UNSET
    last_month: Union[Unset, bool] = UNSET
    last_quarter: Union[Unset, bool] = UNSET
    last_six_month: Union[Unset, bool] = UNSET
    last_week: Union[Unset, bool] = UNSET
    last_year: Union[Unset, bool] = UNSET
    months_last_year: Union[Unset, bool] = UNSET
    months_this_year: Union[Unset, bool] = UNSET
    quarters_last_year: Union[Unset, bool] = UNSET
    quarters_this_year: Union[Unset, bool] = UNSET
    this_bi_week: Union[Unset, bool] = UNSET
    this_bimonth: Union[Unset, bool] = UNSET
    this_day: Union[Unset, bool] = UNSET
    this_financial_year: Union[Unset, bool] = UNSET
    this_month: Union[Unset, bool] = UNSET
    this_quarter: Union[Unset, bool] = UNSET
    this_six_month: Union[Unset, bool] = UNSET
    this_week: Union[Unset, bool] = UNSET
    this_year: Union[Unset, bool] = UNSET
    weeks_this_year: Union[Unset, bool] = UNSET
    yesterday: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bi_months_this_year = self.bi_months_this_year

        last_10_financial_years = self.last_10_financial_years

        last_10_years = self.last_10_years

        last_12_months = self.last_12_months

        last_12_weeks = self.last_12_weeks

        last_14_days = self.last_14_days

        last_180_days = self.last_180_days

        last_2_six_months = self.last_2_six_months

        last_30_days = self.last_30_days

        last_3_days = self.last_3_days

        last_3_months = self.last_3_months

        last_4_bi_weeks = self.last_4_bi_weeks

        last_4_quarters = self.last_4_quarters

        last_4_weeks = self.last_4_weeks

        last_52_weeks = self.last_52_weeks

        last_5_financial_years = self.last_5_financial_years

        last_5_years = self.last_5_years

        last_60_days = self.last_60_days

        last_6_bi_months = self.last_6_bi_months

        last_6_months = self.last_6_months

        last_7_days = self.last_7_days

        last_90_days = self.last_90_days

        last_bi_week = self.last_bi_week

        last_bimonth = self.last_bimonth

        last_financial_year = self.last_financial_year

        last_month = self.last_month

        last_quarter = self.last_quarter

        last_six_month = self.last_six_month

        last_week = self.last_week

        last_year = self.last_year

        months_last_year = self.months_last_year

        months_this_year = self.months_this_year

        quarters_last_year = self.quarters_last_year

        quarters_this_year = self.quarters_this_year

        this_bi_week = self.this_bi_week

        this_bimonth = self.this_bimonth

        this_day = self.this_day

        this_financial_year = self.this_financial_year

        this_month = self.this_month

        this_quarter = self.this_quarter

        this_six_month = self.this_six_month

        this_week = self.this_week

        this_year = self.this_year

        weeks_this_year = self.weeks_this_year

        yesterday = self.yesterday

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bi_months_this_year is not UNSET:
            field_dict["biMonthsThisYear"] = bi_months_this_year
        if last_10_financial_years is not UNSET:
            field_dict["last10FinancialYears"] = last_10_financial_years
        if last_10_years is not UNSET:
            field_dict["last10Years"] = last_10_years
        if last_12_months is not UNSET:
            field_dict["last12Months"] = last_12_months
        if last_12_weeks is not UNSET:
            field_dict["last12Weeks"] = last_12_weeks
        if last_14_days is not UNSET:
            field_dict["last14Days"] = last_14_days
        if last_180_days is not UNSET:
            field_dict["last180Days"] = last_180_days
        if last_2_six_months is not UNSET:
            field_dict["last2SixMonths"] = last_2_six_months
        if last_30_days is not UNSET:
            field_dict["last30Days"] = last_30_days
        if last_3_days is not UNSET:
            field_dict["last3Days"] = last_3_days
        if last_3_months is not UNSET:
            field_dict["last3Months"] = last_3_months
        if last_4_bi_weeks is not UNSET:
            field_dict["last4BiWeeks"] = last_4_bi_weeks
        if last_4_quarters is not UNSET:
            field_dict["last4Quarters"] = last_4_quarters
        if last_4_weeks is not UNSET:
            field_dict["last4Weeks"] = last_4_weeks
        if last_52_weeks is not UNSET:
            field_dict["last52Weeks"] = last_52_weeks
        if last_5_financial_years is not UNSET:
            field_dict["last5FinancialYears"] = last_5_financial_years
        if last_5_years is not UNSET:
            field_dict["last5Years"] = last_5_years
        if last_60_days is not UNSET:
            field_dict["last60Days"] = last_60_days
        if last_6_bi_months is not UNSET:
            field_dict["last6BiMonths"] = last_6_bi_months
        if last_6_months is not UNSET:
            field_dict["last6Months"] = last_6_months
        if last_7_days is not UNSET:
            field_dict["last7Days"] = last_7_days
        if last_90_days is not UNSET:
            field_dict["last90Days"] = last_90_days
        if last_bi_week is not UNSET:
            field_dict["lastBiWeek"] = last_bi_week
        if last_bimonth is not UNSET:
            field_dict["lastBimonth"] = last_bimonth
        if last_financial_year is not UNSET:
            field_dict["lastFinancialYear"] = last_financial_year
        if last_month is not UNSET:
            field_dict["lastMonth"] = last_month
        if last_quarter is not UNSET:
            field_dict["lastQuarter"] = last_quarter
        if last_six_month is not UNSET:
            field_dict["lastSixMonth"] = last_six_month
        if last_week is not UNSET:
            field_dict["lastWeek"] = last_week
        if last_year is not UNSET:
            field_dict["lastYear"] = last_year
        if months_last_year is not UNSET:
            field_dict["monthsLastYear"] = months_last_year
        if months_this_year is not UNSET:
            field_dict["monthsThisYear"] = months_this_year
        if quarters_last_year is not UNSET:
            field_dict["quartersLastYear"] = quarters_last_year
        if quarters_this_year is not UNSET:
            field_dict["quartersThisYear"] = quarters_this_year
        if this_bi_week is not UNSET:
            field_dict["thisBiWeek"] = this_bi_week
        if this_bimonth is not UNSET:
            field_dict["thisBimonth"] = this_bimonth
        if this_day is not UNSET:
            field_dict["thisDay"] = this_day
        if this_financial_year is not UNSET:
            field_dict["thisFinancialYear"] = this_financial_year
        if this_month is not UNSET:
            field_dict["thisMonth"] = this_month
        if this_quarter is not UNSET:
            field_dict["thisQuarter"] = this_quarter
        if this_six_month is not UNSET:
            field_dict["thisSixMonth"] = this_six_month
        if this_week is not UNSET:
            field_dict["thisWeek"] = this_week
        if this_year is not UNSET:
            field_dict["thisYear"] = this_year
        if weeks_this_year is not UNSET:
            field_dict["weeksThisYear"] = weeks_this_year
        if yesterday is not UNSET:
            field_dict["yesterday"] = yesterday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        bi_months_this_year = d.pop("biMonthsThisYear", UNSET)

        last_10_financial_years = d.pop("last10FinancialYears", UNSET)

        last_10_years = d.pop("last10Years", UNSET)

        last_12_months = d.pop("last12Months", UNSET)

        last_12_weeks = d.pop("last12Weeks", UNSET)

        last_14_days = d.pop("last14Days", UNSET)

        last_180_days = d.pop("last180Days", UNSET)

        last_2_six_months = d.pop("last2SixMonths", UNSET)

        last_30_days = d.pop("last30Days", UNSET)

        last_3_days = d.pop("last3Days", UNSET)

        last_3_months = d.pop("last3Months", UNSET)

        last_4_bi_weeks = d.pop("last4BiWeeks", UNSET)

        last_4_quarters = d.pop("last4Quarters", UNSET)

        last_4_weeks = d.pop("last4Weeks", UNSET)

        last_52_weeks = d.pop("last52Weeks", UNSET)

        last_5_financial_years = d.pop("last5FinancialYears", UNSET)

        last_5_years = d.pop("last5Years", UNSET)

        last_60_days = d.pop("last60Days", UNSET)

        last_6_bi_months = d.pop("last6BiMonths", UNSET)

        last_6_months = d.pop("last6Months", UNSET)

        last_7_days = d.pop("last7Days", UNSET)

        last_90_days = d.pop("last90Days", UNSET)

        last_bi_week = d.pop("lastBiWeek", UNSET)

        last_bimonth = d.pop("lastBimonth", UNSET)

        last_financial_year = d.pop("lastFinancialYear", UNSET)

        last_month = d.pop("lastMonth", UNSET)

        last_quarter = d.pop("lastQuarter", UNSET)

        last_six_month = d.pop("lastSixMonth", UNSET)

        last_week = d.pop("lastWeek", UNSET)

        last_year = d.pop("lastYear", UNSET)

        months_last_year = d.pop("monthsLastYear", UNSET)

        months_this_year = d.pop("monthsThisYear", UNSET)

        quarters_last_year = d.pop("quartersLastYear", UNSET)

        quarters_this_year = d.pop("quartersThisYear", UNSET)

        this_bi_week = d.pop("thisBiWeek", UNSET)

        this_bimonth = d.pop("thisBimonth", UNSET)

        this_day = d.pop("thisDay", UNSET)

        this_financial_year = d.pop("thisFinancialYear", UNSET)

        this_month = d.pop("thisMonth", UNSET)

        this_quarter = d.pop("thisQuarter", UNSET)

        this_six_month = d.pop("thisSixMonth", UNSET)

        this_week = d.pop("thisWeek", UNSET)

        this_year = d.pop("thisYear", UNSET)

        weeks_this_year = d.pop("weeksThisYear", UNSET)

        yesterday = d.pop("yesterday", UNSET)

        relative_periods = cls(
            bi_months_this_year=bi_months_this_year,
            last_10_financial_years=last_10_financial_years,
            last_10_years=last_10_years,
            last_12_months=last_12_months,
            last_12_weeks=last_12_weeks,
            last_14_days=last_14_days,
            last_180_days=last_180_days,
            last_2_six_months=last_2_six_months,
            last_30_days=last_30_days,
            last_3_days=last_3_days,
            last_3_months=last_3_months,
            last_4_bi_weeks=last_4_bi_weeks,
            last_4_quarters=last_4_quarters,
            last_4_weeks=last_4_weeks,
            last_52_weeks=last_52_weeks,
            last_5_financial_years=last_5_financial_years,
            last_5_years=last_5_years,
            last_60_days=last_60_days,
            last_6_bi_months=last_6_bi_months,
            last_6_months=last_6_months,
            last_7_days=last_7_days,
            last_90_days=last_90_days,
            last_bi_week=last_bi_week,
            last_bimonth=last_bimonth,
            last_financial_year=last_financial_year,
            last_month=last_month,
            last_quarter=last_quarter,
            last_six_month=last_six_month,
            last_week=last_week,
            last_year=last_year,
            months_last_year=months_last_year,
            months_this_year=months_this_year,
            quarters_last_year=quarters_last_year,
            quarters_this_year=quarters_this_year,
            this_bi_week=this_bi_week,
            this_bimonth=this_bimonth,
            this_day=this_day,
            this_financial_year=this_financial_year,
            this_month=this_month,
            this_quarter=this_quarter,
            this_six_month=this_six_month,
            this_week=this_week,
            this_year=this_year,
            weeks_this_year=weeks_this_year,
            yesterday=yesterday,
        )

        relative_periods.additional_properties = d
        return relative_periods

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
