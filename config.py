from pathlib import Path
import os

DB_CONNECTION_STRING = f"postgresql://postgres:{os.getenv('pgAdmin')}@localhost:5432/hh_parser"
QUERIES_PATH = str(Path(__file__).resolve().parent / "database" / "queries.sql")
EMPLOYEERS_VACANCY_ID = {
    "ADV": 421950,
    "МФТИ": 1008541,
    "Квантбокс": 2136982,
    "АВСофт": 2355830,
    "Северсталь": 6041,
    "HYPERPC": 1199534,
    "ЛАНИТ": 733,
    "ТЕНЗОР": 1266214,
    "VK": 15478,
    "АйТеко": 115,
    "МДО": 736233,
    "getmatch": 864086,
    "HuntForYou": 4456441,
    "Триафлай": 4514966,
    "точка": 2324020,
    "SitronicsGroup": 35065,
    "STEPLOGIC": 2168579,
    "Ventra": 1838,
    "RAMAXGroup": 142514,
    "ASTON": 6093775,
    "HFLabs": 15589,
    "Аксофт": 1008388,
    "IBS": 139,
    "Крит": 1115346,
    "Айтеко": 115,
    "softline": 2381,
    "Рексфот": 3984,
    "ПервыйБит": 3177,
    "Алгоритмика": 2657797
}
