from utils.json_utils import JsonUtils
from utils.pandas_utils import PandasUtils


url = "https://fmsampaio.github.io/helper-sites/json-examples/disciplinas.json"

json = JsonUtils(url).__json__()