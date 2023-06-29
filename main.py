from utils.json_utils import JsonUtils
from utils.pandas_utils import PandasUtils
from services.update_db_service import UpdateDB


# url = "https://fmsampaio.github.io/helper-sites/json-examples/disciplinas.json"
# # url = "https://fmsampaio.github.io/helper-sites/json-examples/alunos.json"

# json = JsonUtils(url).__json__()

# print(PandasUtils().jsonToDataframe(json))

UpdateDB().updateTableEstudantes()