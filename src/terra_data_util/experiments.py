
import json

import firecloud
import firecloud.api as fapi
from firecloud import fiss


# dir(fapi)
# help(fapi)
#
# dir(fiss)
# help(fiss)

namespace="anvil-stage-demo"
workspace="mbaumann dev fiss debug playground 20190925 2141"

result = fapi.list_entity_types(namespace, workspace)
table_data = json.loads(result.text)
print(json.dumps(table_data, indent=4))
print(f"Table names: {table_data.keys()}")

total_attribute_count = 0
tables_with_case = []
tables_with_sample = []
for k, v in table_data.items():
    attribute_names = v['attributeNames']
    total_attribute_count += len(attribute_names)
    id_name = v['idName']
    if "case" in attribute_names or "case" in id_name:
        tables_with_case.append(k)
    if "sample" in attribute_names or "sample" in id_name:
        tables_with_sample.append(k)

print(f"Total attribute count: {total_attribute_count}")
print(f"Tables with `case`: {tables_with_case} ({len(tables_with_case)})")
print(f"Tables with `sample`: {tables_with_sample} ({len(tables_with_sample)})")

assert "sample"in table_data['case'] and "sample"in table_data['aliquot']
assert