from datetime import datetime, timedelta

from Leek.decision.strategy import GrowthSelection
from Leek.leek import Leek


def main():
    leek1 = Leek(1)
    g = GrowthSelection(leek1, datetime.today())
    start_date = datetime.strptime('2021-06-01', '%Y-%m-%d')
    data = g.get_market_data(
                          start_date=start_date-timedelta(days=1000),
                          end_date=start_date,
                          options="unit=1;Period=Q;Fill=Previous")
    for r, d in data.items():
        g.market.data_source.write2csv(r, d)
    res = g.apply_rules(data)
    print(len(data), len(res))
    for c in res.keys():
        print(c, res[c]['sec_name'].iloc[0])


if __name__ == '__main__':
    main()