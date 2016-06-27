import os
from sql.mlb_database import mlb_database
from mine.rotowire import mine_pregame_stats
from mine.draft_kings import Draftkings
from datetime import date, timedelta
from email_service import send_email
import cProfile

os.chdir("/home/cameron/workspaces/MlbDatabase/mlb_scrape/Released/mlbscrape_python")

databaseSession = mlb_database.open_session()

cProfile.run('mine_pregame_stats(mlb_database)')
Draftkings.save_daily_csv()
csv_dict = Draftkings.get_csv_dict()
Draftkings.update_salaries(databaseSession, csv_dict)
Draftkings.predict_daily_points(databaseSession, date.today())
optimal_lineup = Draftkings.get_optimal_lineup(databaseSession, date.today())
print optimal_lineup
send_email(optimal_lineup.__str__())

databaseSession.close()

