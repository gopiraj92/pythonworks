
from frameworks.models import frameworks as fws

# print all framework names
print([fw.get("name") for fw in fws])

# print python framework names only
print([fw.get("name") for fw in fws if fw.get("language") == "python"])

# print framework names whose rating > 4 only
print([fw.get("name") for fw in fws if fw.get("rating") > 4])

# print framework names belongs to backend only
print([fw.get("name") for fw in fws if fw.get("belongsto") == "backend"])

# print top rated framework name
print([fw.get("name") for fw in fws])
